function p = predictOneVsAll(all_w, X)
%PREDICT Predict the label for a trained one-vs-all classifier. The labels 
%are in the range 1..K, where K = size(all_w, 1). 

m = size(X, 1);
num_labels = size(all_w, 1);

p = zeros(size(X, 1), 1);
% Add ones to the X data matrix
X = [ones(m, 1) X];

%%

ps = sigmoid(X*all_w');
[p_max, i_max]=max(ps, [], 2); %max value, max value position
%Max value position corresponds to the actual number 
% 10 column - 10 class, if the max value position refers to 
% the 10th colum than thats your guess
p = i_max;

end