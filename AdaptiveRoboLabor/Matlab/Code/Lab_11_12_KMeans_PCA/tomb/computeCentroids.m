function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returns the new centroids by computing the means of the 
%data points assigned to each centroid.

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);

for k = 1:K
  centroid = zeros(1, n);
  Ck = 0;
  for i = 1:m
    if idx(i) == k
      centroid = centroid + X(i, :);
      Ck = Ck + 1;
    end    
  end
  centroids(k,:) = centroid.*(1/Ck);
end

end

