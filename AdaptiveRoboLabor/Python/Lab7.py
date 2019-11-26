import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
#------------- USED FUNCTIONS DECLARATIONS ---------------------
def sigmoid(z):
    return 1/(1+(np.exp(-z)))

def sigmoidGradient(z):
    return sigmoid(z) * (1-sigmoid(z))


def nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, Lambda):
    """
    nn_params contains the parameters unrolled into a vector

    compute the cost and gradient of the neural network
    """
    # Reshape nn_params back into the parameters Theta1 and Theta2
    Theta1 = nn_params[:((input_layer_size + 1) * hidden_layer_size)].reshape(hidden_layer_size, input_layer_size + 1)
    Theta2 = nn_params[((input_layer_size + 1) * hidden_layer_size):].reshape(num_labels, hidden_layer_size + 1)

    m = X.shape[0]
    J = 0
    X = np.hstack((np.ones((m, 1)), X))
    y10 = np.zeros((m, num_labels))

    a1 = sigmoid(X @ Theta1.T)
    a1 = np.hstack((np.ones((m, 1)), a1))  # hidden layer
    a2 = sigmoid(a1 @ Theta2.T)  # output layer

    for i in range(1, num_labels + 1):
        y10[:, i - 1][:, np.newaxis] = np.where(y == i, 1, 0)
    for j in range(num_labels):
        J = J + sum(-y10[:, j] * np.log(a2[:, j]) - (1 - y10[:, j]) * np.log(1 - a2[:, j]))

    cost = 1 / m * J
    reg_J = cost + Lambda / (2 * m) * (np.sum(Theta1[:, 1:] ** 2) + np.sum(Theta2[:, 1:] ** 2))

    # Implement the backpropagation algorithm to compute the gradients

    grad1 = np.zeros((Theta1.shape))
    grad2 = np.zeros((Theta2.shape))

    for i in range(m):
        xi = X[i, :]  # 1 X 401
        a1i = a1[i, :]  # 1 X 26
        a2i = a2[i, :]  # 1 X 10
        d2 = a2i - y10[i, :]
        d1 = Theta2.T @ d2.T * sigmoidGradient(np.hstack((1, xi @ Theta1.T)))
        grad1 = grad1 + d1[1:][:, np.newaxis] @ xi[:, np.newaxis].T
        grad2 = grad2 + d2.T[:, np.newaxis] @ a1i[:, np.newaxis].T

    grad1 = 1 / m * grad1
    grad2 = 1 / m * grad2

    grad1_reg = grad1 + (Lambda / m) * np.hstack((np.zeros((Theta1.shape[0], 1)), Theta1[:, 1:]))
    grad2_reg = grad2 + (Lambda / m) * np.hstack((np.zeros((Theta2.shape[0], 1)), Theta2[:, 1:]))

    return cost, grad1, grad2, reg_J, grad1_reg, grad2_reg

def randInitializeWeights(L_in, L_out):
    epsilon_init = 0.12

    W = np.random.rand(L_out,L_in+1)*(2*epsilon_init)-epsilon_init

    return W


def gradientDescentnn(X, y, initial_nn_params, alpha, num_iters, Lambda, input_layer_size, hidden_layer_size,
                      num_labels):
    """
    Take in numpy array X, y and theta and update theta by taking num_iters gradient steps
    with learning rate of alpha

    return theta and the list of the cost of theta during each iteration
    """
    Theta1 = initial_nn_params[:((input_layer_size + 1) * hidden_layer_size)].reshape(hidden_layer_size,
                                                                                      input_layer_size + 1)
    Theta2 = initial_nn_params[((input_layer_size + 1) * hidden_layer_size):].reshape(num_labels, hidden_layer_size + 1)

    m = len(y)
    C_history = []

    for i in range(num_iters):
        if (i%10==0):
            print('Iteration:', i+1)
        elif (i==num_iters):
            print('Done!')
        nn_params = np.append(Theta1.flatten(), Theta2.flatten())
        cost, grad1, grad2 = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, num_labels, X, y, Lambda)[
                             3:]
        Theta1 = Theta1 - (alpha * grad1)
        Theta2 = Theta2 - (alpha * grad2)
        C_history.append(cost)

    nn_paramsFinal = np.append(Theta1.flatten(), Theta2.flatten())
    return nn_paramsFinal, C_history

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



#------------- USED FUNCTIONS END ------------------------------
#-------------- Load the data ----------------------------------
data = loadmat("Lab7data.mat")
X = data["X"]
Y = data ["y"]
del data
m = X.shape[0]
print('Shape of X and Y in order:')
print(X.shape)
print(Y.shape)
#------------- Load weights ------------------------------------
data = loadmat("Lab7Weights.mat")
w1 = np.array(data["Theta1"])
w2 = np.array(data["Theta2"])
print('Shape of w1 and w2 in order:')
print(w1.shape)
print(w2.shape)
del data
#---------------- visualization of the data --------------------
print("Printing some random data ...")
fig, ax = plt.subplots(10,10, figsize =(8,8))
for i in range(10):
    for j in range(10):
        ax[i,j].imshow(X[np.random.randint(0,m+1),:].reshape(20,20, order = "F"), cmap="hot")
        ax[i,j].axis("off")
plt.show()
#----------------- Compute Cost (Feedforward) --------------------
Lambda = 1
input_layer_size = 400
hidden_layer_size = 25
num_labels = 10
nn_params = np.append(w1.flatten(), w2.flatten())

C, reg_C = nnCostFunction(nn_params,input_layer_size,hidden_layer_size,num_labels,X,Y,Lambda)[0:4:3]
print("Cost at parameters (non-regularized):",C,"\nCost at parameters (Regularized):",reg_C)

initial_w1 = randInitializeWeights(input_layer_size,hidden_layer_size)
initial_w2 = randInitializeWeights(hidden_layer_size,num_labels)
initial_nn_params = np.append(initial_w1.flatten(),initial_w2.flatten())

nnw, nnC_history = gradientDescentnn(X,Y,initial_nn_params,0.8,800,1,input_layer_size,hidden_layer_size,num_labels)
w1 = nnw[:((input_layer_size+1) * hidden_layer_size)].reshape(hidden_layer_size,input_layer_size+1)
w2 = nnw[((input_layer_size +1)* hidden_layer_size ):].reshape(num_labels,hidden_layer_size+1)

pred3 = predict(w1,w2,X)
acc = accuracy(pred3,Y)

print('Training Set Accuracy:',acc,'%')
plt.plot(nnC_history)
plt.show()

