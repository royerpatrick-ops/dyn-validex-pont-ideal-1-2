"""Exact rational Simpson enclosure of the ideal bridge; no RNG or model import.

Taylor jets contain interval enclosures of f^(j)/j!, j=0..4. Arithmetic
recurrences follow formal power series; sqrt bounds use integer isqrt only.
The certificate concerns I_[1,2] in unnormalized ideal-integral units.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import time


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self):
        object.__setattr__(self, 'lo', Q(self.lo))
        object.__setattr__(self, 'hi', Q(self.hi))
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    @staticmethod
    def cast(x):
        return x if isinstance(x, Interval) else Interval(Q(x), Q(x))

    def __add__(self, other):
        other = self.cast(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        other = self.cast(other)
        products = (self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError('division interval contains zero')
        return Interval(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * self.cast(other).reciprocal()

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError('nonnegative integer power required')
        result = Interval(1,1)
        for _ in range(n):
            result = result*self
        return result

    def abs_bound(self):
        return max(abs(self.lo), abs(self.hi))

    def to_json(self):
        return {'lower': fraction_text(self.lo), 'upper': fraction_text(self.hi)}


def sqrt_bound(x, bits):
    x = Q(x)
    if x < 0:
        raise ValueError('negative square root argument')
    scale = 1 << bits
    k = isqrt((x.numerator << (2*bits)) // x.denominator)
    lo = Q(k,scale)
    hi = lo if lo*lo == x else Q(k+1,scale)
    assert lo*lo <= x <= hi*hi
    return Interval(lo,hi)


def sqrt_interval(x, bits):
    return Interval(sqrt_bound(x.lo,bits).lo, sqrt_bound(x.hi,bits).hi)


class Jet:
    order = 4

    def __init__(self, coefficients):
        if len(coefficients) != self.order+1:
            raise ValueError('five Taylor coefficients required')
        self.c = tuple(Interval.cast(x) for x in coefficients)

    @classmethod
    def constant(cls, x):
        return cls([x]+[0]*cls.order)

    @classmethod
    def variable(cls, x):
        return cls([x,1]+[0]*(cls.order-1))

    @classmethod
    def cast(cls, x):
        return x if isinstance(x,cls) else cls.constant(x)

    def __add__(self, other):
        other = self.cast(other)
        return Jet([x+y for x,y in zip(self.c,other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Jet([-x for x in self.c])

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        other = self.cast(other)
        return Jet([sum((self.c[k]*other.c[n-k] for k in range(n+1)),Interval(0,0))
                    for n in range(self.order+1)])

    __rmul__ = __mul__

    def reciprocal(self):
        b = [self.c[0].reciprocal()]
        for n in range(1,self.order+1):
            b.append(-b[0]*sum((self.c[k]*b[n-k] for k in range(1,n+1)),Interval(0,0)))
        return Jet(b)

    def __truediv__(self, other):
        return self*self.cast(other).reciprocal()

    def __pow__(self, n):
        if not isinstance(n,int) or n < 0:
            raise ValueError('nonnegative integer power required')
        result = Jet.constant(1)
        for _ in range(n):
            result = result*self
        return result

    def sqrt(self,bits):
        if self.c[0].lo <= 0:
            raise ValueError('strict positivity required for sqrt derivatives')
        b = [sqrt_interval(self.c[0],bits)]
        for n in range(1,self.order+1):
            middle = sum((b[k]*b[n-k] for k in range(1,n)),Interval(0,0))
            b.append((self.c[n]-middle)/(2*b[0]))
        return Jet(b)


def expression(a,t,bits):
    z = (t**2/4 + 2*(a.reciprocal()**3)).sqrt(bits)
    return (a**7/24)*t*(1-t)*(2*z-1)*(z**2+2*z-1)


def derivative_bounds(bits):
    A,T = Interval(1,2),Interval(0,1)
    ja = expression(Jet.variable(A),Jet.constant(T),bits)
    jt = expression(Jet.constant(A),Jet.variable(T),bits)
    Ma,Mt = factorial(4)*ja.c[4].abs_bound(),factorial(4)*jt.c[4].abs_bound()
    return Ma,Mt,{'a_jet_coefficients':[v.to_json() for v in ja.c],
                  't_jet_coefficients':[v.to_json() for v in jt.c]}


def point_value(a,t,bits):
    z = sqrt_bound(t*t/4+2/(a**3),bits)
    return (a**7/24)*t*(1-t)*(2*z-1)*(z*z+2*z-1)


def simpson_weight(i,n):
    return 1 if i in (0,n) else (4 if i%2 else 2)


def required_grid(bound,width_target):
    n = 2
    while bound/(180*n**4) > width_target/8:
        n *= 2
    return n


def fraction_text(x):
    x=Q(x)
    return f'{x.numerator}/{x.denominator}'


def outward_decimal(x,places,upper=False):
    x=Q(x)
    scale=10**places
    n = -((-x.numerator*scale)//x.denominator) if upper else x.numerator*scale//x.denominator
    sign='-' if n<0 else ''
    n=abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'


def certify(output,bits,target, max_nodes):
    start=time.monotonic()
    Ma,Mt,jets=derivative_bounds(bits)
    na,nt=required_grid(Ma,target),required_grid(Mt,target)
    nodes=(na+1)*(nt+1)
    if nodes>max_nodes:
        raise ValueError(f'grid requires {nodes} nodes above deterministic budget {max_nodes}')
    total=Interval(0,0)
    for i in range(na+1):
        a=1+Q(i,na)
        row=Interval(0,0)
        for j in range(nt+1):
            t=Q(j,nt)
            row += simpson_weight(j,nt)*point_value(a,t,bits)
        total += simpson_weight(i,na)*row
    simpson=total/(9*na*nt)
    error_a=Ma/(180*na**4)
    error_t=Mt/(180*nt**4)
    error=error_a+error_t
    I1=simpson+Interval(-error,error)
    I0=Interval.cast(Q(233591,322560))-(Q(128,315)*sqrt_bound(Q(2),bits))
    result=I0+I1
    assert result.hi-result.lo <= target
    payload={'schema':'DYN-IDEAL-BRIDGE-1-2-RATIONAL-QUADRATURE-CERTIFICATE-v0.1',
             'status':'PASS_RATIONAL_IDEAL_BRIDGE_ENCLOSURE',
             'units':'I_[1,2]=integral_1^2 a E_Pa[c] da; unnormalized ideal integral',
             'depends_on_mathematical_reduction':'H and G partition proofs; internal independent review required',
             'integrand':'a^7/24*t*(1-t)*(2*z-1)*(z^2+2*z-1), z=sqrt(t^2/4+2/a^3)',
             'domain':{'a':['1','2'],'t':['0','1']},
             'square_root_lower_bound':'1/2',
             'arithmetic':'fractions.Fraction, exact integers, integer isqrt; no floating point in enclosure',
             'sqrt_dyadic_bits':bits, 'requested_maximum_width':fraction_text(target),
             'fourth_partial_derivative_bounds':{'Ma':fraction_text(Ma),'Mt':fraction_text(Mt),**jets},
             'grid':{'a_subintervals':na,'t_subintervals':nt,'nodes':nodes,'rule':'tensor composite Simpson; rational dyadic nodes and positive weights'},
             'quadrature_error_theorem':'abs(I1-Q_aQ_t F)<=Ma/(180*Na^4)+Mt/(180*Nt^4)',
             'quadrature_error':{'a':fraction_text(error_a),'t':fraction_text(error_t),'total':fraction_text(error)},
             'simpson_node_interval':simpson.to_json(),
             'I1_enclosure':I1.to_json(), 'I0_exact':'233591/322560-128*sqrt(2)/315',
             'I0_enclosure':I0.to_json(), 'I_bridge_enclosure':result.to_json(),
             'I_bridge_outward_decimal_9_places':[outward_decimal(result.lo,9),outward_decimal(result.hi,9,True)],
             'enclosure_width':fraction_text(result.hi-result.lo),
             'limits':['Ideal compact bridge only; no global C, canonical units or 6/pi^2 factor.',
                       'No numeric-to-continuous transport of P2 results.',
                       'Software and mathematical review are internal IA checks, not formal proof-assistant certification.'],
             'new_rng_created_or_consumed':False,'new_P2_or_replication':False,'frozen_ledger_modified':False,
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'compute_elapsed_seconds_diagnostic':time.monotonic()-start}
    output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'grid':payload['grid'],'I_bridge_outward_decimal_9_places':payload['I_bridge_outward_decimal_9_places'],
                      'compute_elapsed_seconds_diagnostic':payload['compute_elapsed_seconds_diagnostic']}))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--bits',type=int,default=64)
    parser.add_argument('--width',type=Q,default=Q(1,1000000))
    parser.add_argument('--max-nodes',type=int,default=300000)
    parser.add_argument('--bounds-only',action='store_true')
    args=parser.parse_args()
    if args.bits<16 or args.width<=0 or args.max_nodes<9:
        parser.error('invalid deterministic certificate parameters')
    if args.bounds_only:
        Ma,Mt,jets=derivative_bounds(args.bits)
        na,nt=required_grid(Ma,args.width),required_grid(Mt,args.width)
        print(json.dumps({'Ma':fraction_text(Ma),'Mt':fraction_text(Mt),'Na':na,'Nt':nt,'nodes':(na+1)*(nt+1),**jets}))
    else:
        certify(args.output,args.bits,args.width,args.max_nodes)


if __name__=='__main__':
    main()
