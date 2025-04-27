% ar1_simulation.m
% Simulates an AR(1) process and plots the result

n = 50;          % Number of points
phi = 0.8;       % AR(1) coefficient
sigma = 0.5;     % Standard deviation of noise

x = zeros(1, n); % Initialize the series
x(1) = 0;        % Initial value

for t = 2:n
    x(t) = phi * x(t-1) + sigma * randn;
end

plot(x);
title('Simulated AR(1) Process');
xlabel('Time');
ylabel('Value');
grid on;

