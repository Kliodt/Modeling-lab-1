import math

def get_dual_exp_math_expected(q: float, v: float, t: float):
    return ((1 + math.sqrt((1 - q)* (v * v - 1) / (2 * q))) * t, ((q) * (v * v - 1) / (2 - 2 * q)) * t)

