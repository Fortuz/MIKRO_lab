import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.optimize import fmin_tnc
#--------------------- Definitions of used functions --------
def linearRegCostFunction(w,*args):
    X,y,Lambda = args
    m = y.shape[0]
    print(m)
    y=y.reshape(m,1)

    w_0 = w.copy()
    w_0[0] = 0
    penalty = (Lambda/(2*m))*np.sum(w_0**2)
    C = (1/(2*m)) * (np.sum(((X @ w)-y)**2)) + penalty

    return C

def linRegGrad(w,*args):
    X,y,Lambda = args

    m = y.shape[0]
    y=y.reshape(m,1)

    w_0 = w.copy()
    w_0[0] = 0

    w = w.reshape(2,1)

    grad = (1 / m) * np.sum((((X @ w) - y) * X), 0) + ((Lambda / m) * w_0.T)

    return grad

def trainLinearReg(X,y,Lambda):
    args = (X,y.flatten(),Lambda)
    init_w = np.ones((X.shape[1],1))
    result1 = fmin_tnc(linearRegCostFunction,init_w.flatten(),fprime=linRegGrad, args=args, disp=0)

    return result1[0]

def learningCurve(X,Y,X_val,Y_val,Lambda):
    m = X.shape[0]

    error_train = np.zeros((m,1))
    error_val = np.zeros((m,1))

    for i in range (m):
        w = trainLinearReg(X[0:i,:],Y[0:i],Lambda)




    return error_train, error_val






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
#--------------------- Regularized Linear regression Cost and gradients -----------
w = np.array([[1],[1]])
C = linearRegCostFunction(w,np.column_stack((np.ones((m,1)),X)),Y,1)
grad = linRegGrad(w,np.column_stack((np.ones((m,1)),X)),Y,1)
print('''Cost at weight: 
[[1]
[1]]
Expected: 303.9921
Computed:''',C, '''
Gradient expected: [-15.303015 598.2507]
Gradient computed:''', grad)
#----------------------------- Train Linear Regression ----------------------
Lambda = 0

w = trainLinearReg(np.column_stack((np.ones((m,1)),X)),Y,Lambda)
print('Weights with the optimization:',w)

plt.plot(X,Y,'x',label='Training data')
plt.plot(X,np.column_stack((np.ones((m,1)),X)) @ w,'--', label='Trained LR with lambda 0')
plt.xlabel('Change in water level (X)')
plt.ylabel('water flowing out of the dam (Y)')
plt.legend()
plt.show()
# ---------------------------- Train Curve for Linear Regression ---------------
Lambda = 0
asd = learningCurve(X,Y,X_val,Y_val,Lambda)