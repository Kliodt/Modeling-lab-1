from matplotlib import pyplot as plt

from taskGenerator import *

root_path = str(Path(__file__).resolve().parents[1])
with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

new_sample = genereate_sample(get_dual_exp_math_expected(0.5, koVariatsiya(sample), matOzhidaniye(sample)), 300, distriutions.DUAL_EXP)
print(new_sample)
plt.hist(new_sample, color='aquamarine', ec='black', linewidth=0.05, bins=3 * (1 + int(math.log2(len(sample)))), density=True)
plt.show()