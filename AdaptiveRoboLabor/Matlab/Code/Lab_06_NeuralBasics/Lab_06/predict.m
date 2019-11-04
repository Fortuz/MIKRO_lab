function p = predict(w1, w2, X)
%PREDICT Predict the label of an input given a trained neural network
% Useful values
m = size(X, 1);
num_labels = size(w2, 1);

p = zeros(size(X, 1), 1);

a1 = [ones(m, 1) X];
z2 = a1*w1';
a2 = [ones(size(z2, 1), 1) sigmoid(z2)];
z3 = a2*w2';
a3 = sigmoid(z3);

[p_max, p] = max(a3, [], 2);

end
