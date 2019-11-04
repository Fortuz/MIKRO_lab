function out = mapFeature(X1, X2)
% MAPFEATURE Feature mapping function to polynomial features

degree=3; % change it to 6 for example
out = ones(size(X1(:,1))); % first column ones -> bias
for i = 1:degree
    for j = 0:i
        out(:, end+1) = (X1.^(i-j)).*(X2.^j);
    end
end

end