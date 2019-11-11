function C = computeCostMulti(X, Y, w)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables

% Initialize some useful values

m = length(Y);
C = 0;

C = (1/(2*m) * (X*w-Y)'*(X*w-Y));
end