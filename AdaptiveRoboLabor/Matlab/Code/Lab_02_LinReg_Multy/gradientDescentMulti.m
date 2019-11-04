function [w, C_history] = gradientDescentMulti(X, Y, w, lr, epochs)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
% Initialize some useful values
m = length(Y);
C_history = zeros(epochs, 1);
temp = zeros(size(w, 1), 1);

for iter = 1:epochs
  for i=1:size(w,1)
    temp(i) = w(i) - (lr/m)*sum((X*w-Y).*X(:,i));
  end
  
  w = temp;  
    C_history(iter) = computeCostMulti(X, Y, w);

end

end
