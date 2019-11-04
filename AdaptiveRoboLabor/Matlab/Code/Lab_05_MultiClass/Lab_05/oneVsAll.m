function [all_w] = oneVsAll(X, y, num_labels, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_w, where the i-th row of all_w 
%corresponds to the classifier for label i
%%
% Some useful variables
m = size(X, 1); % examples
n = size(X, 2); % features
all_w = zeros(num_labels, n + 1); 

% Add ones to the X data matrix
X = [ones(m, 1) X];

for c = 1:num_labels
  init_w = zeros(n+1, 1);
  options = optimset('GradObj', 'on', 'MaxIter', 50);
  [w] = fmincg(@(t)(lrCostFunction(t, X, (y==c), lambda)), init_w, options);
  all_w(c, :) = w';
end

end