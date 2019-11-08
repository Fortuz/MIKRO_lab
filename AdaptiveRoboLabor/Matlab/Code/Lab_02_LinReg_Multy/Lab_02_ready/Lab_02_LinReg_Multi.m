%% Machine Learning
% Lab 2: Linear Regression with Multiple variable
% --- Housing Prices ----
%{
In this part, you will implement linear regression with multiple variables to
predict the prices of houses. Suppose you are selling your house and you
want to know what a good market price would be. One way to do this is to
first collect information on recent houses sold and make a model of housing
prices.
%}

%% %% Initialization
clear ; close all; clc % Clear and close figures
%% Load Data
fprintf('Loading data ...\n');
data = load('ex1data2.txt');
fprintf('First 5 element of original data:\n')
data(1:5, :)

%% Parsing data
X_origin = data(:, 1:2);
X = data(:, 1:2); % x1:size (0-2000 feet^2) and x2: number of bedrooms (1-5)
Y = data(:, 3); % dollar
m = length(Y);

% Print out some data points
fprintf('First 10 examples from the dataset: \n');
fprintf(' x = [%.0f %.0f], y = %.0f \n', [X(1:10,:) Y(1:10,:)]');

%% Scale Features and set them to zero mean
% Feature scaling and mean normalization:
% Scale features and set them to zero mean
fprintf('Normalizing Features ...\n');

[X avg sigma] = featureNormalize(X);

% Add intercept term to X
X = [ones(m, 1) X];


%% Gradient Descent
fprintf('Running gradient descent ...\n');

% Choose some learning_rate value
lr = 0.01; % learning_rate
epochs = 400;

% Init Weights and run Gradient Descent
w = zeros(3,1);
[w, C_history] = gradientDescentMulti(X, Y, w, lr, epochs);

%% Plot the convergence graph
figure;
plot(1:numel(C_history), C_history, '-b', 'LineWidth', 2);
% n = numel(A) returns the number of elements, n, in array A, equivalent to prod(size(A)).
xlabel('Number of iterations');
ylabel('Cost Function (C)');

% Display gradient descent's result
fprintf('Weights computed from gradient descent: \n');
fprintf(' %f \n', w);
fprintf('\n');

%% Estimate the price of a 1650 sq-ft, 3 br house
% Recall that the first column of X is all-ones. Thus, it does
% not need to be normalized.
FEET = 1650;
BED = 3;
price = [1 (FEET-avg(1))/sigma(1) (BED-avg(2))/sigma(2)]*w;
%Predicted price should be: $293081.464335

fprintf(['Predicted price of a 1650 sq-ft, 3 br house ' ...
         '(using gradient descent):\n $%f\n'], price);
