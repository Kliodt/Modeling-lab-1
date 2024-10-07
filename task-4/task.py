import json
import math
from pathlib import Path

from matplotlib import pyplot as plt

root_path = str(Path(__file__).resolve().parents[1])


with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

plt.hist(sample, color='aquamarine', ec='black', linewidth=0.05, bins=3 * (1 + int(math.log2(len(sample)))), density=True)
plt.show()