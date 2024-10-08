import json
import math
from enum import Enum
from pathlib import Path
from random import random

import numpy.random


class distriutions(Enum):
    DUAL_EXP = 1
    EXP = 2


root_path = str(Path(__file__).resolve().parents[1])

with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]


def get_dual_exp_math_expected(q: float, v: float, t: float):
    return (
    q, (1 + math.sqrt((1 - q) * (v * v - 1) / (2 * q))) * t, (1 - math.sqrt((q) * (v * v - 1) / (2 - 2 * q))) * t)


def matOzhidaniye(sample) -> float:
    return sum(sample) / len(sample)


def dispersiya(sample) -> float:
    mx = matOzhidaniye(sample)
    return sum([(x - mx) ** 2 for x in sample]) / (len(sample) - 1)


def sredneKvadraticheskoeOtklonenie(sample) -> float:
    return dispersiya(sample) ** 0.5


def koVariatsiya(sample) -> float:
    return sredneKvadraticheskoeOtklonenie(sample) / matOzhidaniye(sample)


def genereate_sample(distr_info: tuple, n: int, d: distriutions):
    result = []
    if d == distriutions.DUAL_EXP:
        for i in range(n):
            if (random() < distr_info[0]):
                result.append(float(numpy.random.exponential(distr_info[1], 1)[0]))
            else:
                result.append(float(numpy.random.exponential(distr_info[2], 1)[0]))
    if d == distriutions.EXP:
        result = numpy.random.exponential(distr_info[0], n)
    return result
