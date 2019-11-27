
%% Machine Learning
% Lab 5: Multi class classification - One VS ALL
% --- Handwritten Digits ---
%{
For this exercise, you will use logistic regression to
recognize handwritten digits (from 0 to 9). Automated handwritten digit
recognition is widely used today - from recognizing zip codes (postal codes)
on mail envelopes to recognizing amounts written on bank checks.
%}

%% Initialization
clear ; close all; clc

%% Setup the parameters you will use for this part of the exercise
input_layer_size  = 400;  % 20x20 Input Images of Digits
num_labels = 10;          % 10 labels, from 1 to 10
% (note that we have mapped "0" to label 10

%% Loading and Visualizing Data
% Load Training Data
fprintf('Loading and Visualizing Data ...\n')
load('ex3data1.mat'); % training data stored in arrays X, y
m = size(X, 1);

% Randomly select 100 data points to display
rand_indices = randperm(m);
sel = X(rand_indices(1:100), :);

displayData(sel);

fprintf('Program paused. Press enter to continue.\n');
pause;

%% Vectorize Logistic Regression

% Test case for lrCostFunction
fprintf('\nTesting lrCostFunction() with regularization');

w_t = [-2; -1; 1; 2];
X_t = [ones(5,1) reshape(1:15,5,3)/10];
Y_t = ([1;0;1;0;1] >= 0.5);
lambda_t = 3;
[C grad] = lrCostFunction(w_t, X_t, Y_t, lambda_t);

fprintf('\nCost: %f\n', C);
fprintf('Expected cost: 2.534819\n');
fprintf('Gradients:\n');
fprintf(' %f \n', grad);
fprintf('Expected gradients:\n');
fprintf(' 0.146561\n -0.548558\n 0.724722\n 1.398003\n');

fprintf('Program paused. Press enter to continue.\n');
pause;

%% One-vs-All Training 
fprintf('\nTraining One-vs-All Logistic Regression...\n');

lambda = 0.1;
[all_w] = oneVsAll(X, y, num_labels, lambda);

fprintf('Program paused. Press enter to continue.\n');
pause;

%% Predict for One-Vs-All 

pred = predictOneVsAll(all_w, X);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);


