"""Exact, deterministic checks of the bridge partition, not draw fixtures."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def indices_from_table(a,r,q):
    assert a>0 and 0<=r<3*a/2 and 0<=q<a
    if r<a/2:
        if q<=r:
            return [0]
        if q<a-r:
            return []
        return [-1]
    if r<a:
        if q<a-r:
            return [0]
        if q<=r:
            return [-1,0]
        return [-1]
    if q<=r-a:
        return [-1,0,1]
    if q<2*a-r:
        return [-1,0]
    return [-2,-1,0]


def direct_indices(a,d,offset):
    # In this check the support is shorter than 3a and offsets are in [0,2a).
    return [j for j in range(-4,5) if (offset+j*a)**2<=2*d]


def direct_c(a,d,offset,indices):
    if len(indices)<2:
        return Q(0)
    x1,x2=offset+indices[0]*a,offset+indices[-1]*a
    return d*(x2-x1)-(x2**3-x1**3)/3


def table_c(a,d,q,indices):
    if len(indices)<2:
        return Q(0)
    if indices==[-1,0]:
        return a*d-a*q*q+a*a*q-a**3/3
    if indices==[-1,0,1]:
        return 2*a*d-2*a*q*q-2*a**3/3
    if indices==[-2,-1,0]:
        return 2*a*d-2*a*(q-a)**2-2*a**3/3
    raise AssertionError(indices)


def integral_polynomial(coefficients,lo,hi):
    return sum((c*(hi**(i+1)-lo**(i+1))/Q(i+1) for i,c in enumerate(coefficients)),Q(0))


def H_from_partition(a,r):
    d=r*r/2
    if r<a/2:
        return Q(0)
    c2=[a*d-a**3/3,a*a,-a]
    if r<a:
        return integral_polynomial(c2,a-r,r)/a
    cl=[2*a*d-2*a**3/3,Q(0),-2*a]
    cr=[2*a*d-8*a**3/3,4*a*a,-2*a]
    return (integral_polynomial(cl,Q(0),r-a)+integral_polynomial(c2,r-a,2*a-r)
            +integral_polynomial(cr,2*a-r,a))/a


def text(x):
    return f'{x.numerator}/{x.denominator}' if isinstance(x,Q) else x


def main():
    geometry=0; ranks=0; averages=0; contacts=[]
    for a in map(Q,(1,Q(5,4),Q(4,3),Q(3,2),2)):
        for ratio in map(Q,(0,Q(1,8),Q(1,4),Q(1,2),Q(3,4),1,Q(5,4),Q(191,128))):
            r=a*ratio; d=r*r/2
            candidates={Q(0),a/2,a-Q(1,4096)*a}
            for value in (r,a-r,r-a,2*a-r):
                candidates.update((value-a/4096,value,value+a/4096))
            candidates.update(a*Q(i,16) for i in range(16))
            for q in sorted(x for x in candidates if 0<=x<a):
                predicted=indices_from_table(a,r,q)
                actual=direct_indices(a,d,q)
                assert predicted==actual
                assert table_c(a,d,q,predicted)==direct_c(a,d,q,actual)
                geometry+=1
                if q in (r,a-r,r-a,2*a-r):
                    contacts.append({'a':text(a),'r':text(r),'q':text(q),'indices':actual,'c':text(direct_c(a,d,q,actual))})
            H=H_from_partition(a,r)
            expected=Q(0) if r<a/2 else Q(2,3)*d*r+a*d-Q(2,3)*a*a*r+a**3/6
            assert H==expected
            averages+=1
        delta_values={Q(0),1/(16*a),1/(4*a),1/(2*a),15/(16*a),a*a/8,a*a/2,a*a/2-1/a}
        delta_values.update((a*v)**2/2 for v in (Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1)))
        for delta in sorted(x for x in delta_values if 0<=x<1/a):
            s_values={a*Q(i,8) for i in range(8)}
            for ratio in (Q(0),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                r=a*ratio
                if r*r==2*delta:
                    for value in (r,a-r):
                        s_values.update((value-a/4096,value,value+a/4096))
            for s in sorted(x for x in s_values if 0<=x<a):
                beta_values={Q(0),a/8,a/2,7*a/8}
                if s>0:
                    beta_values.update((a-s-a/4096,a-s,a-s+a/4096))
                for beta in sorted(x for x in beta_values if 0<=x<a):
                    # Strict squared emptiness preserves occupied contacts.
                    k_expected=int(delta<a*a/8 and s*s>2*delta and (a-s)**2>2*delta)
                    row0=direct_indices(a,delta,s)
                    k_actual=0 if row0 else 1
                    assert k_expected==k_actual
                    offset=s+k_actual*beta; d=delta+Q(k_actual)/a
                    raw_indices=direct_indices(a,d,offset)
                    assert 1<=len(raw_indices)<=3
                    _,q=divmod(offset,a)
                    shifted=direct_indices(a,d,q)
                    assert direct_c(a,d,offset,raw_indices)==table_c(a,d,q,shifted)
                    if k_actual:
                        assert d>=a*a/8
                    ranks+=1
    qh=Q(1,480)+Q(1,128)-Q(1,36)+Q(1,48)
    assert qh==Q(17,5760)
    i0rational=Q(32,15)+1-Q(128,63)-Q(17,180)-(Q(1,4)+Q(1,30)-Q(17,46080))
    i0sqrt=-Q(8,15)+Q(8,63)
    assert i0rational==Q(233591,322560) and i0sqrt==-Q(128,315)
    payload={'status':'PASS_EXACT_BRIDGE_PARTITION_CHECKS','geometry_cases':geometry,
             'rank_and_contribution_cases':ranks,'phase_average_integrals_checked':averages,
             'closed_contacts_checked':contacts,'closed_contact_count':len(contacts),
             'Q_at_h_coefficient':text(qh),'I0_coefficients':{'rational':text(i0rational),'sqrt2':text(i0sqrt)},
             'model_or_sampler_imported':False,'rng_created_or_consumed':False,'P2_called':False,
             'prospective_or_archived_raw_words_used':False,'new_frozen_fixture':False,
             'method':'Fraction direct finite lattice enumeration vs phase table, exact polynomial phase integration and rank tests; finite cases accompany analytic proof.',
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path('bridge_partition_checks_work.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:payload[k] for k in ('status','geometry_cases','rank_and_contribution_cases','phase_average_integrals_checked','closed_contact_count')}))


if __name__=='__main__':
    main()
