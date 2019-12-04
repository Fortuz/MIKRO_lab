import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

# -------- USED FUNCTIONS DEFINITIONS -------------------------
def computeCost(X,Y,w):
    m = Y.size
    C = np.sum((X@w - Y)**2, axis=None)/(2*m)
    return C

def gradientDescent(X,Y,w,learning_rate,num_iters):
    m = Y.size
    C_history = np.zeros((num_iters,1))

    for i in range(0,num_iters):
        #VIGÁZAT szimultán update!!!!!
        neww=np.zeros((2,1))
        neww[0] = w[0] - (learning_rate/m) * np.sum(X@w-Y, axis=None)
        neww[1] = w[1] - (learning_rate/m) * np.sum((X@w-Y)*(X[:,1].reshape(97,1)), axis=None)
        w=neww.copy()
        C_history[i] =computeCost(X,Y,w)

    return w, C_history
# ------- END OF THE USED FUNCTIONS DEFINITIONS ---------------
#--------------------------------------------------------------
#------------------ GETTING THE DATA --------------------------
file=open("Lab1data.txt")                   # megnyitjuk a filet csak olvasásra/text formátumban, fontos hogy a mappában legyen
data=file.readlines()
file.close()

X=[]
Y=[]
for line in data:                           # Az adatokat formázzuk, hogy X és Y
    a,b = line.split(',')
    X.append(float (a))
    Y.append(float(b))

X=np.array(X)
Y=np.array(Y)
m=Y.size
'''
print('X értékei:\n', X)                     #kiiratjuk X;Y; darabszámot
print('Y értékei: \n', Y)
print('Az adatok száma: ', m)
'''
#------------------- DATA VIZUALIZATION -------------------------
plt.plot(X,Y,'o', c= "g")                           # kiplottoljuk a kezdeti értékeket
plt.title("Training data")
plt.xlabel("Population of a city in 10 000s")
plt.ylabel("Profit in $10 000s ")
plt.show()
#-------------------- INITIALIZATION ----------------------------
X=np.column_stack((np.ones(m),X))           # hozzáfűzünk egy 1-esekből álló oszlopot
Y=Y.reshape(m,1)                           # oszlopvektort csinálunk az Y-ból is

w=np.zeros((2,1))                           # initial fitting parameter
epochs= 1500                                 # some gradient descent settings
learning_rate=0.01
#----------------- TEST with some data ----------------------------
C=computeCost(X,Y,np.array([[0],[0]]).reshape((2,1)))
print('''Testing the cost function (Error function):
\tWith weights w = [0;0]
\tExpected value (approx.) = 32.07
\tCost computed = ''',C)
C=computeCost(X,Y,np.array([[-1],[2]]))
print('''\n\tWith weights w = [-1;2]
\tExpected value (approx.) = 54.24
\tCost computed = ''',C)
#----------------- Gradient method -----------------------------
print('''\nGradient descent:
\tWeights expected (approx.): 
\t[-3.6303] [1.1664]''')
w,C_history=gradientDescent(X,Y,w,learning_rate,epochs)
print('\tWeights calculated:\n   ',w[0],w[1])

plt.plot(range(0, C_history.size), C_history)
plt.title("Gradient descent algorithms effect through the iterations")
plt.xlabel("Iteration")
plt.ylabel("Cost function value")
plt.show()


#------------------ Plot the linear fit -------------------------
plt.plot((X[:,1]).reshape(97,1),Y,'o', label = "Training data")
plt.plot((X[:,1]).reshape(97,1),X@w,'-',label = "Linear regression")
plt.xlabel("Population of a city in 10 000s")
plt.ylabel("Profit in $10 000s ")
plt.title("Linear regression and the training data")
plt.legend()
plt.show()
#--------- Prediction for population values 35 000 and 75 000 pop.----------
Prediction1 = (np.array([[1], [35000]])).reshape(1,2)@w
Prediction2 = (np.array([[1], [75000]])).reshape(1,2)@w
print('\nPrediction for 35 000:\n',Prediction1)
print('\nPrediction for 75 000:\n',Prediction2)
#----------- Vizualization Cost function ------------------------
w0_vals = np.linspace(-10,10,100)
w1_vals = np.linspace(-1,4,100)
C_vals = np.zeros((w0_vals.size,w1_vals.size))

for i in range((w0_vals).size):
    for j in range((w1_vals).size):
        t=np.array([w0_vals[i],w1_vals[j]]).reshape(2,1)
        C_vals[[i],[j]]= computeCost(X,Y,t)
C_vals=C_vals.T
#-------------- Print the surface plot of Cost function--------------
fig= plt.figure()
ax=plt.axes(projection='3d')
x, y = np.meshgrid(w0_vals, w1_vals)
surf = ax.plot_surface(x, y, C_vals, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.title("Surface plot of the Cost function")
plt.xlabel("w0")
plt.ylabel("w1")
plt.show()
#----------------------- Contour plot -------------------------------
plt.contour(w0_vals,w1_vals,C_vals,np.logspace(-2,3,20))
plt.plot(w[0],w[1],'x')
plt.title("Contour plot of C_vals in logarithmic scale")
plt.xlabel("w0")
plt.ylabel("w1")
plt.show()
#--------------------------------------------------------------------
import pandas as pd

data = pd.read_csv('Lab1data.txt')
print(data)

