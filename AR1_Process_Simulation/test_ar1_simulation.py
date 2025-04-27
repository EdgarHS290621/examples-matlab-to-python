import numpy as np
from ar1_simulation import simulate_ar1_process

def test_ar1_simulation_length():
    """Test to check the length of the simulated AR(1) series."""
    n_points = 50
    phi = 0.8
    sigma = 0.5
    series = simulate_ar1_process(n_points, phi, sigma)
    
    assert len(series) == n_points, "Length of the series should match the number of points requested."
    print("Test passed: Correct length of AR(1) series.")

def test_ar1_simulation_values():
    """Test to check that the series values are finite numbers (no NaNs or infinities)."""
    n_points = 50
    phi = 0.8
    sigma = 0.5
    series = simulate_ar1_process(n_points, phi, sigma)
    
    assert np.all(np.isfinite(series)), "All values in the AR(1) series should be finite."
    print("Test passed: All values are finite.")

if __name__ == "__main__":
    test_ar1_simulation_length()
    test_ar1_simulation_values()

