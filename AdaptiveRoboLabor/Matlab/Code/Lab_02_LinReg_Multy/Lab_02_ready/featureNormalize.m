function [X_norm, avg, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%   FEATURENORMALIZE(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.

X_norm = X;
avg = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

for i=1:size(avg,2)
    avg(1,i) = mean(X(:,i)); 
    sigma(1,i) = std(X(:,i));
    X_norm(:,i) = (X(:,i)-avg(1,i))/sigma(1,i);
end

end