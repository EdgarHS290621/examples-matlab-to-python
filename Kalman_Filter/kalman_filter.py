import numpy as np

def kalman_filter(measurements, initial_estimate=0, initial_uncertainty=1, 
                  process_noise=0.1, measurement_noise=0.5):
    """
    Applies a simple 1D Kalman Filter to a list of measurements.

    Parameters:
    - measurements (list or np.array): Sequence of measurements
    - initial_estimate (float): Initial state estimate
    - initial_uncertainty (float): Initial uncertainty
    - process_noise (float): Process noise covariance (Q)
    - measurement_noise (float): Measurement noise covariance (R)

    Returns:
    - np.array: Updated state estimates after each measurement
    """
    x = initial_estimate
    P = initial_uncertainty

    estimates = []

    for measurement in measurements:
        # Prediction step
        P = P + process_noise
        
        # Measurement update step
        K = P / (P + measurement_noise)
        x = x + K * (measurement - x)
        P = (1 - K) * P

        estimates.append(x)

    return np.array(estimates)

if __name__ == "__main__":
    # Example usage
    measurements = np.array([1, 2, 3])
    estimates = kalman_filter(measurements)
    print(estimates)

