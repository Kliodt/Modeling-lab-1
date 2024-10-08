from pathlib import Path
from taskGenerator import *
from task import *
import json

root_path = str(Path(__file__).resolve().parents[1])
with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

new_sample = genereate_sample(get_dual_exp_math_expected(0.5, koVariatsiya(sample), matOzhidaniye(sample)), 300, distriutions.DUAL_EXP)

for shift in range(20):
    print(f"Коэфф. автокорреляции (сдвиг {shift}): {autoCorrelyatsia(new_sample, shift)}")