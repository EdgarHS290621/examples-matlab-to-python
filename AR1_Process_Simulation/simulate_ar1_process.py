import numpy as np
import matplotlib.pyplot as plt

def simulate_ar1_process(n, phi, sigma, plot=True):
    """
    Simulates an AR(1) process.

    Parameters:
    - n (int): Number of points
    - phi (float): AR coefficient
    - sigma (float): Standard deviation of noise
    - plot (bool): Whether to plot the series

    Returns:
    - np.array: The simulated series
    """
    x = np.zeros(n)
    x[0] = 0

    for t in range(1, n):
        x[t] = phi * x[t-1] + sigma * np.random.randn()

    if plot:
        plt.plot(x)
        plt.title('Simulated AR(1) Process')
        plt.show()

    return x

if __name__ == "__main__":
    simulate_ar1_process(50, 0.8, 0.5)

