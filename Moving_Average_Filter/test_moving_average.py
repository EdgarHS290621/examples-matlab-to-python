import numpy as np
import pandas as pd

def moving_average(data, window_size):
    return pd.Series(data).rolling(window=window_size).mean().to_numpy()

def test_moving_average():
    data = np.array([1, 2, 3, 4, 5])
    expected_output = np.array([np.nan, np.nan, 2.0, 3.0, 4.0])
    output = moving_average(data, 3)
    np.testing.assert_almost_equal(output, expected_output, decimal=1)

if __name__ == "__main__":
    test_moving_average()
    print("Test passed!")

