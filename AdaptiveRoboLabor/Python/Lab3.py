import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco
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

    plt.plot(neg[:,0],neg[:,1],'x')
    plt.plot(pos[:,0],pos[:,1],'o')
    plt.legend(['Not admitted','Admitted'])
    plt.show()

    return pos, neg

def sigmoid(z):
    g = np.zeros(z.size)
    g = 1/(1 + np.exp(-z))

    return g

def costFunction(w,X,Y):
    m = Y.size
    C = 0

    C = (1/m) * np.sum((-Y) * (np.log(sigmoid(X@w))) - (1-Y) * (np.log(sigmoid(X@w))))

    return C

def gradFunction(w,X,Y):
    grad = np.zeros(w.size)

    for i in range(0,w.size):
        grad[i] = (1/m) * np.sum((np.reshape(sigmoid(X@w),(m,1))-Y) * np.reshape((X[:,i]),(m,1)))

    return grad


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
plotData(X,Y)
#----------------- Reshape data + initialization -----
m,n = X.shape           # m adatok száma / n feature-k száma

X=np.column_stack((np.ones((m,1)),X))       # bias
#----------------- teszt nulla és nem nulla súlyokkal
initial_w = np.zeros((n+1))
C = costFunction(initial_w,X,Y)
grad = gradFunction(initial_w,X,Y)

print('''Cost and Gradient  at initial weights (zeros):
Expected cost (approx.): 0.693
Computed:''',C)
print('''Expected gradient(approx.):
 [-0.1  -12.0092    -11.2628]
Computed:\n''',grad)

test_w = np.array([-24, 0.2, 0.2])
C = costFunction(test_w,X,Y)
grad = gradFunction(test_w,X,Y)
print('Test weights:',test_w)
print('''Cost and Gradient  at test weights:
Expected cost (approx.): 0.218
Computed:''',C)
print('''Expected gradient(approx.):
 [0.043     2.566   2.647]
Computed:\n''',grad)
print('\n')
#----------------
asd = sco.fmin_bfgs(f=costFunction, x0=initial_w, args=(X,Y), disp=True, maxiter=400)
print('\n')
print(asd)