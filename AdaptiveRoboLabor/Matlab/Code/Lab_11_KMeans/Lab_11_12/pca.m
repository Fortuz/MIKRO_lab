function [U, S] = pca(X)
%PCA Run principal component analysis on the dataset X
%   Computes eigenvectors of the covariance matrix of X
%   Returns the eigenvectors U, the eigenvalues (on diagonal) in S

[m, n] = size(X);

U = zeros(n);
S = zeros(n);

Sigma = (1/m).*(X'*X);
[U, S, V] = svd(Sigma);
end
