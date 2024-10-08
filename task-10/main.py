import json
import math
from pathlib import Path
from taskGenerator import *
from matplotlib import pyplot as plt
from task import *

root_path = str(Path(__file__).resolve().parents[1])


with open(f"{root_path}/sample.json", "r") as file:
    sample1 = json.load(file)["sample"]

sample2 = genereate_sample(get_dual_exp_math_expected(0.5, koVariatsiya(sample), matOzhidaniye(sample)), 300, distriutions.DUAL_EXP)

print(f"Корреляция{correlyatsia(sample1, sample2)}")