clear; close all; clc;

% Load data
data = load('ex2data1.txt');

X = data(:, [1, 2]);
Y = data(:, 3);      

% Print out some data points
fprintf('First 10 examples from the dataset: \n');
fprintf(' x = [%.0f %.0f], y = %.0f \n', [X(1:10,:) Y(1:10,:)]');

fprintf(['Plotting data with + indicating (y = 1) examples and o ' ...
         'indicating (y = 0) examples.\n']);
     
plotData(X, Y);
hold on;
xlabel('Exam 1 score');
ylabel('Exam 2 score');
legend('Admitted', 'Not admitted');
hold off;

% Cost function
[m, n]=size(X);

%Bias
X = [ones(m, 1) X];

% Init W
init_w = zeros(n+1, 1);

[C, grad] = costFunction(init_w, X, Y);

fprintf('Cost: %f\n', C);
fprintf('Grad: %f\n', grad);

% Optimalizálás
options = optimset('GradObj', 'on', 'MaxIter', 400);

[w, C] = fminunc(@(t)(costFunction(t, X, Y)), init_w, options);

plotDecisionBoundary(w, X, Y);
hold on;
xlabel('Exam 1 score');
ylabel('Exam 2 score');
legend('Admitted', 'Not admitted');
hold off;

% Predict
prob = sigmoid([1 45 85]*w);
fprintf('Probability: %f\n', prob);

p = predict(w, X);
fprintf('Train accuracy: %f\n', mean(double(p==Y))*100);


