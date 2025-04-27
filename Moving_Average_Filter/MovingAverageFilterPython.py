import numpy as np
import pandas as pd

# Moving Average Filter in Python

data = np.array([1, 2, 3, 2, 5, 8, 6, 7])  # Simulated stock prices
window_size = 3

smoothed_data = pd.Series(data).rolling(window=window_size).mean()

print(smoothed_data.to_numpy())

