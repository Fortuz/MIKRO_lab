import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
#--------------------- Definitions of used functions --------
def linearRegCostFunction(X,y,w,Lambda):
    m = y.shape[0]

    C = 0
    grad = np.zeros(w.shape)

    w_0 = w
    w_0[0] = 0
    penalty = (Lambda/(2*m))*np.sum(w_0**2)
    C = (1/(2*m))*np.sum((X @ w)-y) + penalty

    grad = (1/m)* np.sum(((X @ w)-y)*X) + ((Lambda/m) @ w_0.T)


    return C, grad







#---------------------- End of definitions ---------------------
#---------------------- Loading data ---------------------------
data = loadmat("Lab8data.mat")
#print(data)
X = data["X"]
Y = data ["y"]
X_test = ["Xtest"]
Y_test = ["ytest"]
X_val = ["Xval"]
Y_val = ["yval"]
del data
m = X.shape[0]
print('Shape of X:', X.shape)
print('Shape of Y:', Y.shape)
#---------------------- plotting training data ----------------------
plt.plot(X,Y,'x')
plt.title('Training data')
plt.xlabel('Change in water level (X)')
plt.ylabel('Water floeing out of the dam (Y)')
plt.show()
#--------------------- Regularized Linear regression Cost -----------
w = np.array([1,1])
C, grad = linearRegCostFunction(np.column_stack((np.ones((m,1)),X)),Y,w,1)

print(C, grad)




