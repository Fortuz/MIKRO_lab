function [C, grad] = lrCostFunction(w, X, y, lambda)
%Compute cost and gradient for logistic regression with 
%regularization
%% Vectorized form

m = length(y); % number of training examples 
C = 0;
grad = zeros(size(w));

h = sigmoid(X*w);
% calculate penalty
% excluded the first weight value
w_reg = [0 ; w(2:size(w), :)];
p = lambda*(w_reg'*w_reg)/(2*m);
C = ((-y)'*log(h) - (1-y)'*log(1-h))/m + p;

% calculate grads
grad = (X'*(h - y)+lambda*w_reg)/m;
end
