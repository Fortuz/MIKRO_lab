function p = predictOneVsAll(all_w, X)
%PREDICT Predict the label for a trained one-vs-all classifier. The labels 
%are in the range 1..K, where K = size(all_w, 1). 

m = size(X, 1);
num_labels = size(all_w, 1);

p = zeros(size(X, 1), 1);
% Add ones to the X data matrix
X = [ones(m, 1) X];

%%



end