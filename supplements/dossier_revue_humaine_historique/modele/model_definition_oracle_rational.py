"""Oracle rationnel pur pour l'observable du premier rang occupé."""

from dataclasses import asdict, dataclass
from fractions import Fraction
import math


def as_fraction(value):
    if isinstance(value, bool):
        raise ValueError("boolean interdit")
    if isinstance(value, Fraction):
        result = value
    elif isinstance(value, int):
        result = Fraction(value)
    elif isinstance(value, float) and math.isfinite(value):
        result = Fraction(value)
    else:
        raise ValueError("int, float fini ou Fraction requis")
    return result


def floor_fraction(value):
    value = as_fraction(value)
    return value.numerator // value.denominator


def ceil_fraction(value):
    value = as_fraction(value)
    return -((-value.numerator) // value.denominator)


def fraction_text(value):
    value = as_fraction(value)
    return f"{value.numerator}/{value.denominator}"


def constructive_kmax(a, delta):
    a, delta = map(as_fraction, (a, delta))
    if a <= 0 or not 0 <= delta < 1 / a:
        raise ValueError("a>0 et 0<=delta<1/a requis")
    return max(0, ceil_fraction(a**3 / 8 - a * delta))


def row_extrema(a, delta, s, beta, k):
    a, delta, s, beta = map(as_fraction, (a, delta, s, beta))
    if a <= 0 or not 0 <= delta < 1 / a or not 0 <= s < a:
        raise ValueError("domaine rationnel invalide")
    if isinstance(k, bool) or not isinstance(k, int) or k < 0:
        raise ValueError("k entier positif requis")
    d = delta + Fraction(k) / a
    offset = s + k * beta
    common = math.lcm(offset.denominator, a.denominator)
    offset_integer = offset.numerator * (common // offset.denominator)
    step_integer = a.numerator * (common // a.denominator)
    threshold = 2 * d
    squared_cap = threshold.numerator * common * common // threshold.denominator
    radius_integer = math.isqrt(squared_cap)
    j_min = ceil_fraction(Fraction(-radius_integer - offset_integer, step_integer))
    j_max = floor_fraction(Fraction(radius_integer - offset_integer, step_integer))
    if j_min > j_max:
        return d, None, None
    return d, j_min, j_max


@dataclass(frozen=True)
class OracleResult:
    k: int
    d: Fraction
    j_min: int
    j_max: int
    point_count: int
    x_min: Fraction
    x_max: Fraction
    c: Fraction
    constructive_kmax: int
    d_bound: Fraction
    support_square_verified: bool
    lower_neighbor_outside: bool
    upper_neighbor_outside: bool

    def to_record(self):
        raw = asdict(self)
        for key in ("d", "x_min", "x_max", "c", "d_bound"):
            raw[key] = fraction_text(raw[key])
        return raw


def first_occupied(a, delta, s, beta):
    a, delta, s, beta = map(as_fraction, (a, delta, s, beta))
    limit = constructive_kmax(a, delta)
    for k in range(limit + 1):
        d, j_min, j_max = row_extrema(a, delta, s, beta, k)
        if j_min is None:
            continue
        x_min = s + k * beta + j_min * a
        x_max = s + k * beta + j_max * a
        point_count = j_max - j_min + 1
        c = Fraction(0)
        if point_count >= 2:
            c = d * (x_max - x_min) - (x_max**3 - x_min**3) / 3
        lower = s + k * beta + (j_min - 1) * a
        upper = s + k * beta + (j_max + 1) * a
        d_bound = a**2 / 8 + 1 / a
        return OracleResult(
            k=k,
            d=d,
            j_min=j_min,
            j_max=j_max,
            point_count=point_count,
            x_min=x_min,
            x_max=x_max,
            c=c,
            constructive_kmax=limit,
            d_bound=d_bound,
            support_square_verified=c * c <= 8 * d_bound**3,
            lower_neighbor_outside=lower * lower > 2 * d,
            upper_neighbor_outside=upper * upper > 2 * d,
        )
    raise ArithmeticError("borne constructive violee")

