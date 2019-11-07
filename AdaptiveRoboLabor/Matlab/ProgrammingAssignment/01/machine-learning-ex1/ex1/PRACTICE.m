clear ; close all; clc

fprintf('Loading data ...\n');

%% Load Data
data = load('ex1data2.txt');

X_origin = data(:, 1:2);

X = data(:, 1:2);
y = data(:, 3);
m = length(y);

fprintf('\n');
% Print out some data points
fprintf('First 5 examples from the dataset: \n');
fprintf(' x = [%.0f %.0f], y = %.0f \n', [X(1:5,:) y(1:5,:)]');

fprintf('Program paused. Press enter to continue.\n');
pause;

fprintf('\n');
fprintf('Normalizing Features ...\n');
% Feauter normalizing
X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

% (xi-mui)/sigmai
% Implement in a function!!!!!
%[X mu sigma] = featureNormalize(X);
%--------------------------------------------------
for i=1:size(mu,2)
    mu(1,i) = mean(X(:,i)); 
    sigma(1,i) = std(X(:,i));
    X_norm(:,i) = (X(:,i)-mu(1,i))/sigma(1,i);
end
% -------------------------------------------------
fprintf('Mean vector:        [%0.2f, %0.2f] \n',  [mu(1,1), mu(1,2)]);
fprintf('Standard Deviation: [%0.2f, %0.2f] \n',  [sigma(1,1), sigma(1,2)]);
fprintf('\n');
fprintf('First 5 examples from the normalized: \n');
fprintf(' x = [%.2f %.2f]\n', X_norm(1:5,:)');

fprintf('Program paused. Press enter to continue.\n');
pause;
fprintf('\n');

X = [ones(m, 1) X_norm];
fprintf('First 5 examples from the extended X matrix: \n');
fprintf('x = [%.0f %.2f %.2f]\n', X(1:5,:)');

fprintf('Program paused. Press enter to continue.\n');
pause;
fprintf('\n');

fprintf('Running gradient descent ...\n');
% Choose some alpha value
alpha = 0.01;
num_iters = 400;

% Init Theta and Run Gradient Descent 
theta = zeros(3, 1);
%[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters);
%----------------------------------------------------
J_history = zeros(num_iters, 1);
temp = zeros(size(theta, 1), 1);

for iter = 1:num_iters
  for i=1:size(theta,1)
    temp(i) = theta(i) - (alpha/m)*sum((X*theta-y).*X(:,i));
  end
  
  theta = temp;
  %J_history(iter) = computeCostMulti(X, y, theta);
  %-----------------------------------------------------------------
  J_history(iter) =(1/(2*m)*(X*theta-y)'*(X*theta-y));
  %-----------------------------------------------------------------
end
%---------------------------------------------------
fprintf('Theta = [%.2f %.2f %.2f]\n', theta);
figure;
plot(1:numel(J_history), J_history, '-b', 'LineWidth', 2);
xlabel('Number of iterations');
ylabel('Cost J');

fprintf('Program paused. Press enter to continue.\n');
pause;
fprintf('\n');

%Estimate the price of a 1650 sq-ft, 3 br house
FEET = 2104;
BED = 3; 

price = [1 (FEET-mu(1))/sigma(1) (BED-mu(2))/sigma(2)]*theta; 

fprintf(['Predicted price of a %0.0f sq-ft, %0.0f br house ' ...
         '(using normal equations):\n $%f\n'], [FEET, BED, price]);

fprintf('Program paused. Press enter to continue.\n');
pause;
fprintf('\n');

%%%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%%%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
%%%+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

fprintf('Solving with normal equations...\n');
%% Load Data
data2 = csvread('ex1data2.txt');
X2 = data2(:, 1:2);
y2 = data2(:, 3);
m2 = length(y2);

% Add intercept term to X
X2 = [ones(m, 1) X2];

% Calculate the parameters from the normal equation
theta2 = zeros(size(X2, 2), 1);
theta2 = pinv(X2'*X2)*X2'*y2;
fprintf('Theta2 = [%.2f %.2f %.2f]\n', theta2);
%No need to feature scaling
price2 = [1 FEET BED]*theta2;

fprintf(['Predicted price of a %0.0f sq-ft, %0.0f br house ' ...
         '(using normal equations):\n $%f\n'], [FEET, BED, price2]);

fprintf('WELL DONE\n');         
pause;
fprintf('\n');
