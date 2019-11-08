function [C, grad] = costFunctionReg(w, X, Y, lambda)
%COSTFUNCTIONREG Compute cost and gradient 
%for logistic regression with regularization

m = length(Y); % number of training examples
C = 0;
grad = zeros(size(w));

% calculate cost function
h = sigmoid(X*w);
% calculate penalty
% excluded the first w value
w1 = [0 ; w(2:size(w), :)];
p = lambda*(w1'*w1)/(2*m);
% Alternative: 
%p = (lambda / (2*m))*sum(w_reg.^2);

C = ((-Y)'*log(h) - (1-Y)'*log(1-h))/m + p;
% Alternative: 
% C = ((1/m).*sum(((-1.*Y).*log(hx)) - ((1.-Y).*log(1.-hx))))+p;

% calculate grads
grad = (X'*(h - Y)+lambda*w1)/m;

end