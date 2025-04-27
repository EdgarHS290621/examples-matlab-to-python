import numpy as np

# Simple Kalman Filter Example in Python

x = 0  # Initial estimate
P = 1  # Initial uncertainty
Q = 0.1  # Process noise covariance
R = 0.5  # Measurement noise covariance

measurements = np.array([1, 2, 3])  # Example measurements

for measurement in measurements:
    # Prediction
    P = P + Q
    
    # Measurement update
    K = P / (P + R)
    x = x + K * (measurement - x)
    P = (1 - K) * P
    
    print(f"Updated state: {x:.2f}")

