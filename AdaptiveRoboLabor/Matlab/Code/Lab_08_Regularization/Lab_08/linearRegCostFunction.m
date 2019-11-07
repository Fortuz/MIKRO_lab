function [C, grad] = linearRegCostFunction(X, y, w, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
C = 0;
grad = zeros(size(w));

w_0 = w;
w_0(1) = 0;
penalty = (lambda / (2*m))*sum(w_0.^2);
C = (1/(2*m))*(sum(((X*w)-y).^2))+penalty;

grad = (1/m)*sum(((X*w)-y).*X)+((lambda/m)*w_0');

grad = grad(:);

end
