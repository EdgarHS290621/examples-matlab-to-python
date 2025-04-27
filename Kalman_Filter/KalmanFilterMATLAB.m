% Simple Kalman Filter Example in MATLAB

x = 0; % Initial estimate
P = 1; % Initial uncertainty
Q = 0.1; % Process noise covariance
R = 0.5; % Measurement noise covariance

measurements = [1, 2, 3]; % Example measurements

for i = 1:length(measurements)
    % Prediction
    P = P + Q;
    
    % Measurement update
    K = P / (P + R);
    x = x + K * (measurements(i) - x);
    P = (1 - K) * P;
    
    fprintf('Updated state: %.2f\n', x);
end

