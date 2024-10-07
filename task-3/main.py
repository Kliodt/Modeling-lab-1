from pathlib import Path

from task import *
import json

root_path = str(Path(__file__).resolve().parents[1])
with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

for shift in range(20):
    print(f"Коэфф. автокорреляции (сдвиг {shift}): {autoCorrelyatsia(sample, shift)}")