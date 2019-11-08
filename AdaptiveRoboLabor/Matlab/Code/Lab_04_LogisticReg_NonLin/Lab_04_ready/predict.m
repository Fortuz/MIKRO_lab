function p = predict(w, X)
%PREDICT Predict whether the label is 0 or 1 using learned logistic 
%regression parameters weights
%   p = PREDICT(w, X) computes the predictions for X using a 
%   threshold at 0.5 (i.e., if sigmoid(Xw) >= 0.5, predict 1)

m = size(X, 1); % Number of training examples
p = zeros(m, 1);

temp = sigmoid(X*w);
for i=1:m
  if temp(i)>=0.5
    temp(i) = 1;
  else
    temp(i) = 0;
  end
end
p = temp;

end