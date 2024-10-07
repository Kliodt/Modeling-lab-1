from pathlib import Path

import matplotlib.pyplot as plt
import json

root_path = str(Path(__file__).resolve().parents[1])
with open(f"{root_path}/sample.json", "r") as file:
    sample = json.load(file)["sample"]

plt.plot(sample)
plt.show()
