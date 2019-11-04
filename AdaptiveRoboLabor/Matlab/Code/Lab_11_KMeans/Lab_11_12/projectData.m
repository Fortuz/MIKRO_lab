function Z = projectData(X, U, K)
%Computes the projection of the normalized inputs X into the reduced 
%dimensional space spanned by the first K columns of U. It returns 
%the projected examples in Z.

Z = zeros(size(X, 1), K);

Ureduce=U(:, 1:K);
Z = X*Ureduce;
end
