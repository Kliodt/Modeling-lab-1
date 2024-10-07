import matplotlib.pyplot as plt
import json

with open("../sample.json", "r") as file:
    sample = json.load(file)["sample"]

plt.plot(sample)
plt.show()
