import json
import math

from matplotlib import pyplot as plt

with open("../sample.json", "r") as file:
    sample = json.load(file)["sample"]

plt.hist(sample, color='aquamarine', ec='black', linewidth=0.05, bins=3 * (1 + int(math.log2(len(sample)))), density=True)
plt.show()