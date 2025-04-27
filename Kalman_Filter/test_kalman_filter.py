import numpy as np
from kalman_filter import kalman_filter

def test_kalman_filter_simple():
    measurements = np.array([1, 2, 3])
    estimates = kalman_filter(measurements)

    # Basic sanity checks
    assert len(estimates) == len(measurements), "Number of estimates should match measurements"
    assert np.all(np.isfinite(estimates)), "All estimates should be finite numbers"
    print("Simple Kalman filter test passed.")

if __name__ == "__main__":
    test_kalman_filter_simple()

