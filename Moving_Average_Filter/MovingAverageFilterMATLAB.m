% Moving Average Filter in MATLAB

data = [1, 2, 3, 2, 5, 8, 6, 7]; % Simulated stock prices
windowSize = 3;

smoothedData = movmean(data, windowSize);

disp(smoothedData);
