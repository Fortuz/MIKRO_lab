function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])

K = size(centroids, 1);
idx=zeros(size(X,1),1);

for i = 1:size(X,1)
    distance = Inf;
    for k = 1:K
        temp2= X(i,:)-centroids(k,:);
        if (temp2*temp2') < distance
            distance = (temp2*temp2');
            temp1 = k;
        end
    end
    idx(i)=temp1;
end

