function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

maxError = Inf;

% It would be nice if this didn't do function optimization by exhaustive search :-/
for currC = [0.01 0.03 0.1 0.3 1 3 10 30]
  for currSigma = [0.01 0.03 0.1 0.3 1 3 10 30]
    model = svmTrain(X, y, currC, @(x1, x2) gaussianKernel(x1, x2, currSigma)); 

    predictions = svmPredict(model, Xval);
    predictionError = mean(double(predictions ~= yval));

    if predictionError < maxError
      maxError = predictionError;
      C = currC;
      sigma = currSigma;
    end
  end
end

end
