from pathlib import Path
from taskGenerator import *
from task import *
import json
root_path = str(Path(__file__).resolve().parents[1])

with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

new_sample = genereate_sample(get_dual_exp_math_expected(0.5, koVariatsiya(sample), matOzhidaniye(sample)), 300, distriutions.DUAL_EXP)


size = len(new_sample)
print(f"Размер: {size}")
print(f"Мат. ож: {matOzhidaniye(new_sample)}")
print(f"Дисперсия: {dispersiya(new_sample)}")
print(f"С.К.О: {sredneKvadraticheskoeOtklonenie(new_sample)}")
print(f"Ковариация: {koVariatsiya(new_sample)}")
print(f"Дов. инт. (0.90): {doveritelniyInterval(new_sample, 0.90)}")
print(f"Дов. инт. (0.95): {doveritelniyInterval(new_sample, 0.95)}")
print(f"Дов. инт. (0.99): {doveritelniyInterval(new_sample, 0.99)}")
