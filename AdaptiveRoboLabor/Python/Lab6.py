import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.io import loadmat
# -------- USED FUNCTIONS DEFINITIONS -------------------------
def sigmoid(z):
    return 1/(1+np.exp(-z))

def predict(w1,w2,X):
    m = X.shape[0]

    a1 = np.column_stack((np.ones((m,1)),X))
    z2 = a1 @ w1.T
    a2 = np.column_stack((np.ones((m,1)),sigmoid(z2)))
    z3 = a2 @ w2.T
    a3 = sigmoid(z3)

    return np.argmax(a3,axis=1)+1

def accuracy(pred,Y):
    return (np.sum(pred[:,np.newaxis]==Y)/5000)*100


#-------- USED FUNCTIONS DEFINITIONS END -------------------------
#------- SETTING UP SOME PARAMETRES ------------------------------
input_layer_size = 400
hidden_layer_size = 25
num_labels = 10
#------------- Loading data --------------------------------------
data = loadmat("Lab6data.mat")
# ide nem árthat kiiratni amm, hogy lássák mi a felosztás és mi alapján rendezzük később
X = data["X"]
Y = data ["y"]
m = X.shape[0]
del data
print('''Shape of the dataset in order X and Y:
''',X.shape,'\n',Y.shape,'\n')
#-------------- displaying some random data ------------------------
print("Printing some random data ...")
fig, ax = plt.subplots(10,10, figsize =(8,8))
for i in range(10):
    for j in range(10):
        ax[i,j].imshow(X[np.random.randint(0,m+1),:].reshape(20,20, order = "F"), cmap="hot")
        ax[i,j].axis("off")
plt.show()
#---------------- loading the optimized theta -------------------------
data = loadmat("Lab6weights.mat")
w1 = data["Theta1"]
w2 = data["Theta2"]
print('''Shape of the weights in order 1 and 2:
''',w1.shape,'\n',w2.shape,'\n')

pred = predict(w1,w2,X)
print('\nTraining set Accuracy: ', accuracy(pred,Y), ' %')






