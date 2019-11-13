import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------------
#--------------------------- Important functions -----------------------------------
def plotData(X,Y):
    pos = []
    neg = []

    for i in range(0,Y.size):
        if Y[i]==1:
            pos.append(X[i,:])
        elif Y[i]==0:
            neg.append(X[i,:])

    pos = np.array(pos)
    neg = np.array(neg)

    plt.scatter(pos[:, 0], pos[:, 1], c="g", marker="o", label="OK")
    plt.scatter(neg[:, 0], neg[:, 1], c="r", marker="x", label="Not OK")
    plt.legend()
    plt.show()

    return pos,neg

def mapFeature(X1,X2,deg=6):

    out = np.ones((m,1))

    for i in range(1,deg+1):
        for j in range(i+1):
            terms = (X1**(i-j)*X2**j).reshape(m,1)
            out = np.column_stack((out,terms))

    return out

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def costFunctionReg(w,X,Y,Lambda=1):
    m = len(Y)

    pred = sigmoid(X@w)                             # prediction
    w1 = np.vstack((np.array([0]),w[1:,:]))         # exclude the first w value
    p = Lambda*(w1.transpose() @ w1)/(2*m)          # penalties

    C = (((-Y).transpose() @ np.log(pred)) - ((1-Y).transpose() @ np.log(1-pred)))/m + p

    grad = (X.transpose() @ (pred -Y) + Lambda*w1)/m

    return C,grad

def gradientDescent(X,Y,w,alpha,num_iters,Lambda):
    m = len(Y)
    C_history = []

    for i in range(num_iters):
        C, grad = costFunctionReg(w,X,Y,Lambda)
        w = w - (alpha*grad)
        C_history = np.append(C_history,C)

    return w, np.array(C_history)

def mapFeaturePlot(x1,x2,deg=6):
    out = np.ones(1)
    for i in range(1,deg+1):
        for j in range(i+1):
            terms= (x1**(i-j) * x2**j)
            out= np.hstack((out,terms))
    return out

def classificationPrediction(w,X):
    pred = (sigmoid(X @ w) > 0.5)
    return ((np.sum(pred==Y)/m)*100)




#--------------------------- Important functions END -------------------------------
file = open("Lab4data.txt")
data = file.readlines()
file.close()

X = []
TEMP = []
Y = []

for line in data:
    a,b,c = line.split(",")
    X.append(float(a))
    TEMP.append(float(b))
    Y.append(float(c))

X=np.array(X)
TEMP=np.array(TEMP)
Y=np.array(Y)
X=np.column_stack((X,TEMP))
m,n = X.shape
del TEMP
Y=Y.reshape(m,1)
#----------------------- Plot data --------------------------------
pos, neg = plotData(X,Y)
#------------------ add polinomial feature -------------------------
X=mapFeature(X[:,0],X[:,1])
init_w = np.zeros((X.shape[1],1))
C, grad =costFunctionReg(init_w,X,Y)
print('Cost at initial weight (zeros): ',C)
#---------------------- gradient descent ----------------------------
w, C_history = gradientDescent(X,Y,init_w,1,800,0.2)
print('\nRegularized weight:\n',w)
#---------------------- Plot C_history -------------------------------
plt.plot(C_history,label = "alpha = 1 / num_iters = 800 / Lambda=0.2")
plt.legend()
plt.show()
#---------------------- Plot decision --------------------------------
plt.scatter(pos[:, 0], pos[:, 1], c="g", marker="o", label="OK")
plt.scatter(neg[:, 0], neg[:, 1], c="r", marker="x", label="Not OK")

u_vals = np.linspace(-1,1.,50)
v_vals = np.linspace(-1,1.,50)
z=np.zeros((len(u_vals),len(v_vals)))

for i in range(len(u_vals)):
    for j in range(len(v_vals)):
        z[i,j] = mapFeaturePlot(u_vals[i],v_vals[j]) @ w

plt.contour(u_vals,v_vals,z.transpose(),0)
plt.xlabel("Exam 1 score")
plt.ylabel("Exam 2 score")
plt.legend(loc=0)
plt.show()
#---------------------- prediction accurecy ----------------------------
acc=classificationPrediction(w,X)
print('\nAccuracy of the classification:',acc, '%')
#---------------------- Lasso prediction (ha nem tetszik töröljük)-------
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty="l1", solver='liblinear')
clf.fit(X,Y.ravel())
wLasso=clf.coef_
wLasso=wLasso.reshape(28,1)
print("The regularized theta using lasso regression:\n",wLasso)

accLasso=classificationPrediction(wLasso,X)
print('\nAccuracy of the classification:', accLasso, '%')



