function [all_w] = oneVsAll(X, y, num_labels, lambda)
%ONEVSALL trains multiple logistic regression classifiers and returns all
%the classifiers in a matrix all_w, where the i-th row of all_w 
%corresponds to the classifier for label i
%%
% Some useful variables
m = size(X, 1); % examples
n = size(X, 2); % features
all_w = zeros(num_labels, n + 1); 



end