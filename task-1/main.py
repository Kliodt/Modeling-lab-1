from pathlib import Path

from task import *
import json
root_path = str(Path(__file__).resolve().parents[1])

with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

for size in [10, 20, 50, 100, 200, 300]:
    sizedSample = sample[:size]
    print("-" * 50)
    print(f"Размер: {size}")
    print(f"Мат. ож: {matOzhidaniye(sizedSample)}")
    print(f"Дисперсия: {dispersiya(sizedSample)}")
    print(f"С.К.О: {sredneKvadraticheskoeOtklonenie(sizedSample)}")
    print(f"Ковариация: {koVariatsiya(sizedSample)}")
    print(f"Дов. инт. (0.90): {doveritelniyInterval(sizedSample, 0.90)}")
    print(f"Дов. инт. (0.95): {doveritelniyInterval(sizedSample, 0.95)}")
    print(f"Дов. инт. (0.99): {doveritelniyInterval(sizedSample, 0.99)}")