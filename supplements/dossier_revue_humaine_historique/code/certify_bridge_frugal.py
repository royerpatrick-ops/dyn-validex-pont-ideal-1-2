"""Deterministic rational Simpson enclosure of the ideal [1,2] bridge.

This is not a P2 process or a draw fixture. It creates no RNG and reads no
sampler, worker, campaign archive, candidate, or frozen ledger. Mathematical
input: the ideal continuous law stated in the companion derivation note.

Fourth-derivative bounds must be justified by the companion proof rather
than inferred from the numerical checks in this program.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import time


def sqrt_bounds(q, denominator):
    if q < 0:
        raise ValueError("Negative square-root argument")
    n = isqrt(q.numerator * denominator * denominator // q.denominator)
    lo = Q(n, denominator)
    exact = lo * lo == q
    hi = lo if exact else Q(n + 1, denominator)
    assert lo * lo <= q <= hi * hi
    return lo, hi


def ordered_interval_mul(c, lo, hi):
    return (c * lo, c * hi) if c >= 0 else (c * hi, c * lo)


def node_bounds(a, u, denominator):
    q = 2 / a + a * a * u * u / 4
    rlo, rhi = sqrt_bounds(q, denominator)
    # F = u(1-u) [B*r + P]. B and P are exact rationals.
    b = a**3 / 6 + a**6 * (u * u - 8) / 48
    p = a**4 / 4 + a**7 * (1 + 3 * u * u / 4) / 24
    blo, bhi = ordered_interval_mul(b, rlo, rhi)
    w = u * (1 - u)
    return w * (blo + p), w * (bhi + p)


def weight(i, n):
    return 1 if i in (0, n) else (4 if i % 2 else 2)


def outward_decimal(q, places, direction):
    scale = 10**places
    n = q.numerator * scale
    if direction == "lower":
        units = n // q.denominator
    elif direction == "upper":
        units = -((-n) // q.denominator)
    else:
        raise ValueError("Unknown outward rounding direction")
    sign = "-" if units < 0 else ""
    whole, fractional = divmod(abs(units), scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def certify(n=80, sqrt_denominator=10**16):
    if n < 2 or n % 2:
        raise ValueError("Simpson n must be positive and even")
    start = time.perf_counter()
    slo = Q(0)
    shi = Q(0)
    for i in range(n + 1):
        a = Q(n + i, n)
        ai = weight(i, n)
        for j in range(n + 1):
            u = Q(j, n)
            lo, hi = node_bounds(a, u, sqrt_denominator)
            wij = ai * weight(j, n)
            slo += wij * lo
            shi += wij * hi
    slo /= 9 * n * n
    shi /= 9 * n * n
    ma4 = Q(18021, 16)
    mu4 = Q(536)
    truncation = (ma4 + mu4) / (180 * n**4)
    sqrt2lo, sqrt2hi = sqrt_bounds(Q(2), sqrt_denominator)
    i0lo = Q(233591, 322560) - Q(128, 315) * sqrt2hi
    i0hi = Q(233591, 322560) - Q(128, 315) * sqrt2lo
    ilo = i0lo + slo - truncation
    ihi = i0hi + shi + truncation
    result = {
        "status": "RATIONAL_ENCLOSURE_CONDITIONAL_ON_COMPANION_PROOF",
        "quantity": "I_ideal_[1,2] = integral_1^2 a*G(a) da",
        "domain": {"a": [1, 2], "u": [0, 1]},
        "simpson_even_subdivisions_each_axis": n,
        "number_of_nodes": (n + 1)**2,
        "sqrt_denominator": str(sqrt_denominator),
        "fourth_derivative_bounds": {"a": str(ma4), "u": str(mu4)},
        "quadrature_truncation_absolute_bound": str(truncation),
        "sqrt_nodes_interval_width_after_positive_quadrature": str(shi - slo),
        "I0_exact": "233591/322560 - (128/315)*sqrt(2)",
        "I1_simpson_lower_rational": str(slo),
        "I1_simpson_upper_rational": str(shi),
        "I_lower_rational": str(ilo),
        "I_upper_rational": str(ihi),
        "I_interval_width_rational": str(ihi - ilo),
        "I_decimal_outward_12_places": [
            outward_decimal(ilo, 12, "lower"),
            outward_decimal(ihi, 12, "upper"),
        ],
        "rng_created_or_consumed": False,
        "p2_called": False,
        "sampling_or_statistics": False,
        "canonical_factor_applied": False,
        "ledger_modified": False,
        "elapsed_seconds_diagnostic": time.perf_counter() - start,
    }
    return result


if __name__ == "__main__":
    result = certify()
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in (
        "status", "number_of_nodes", "I_decimal_outward_12_places",
        "I_interval_width_rational", "elapsed_seconds_diagnostic")}, indent=2))
