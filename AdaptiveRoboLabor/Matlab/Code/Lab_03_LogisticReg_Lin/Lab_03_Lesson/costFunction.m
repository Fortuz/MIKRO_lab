function [C, grad] = costFunction(w, X, Y)
m=length(Y);
C=0;
grad=zeros(size(w));
h=sigmoid(X*w);

C = (1/m)*sum((-Y).*(log(h))-(1-Y).*(log(1-h)));

for i=1:size(w)
    grad(i) = (1/m)*sum((h-Y).*X(:, i));
end
end