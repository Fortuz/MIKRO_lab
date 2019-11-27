function X_rec = recoverData(Z, U, K)
%Recovers an approximation the 
%original data that has been reduced to K dimensions. It returns the
%approximate reconstruction in X_rec.

% You need to return the following variables correctly.
X_rec = zeros(size(Z, 1), size(U, 1));

  X_rec = Z*U(:,1:K)';
end
