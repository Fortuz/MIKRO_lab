import numpy as np
import matplotlib.pyplot as plt
# -------- USED FUNCTIONS DEFINITIONS -------------------------
def featureNormalize(X):
    X_norm=X.copy()
    avg = np.zeros((1,np.size(X,1)))
    sigma = np.zeros((1,np.size(X,1)))

    for i in range(0,np.size(X,1)):
        avg[0,i] = np.mean(X[:,i],axis=0)
        sigma[0,i] = np.std(X[:,i],axis=0,ddof=1)   # ddof=1 mert tapasztalati szórás kell

    for i in range(0,np.size(X,1)):
        for j in range(0,np.size(X,0)):
            X_norm[j,i] = (X[j,i]-avg[0,i])/sigma[0,i]

    return X_norm, avg, sigma

def computeCostMulti(X,Y,w):
    C=0
    C=(1/(2*m))*((X@w-Y).T)@(X@w-Y)
    return C

def gradientDescentMulti(X,Y,w,lr,epochs):
    C_history = np.zeros((epochs,1))
    temp= np.zeros((np.size(w,0),1))

    for iteration in range(0,epochs):
       for i in range(0,np.size(w,0)):
           temp[i] = w[i]-(lr/m)*np.sum((X@w-Y)*(X[:,i].reshape(m,1)), axis=None)
       w=temp
       C_history[iteration]=computeCostMulti(X,Y,w)

    return w, C_history

# ------- END OF THE USED FUNCTIONS DEFINITIONS ---------------
#--------------------------------------------------------------
#------------------ GETTING THE DATA --------------------------
file=open("Lab2data.txt")                   # megnyitjuk a filet csak olvasásra/text formátumban, fontos hogy a mappában legyen
data=file.readlines()
file.close()

X=[]
TEMP=[]
Y=[]

for line in data:
    a,b,c = line.split(',')
    X.append(float(a))
    TEMP.append(float(b))
    Y.append(float(c))

X=np.array(X)
TEMP=np.array(TEMP)
X = np.column_stack((X,TEMP))
Y=np.array(Y)
m=Y.size
Y=Y.reshape(m,1)
del TEMP
'''
print('X értékei:\n', X)
print('Y értékei:\n', Y)
print('Adatok száma: ', m)
'''
print('Normalizeing X vector ...')
X_norm,avg,sigma = featureNormalize(X)
X_norm=np.column_stack((np.ones(m),X_norm))

print('Running gradient descent ...')
lr = 0.01
epochs = 400
w=np.zeros((3,1))
w,C_history= gradientDescentMulti(X_norm,Y,w,lr,epochs)
print('Weights computed from gradient descent:\n', w)

plt.plot(range(0,epochs),C_history)
plt.title("Gradient descent algorithms effect through the iterations",pad= 20)
plt.xlabel("Iterations")
plt.ylabel("Cost function value")
plt.show()

FEET = 1650
BED = 3
price = (np.array([1, ((FEET-avg[0,0])/sigma[0,0]), (BED-avg[0,1])/sigma[0,1]]))@w
print('''Prediction for a 1650 sq-ft / 3 bedroom house:
(predicted price should be $293081.464335)
''',price)


