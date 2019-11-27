function [C grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification

% Reshape nn_params back into the parameters weight1 and weight2, the weight matrices
% for our 2 layer neural network
w1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

w2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
C = 0;
w1_grad = zeros(size(w1));
w2_grad = zeros(size(w2));

A1 = [ones(size(X,1),1) X];
S2 = A1*w1';
A2 = sigmoid(S2);
A2_0 = [ones(size(A2,1),1) A2];
S3 = A2_0*w2';
A3 = sigmoid(S3);

HX = A3;

% recode y to Y // TRICKY => ONE HOT ENCODING
I = eye(num_labels);
Y = zeros(m, num_labels);

for i=1:m
  Y(i, :)= I(y(i), :);
end

penalty = (lambda /(2*m))*(sum(sum(w1(:, 2:end).^2, 2))+sum(sum(w2(:, 2:end).^2, 2)));

C = (1/m) * sum(sum((-Y).*log(HX)-((1-Y).*log(1-HX))))+penalty;

% calculate sigmas //DELTAS
sigma3 = (A3-Y);
sigma2 = (sigma3*w2).*sigmoidGradient([ones(size(S2, 1), 1) S2]);
sigma2 = sigma2(:, 2:end);

% accumulate gradients
delta_1 = (sigma2'*A1);
delta_2 = (sigma3'*A2_0);

% calculate regularized gradient
p1 = (lambda/m)*[zeros(size(w1, 1), 1) w1(:, 2:end)];
p2 = (lambda/m)*[zeros(size(w2, 1), 1) w2(:, 2:end)];
w1_grad = delta_1./m + p1;
w2_grad = delta_2./m + p2;

% Unroll gradients
grad = [w1_grad(:) ; w2_grad(:)];

end
