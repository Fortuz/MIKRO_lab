function p = predict(w, X)
m=size(X, 1);
p = zeros(m, 1);

temp= sigmoid(X*w);
for i=1:m
    if temp(i)>=0.5
        temp(i)=1;
    else
        temp(i)=0;
    end
end
p = temp;
end