import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import numpy as np

# Sample data
df = pd.read_csv("/output.csv",
                 header=0, usecols=[f"increment{2 ** x}" for x in range(7)])

ax = df.T.plot(figsize=(7, 6))

# Add legend and labels
plt.xlabel('Increments')
plt.ylabel('Percentage of Trapezoidal Sum')
plt.title('Increments vs Percentage of Last Calculated Sum')

plt.show()
