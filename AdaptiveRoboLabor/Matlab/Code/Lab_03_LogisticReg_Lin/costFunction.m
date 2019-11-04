function [C, grad] = costFunction(w, X, Y)
%COSTFUNCTION Compute cost and gradient for logistic regression
% Initialize some useful values
m = length(Y); % number of training examples 
C = 0;
grad = zeros(size(w));

C = (1/m) * sum((-Y).*(log(sigmoid(X*w))) - (1-Y).*(log(1-sigmoid(X*w))));

for i=1:size(w)
  grad(i) = (1/m) * sum((sigmoid(X*w)-Y).*X(:,i));
end 
end
