from pathlib import Path
import matplotlib.pyplot as plt

from task import *
import json

root_path = str(Path(__file__).resolve().parents[1])
with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

array = []
for shift in range(1, 11):
    cor = autoCorrelyatsia(sample, shift)
    array.append(cor)
    print(f"Коэфф. автокорреляции (сдвиг {shift}): {cor}")

plt.plot(array)
plt.show()