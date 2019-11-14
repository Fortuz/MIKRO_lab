import numpy as np
import matplotlib.pyplot as plt
# -------- USED FUNCTIONS DEFINITIONS -------------------------
def plotData(X,Y):
    pos=[]
    neg=[]

    for i in range(0,Y.size):
        if Y[i] ==0:
            neg.append(X[i,:])
        elif Y[i] ==1:
            pos.append(X[i,:])

    neg = np.array(neg)
    pos = np.array(pos)

    plt.scatter(neg[:,0],neg[:,1],marker='x',c="r", label="Not admitted")
    plt.scatter(pos[:,0],pos[:,1],marker='o',c="g", label="Admitted")
    plt.title("Training data")
    plt.xlabel("Exam 1 score")
    plt.ylabel("Exam 2 score")
    plt.legend(loc='lower left')
    plt.show()

    return pos, neg

def sigmoid(z):
    # calculates the sigmoid function value
    return 1/(1 + np.exp(-z))

def costFunction(w,X,Y):
    prediction = np.array(sigmoid(X@w))
    error = ((-Y) * np.log(prediction)) - ((1-Y)*(np.log(1-prediction)))
    C = (1/m) * np.sum(error)

    grad = (X.transpose())@(prediction-Y)/m

    return C, grad

def featureNormalization(X):
    mean = np.mean(X,axis=0)
    std = np.std(X, axis=0,ddof=1)
    X_temp = X.copy()

    if std[0] == 0:
        X_temp=np.delete(X_temp,0,1)
        X_norm = (X_temp - mean[1:3]) / std[1:3]
        X_norm=np.column_stack((np.ones((m,1)),X_norm))
    else:
        X_norm = (X_temp - mean) / std

    return X_norm,mean,std

def gradientDescent(X,Y,w,alpha,num_iters=400):
    C_history = []

    for i in range(num_iters):
        C, grad = costFunction(w,X,Y)
        w = w - (alpha*grad)
        C_history.append(C)

    return w, np.array(C_history)

def predictionMaking(X):
    X = (X-mean[1:3])/std[1:3]
    X = np.append(np.ones((1)),X)
    return sigmoid(X@w)

def calculateAccuracy(w,X,Y):
    predictions= (sigmoid(X@w)>0.5)
    percentage=(sum(predictions==Y)/m)*100
    return percentage

# ------- END OF THE USED FUNCTIONS DEFINITIONS ---------------
#--------------------------------------------------------------
#------------------ GETTING THE DATA --------------------------
file=open('Lab3data.txt')
data= file.readlines()
file.close()

X=[]
TEMP=[]
Y=[]

for line in data:
    a,b,c=line.split(',')
    X.append(float(a))
    TEMP.append(float(b))
    Y.append(float(c))

X=np.array(X)
TEMP=np.array(TEMP)
Y=np.array(Y)
X=np.column_stack((X,TEMP))
del TEMP
Y=Y.reshape((Y.size,1))

'''
print('X értékei:\n', X)
print('Y értékei:\n', Y)
'''
#----------------- Plot the data ---------------------
pos,neg=plotData(X,Y)
#----------------- Reshape data + initialization -----
m,n = X.shape           # m adatok száma / n feature-k száma
X=np.column_stack((np.ones((m,1)),X))       # bias
#----------------- teszt nulla és nem nulla súlyokkal
initial_w = np.zeros(((n+1),1))
C,grad = costFunction(initial_w,X,Y)

print('''Cost and Gradient  at initial weights (zeros):
Expected cost (approx.): 0.693
Computed:''',C)
print('''Expected gradient(approx.):
 [-0.1  -12.0092    -11.2628]
Computed:\n''',grad.transpose())

test_w = np.array([[-24], [0.2], [0.2]])
C, grad = costFunction(test_w,X,Y)

print('\nTest weights:',test_w.transpose())
print('''Cost and Gradient  at test weights:
Expected cost (approx.): 0.218
Computed:''',C)
print('''Expected gradient(approx.):
 [0.043     2.566   2.647]
Computed:\n''',grad.transpose())
print('\n')
#---------------- featrure normalization on X for the gradient descent alg. -------------------------------
X,mean,std=featureNormalization(X)                   # feature normalization on X
#---------------- Gradient descent alg. w. diffenrent learning rates---------------------------------------
w = np.array([[0],[0],[0]])
w, C_history = gradientDescent(X,Y,w,0.01)
plt.plot(range(C_history.size), C_history, label= "learning r.:0.01 / iters.: 400")

w = np.array([[0],[0],[0]])
w, C_history = gradientDescent(X,Y,w,0.1)
plt.plot(range(C_history.size), C_history, label= "learning r.:0.1 / iters.: 400")

w = np.array([[0],[0],[0]])
w, C_history = gradientDescent(X,Y,w,1)
plt.plot(range(C_history.size), C_history, label= "learning r.:1 / iters.: 400")
plt.title("Effect of the different constants on the cost function")
plt.xlabel("Number of iterations")
plt.ylabel("Cost function value")
plt.legend()
plt.show()

print('''The cost function at found weights by the gradient descent alg.:
Expected (approx): 0.203
Computed: ''', C_history[-1])
print('''Weights expected (approx.):
[1.659 3.867 3.603]
Weights computed:\n''', w.transpose())
#---------------------- Plot the descision boundary --------------------------
pos=(pos-mean[1:3])/std[1:3]
neg=(neg-mean[1:3])/std[1:3]

plt.scatter(pos[:,0],pos[:,1],c="g", marker="o",label="Admitted")
plt.scatter(neg[:,0],neg[:,1],c="r",marker="x",label="Not admitted")
x_value = np.array([np.min(X[:,1]),np.max(X[:1])])
y_value = -(w[0]+w[1]*x_value)/w[2]
plt.plot(x_value,y_value,"k")
plt.title("Decision boundary and the training data")
plt.xlabel("Exam 1 score")
plt.ylabel("Exam 2 score")
plt.legend(loc=0)
plt.show()
#-------------------- Making some predictions --------------------------------------
prediction=predictionMaking(np.array([45,85]))
print('''Expected result of the prediction with [45 , 85]:
0.776291
Calculated:\n''',prediction)
#--------------------- Calculating the accuracy --------------------------------------
print(calculateAccuracy(w,X,Y), '% accuracy (89 % expected)')



