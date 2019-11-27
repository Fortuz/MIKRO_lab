function [X_norm, mu, sigma] = featureNormalize(X)
%FEATURENORMALIZE Normalizes the features in X 
%{
bsxfun  Binary Singleton Expansion Function
    C = bsxfun(FUNC,A,B) applies the element-by-element binary operation
    specified by the function handle FUNC to arrays A and B, with implicit
    expansion enabled.
%}
mu = mean(X);
X_norm = bsxfun(@minus, X, mu);

sigma = std(X_norm);
X_norm = bsxfun(@rdivide, X_norm, sigma);

end
