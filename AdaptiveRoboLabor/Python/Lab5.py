import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import loadmat

# -------- USED FUNCTIONS DEFINITIONS -------------------------
def sigmoid(z):
    return 1/(1+np.exp(-z))

def lrCostFunction(w,X,Y,Lambda):
    m = len(Y)
    predictions = sigmoid(X@w)
    error = (-Y * np.log(predictions)) - ((1-Y) * np.log(1-predictions))
    C = 1/m * np.sum(error)
    regCost = C + Lambda/(2*m) * np.sum(w[1:]**2)

    j_0 = 1/m * (X.transpose() @ (predictions-Y))[0]
    j_1 = 1/m * (X.transpose() @ (predictions-Y))[1:] + (Lambda/m)*w[1:]

    grad = np.vstack((j_0[:,np.newaxis],j_1))

    return regCost, grad

def gradientDescent(X,Y,w,alpha,num_iters,Lambda):
    C_history = []

    for i in range(num_iters):
        C, grad =lrCostFunction(w,X,Y,Lambda)
        w = w - (alpha * grad)
        C_history.append(C)

    return w, np.array(C_history)

def oneVsAll(X, Y, num_labels, Lambda):
    m, n = X.shape[0],X.shape[1]
    w_init = np.zeros((n + 1, 1))
    w_all = []
    C_all = []

    X = np.hstack((np.ones((m, 1)), X))

    for i in range(1,num_labels + 1):
        w, C_history = gradientDescent(X, np.where(Y == i, 1, 0), w_init, 1, 300, Lambda)
        w_all.extend(w)
        C_all.extend(C_history)

    return np.array(w_all).reshape(num_labels, n + 1), C_all

def predictionOneVsAll(w_all,X):
    m = X.shape[0]
    X = np.hstack((np.ones((m,1)),X))

    predictions = X @ w_all.T
    return np.argmax(predictions,axis=1)+1



# ------- END OF THE USED FUNCTIONS DEFINITIONS ---------------
#--------------------------------------------------------------
#----------- GETTING THE DATA  and visualization --------------
mat = loadmat("Lab5data.mat")
X = mat["X"]
Y = mat["y"]
m = X.shape[0]
# ide nem árthat kiiratni amm, hogy lássák mi a felosztás és mi alapján rendezzük később
print('''Shape of the dataset in order X and Y:
''',X.shape,'\n',Y.shape,'\n')

print("Now showing some random data from the dataset ...")
fig, axis = plt.subplots(10,10,figsize = (8,8))
for i in range(10):
    for j in range(10):
        axis[i,j].imshow(X[np.random.randint(0,m+1),:].reshape(20,20,order="F"),cmap="hot")
        axis[i,j].axis("off")
plt.show()
#-------------- gradient ------------------------------------
w_t = np.array([-2,-1,1,2]).reshape(4,1)
X_t = np.array([np.linspace(0.1,1.5,15)]).reshape(3,5).T
X_t = np.hstack((np.ones((5,1)),X_t))
Y_t = np.array([1,0,1,0,1]).reshape(5,1)
C,grad = lrCostFunction(w_t, X_t, Y_t, 3)
print('\nTest weight:\n',w_t,'''
Testing lrCostFunction() with regularization ... 
Cost function value:''', C, ' Expected: 2.534819')
print('''\nExpected gradients:
 [[0.146561]
 [-0.548558]
 [0.724722]
 [1.398003]]
Computed:\n''',grad)

w_all, C_all = oneVsAll(X,Y,10,0.1)
plt.plot(C_all[0:300])
plt.title("Cost function using Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("C_all value")
plt.show()
#-----------------------
pred = predictionOneVsAll(w_all, X)
acc = sum(pred[:,np.newaxis]==Y)[0]/5000*100
print("Training Set Accuracy:", acc,"%")




