from task import *
import json

with open("../sample.json", "r") as file:
    sample = json.load(file)["sample"]

for shift in range(20):
    print(f"Коэфф. автокорреляции (сдвиг {shift}): {autoCorrelyatsia(sample, shift)}")