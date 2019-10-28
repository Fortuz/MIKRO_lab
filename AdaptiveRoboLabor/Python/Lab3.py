import numpy as np
import matplotlib.pyplot as plt

# -------- USED FUNCTIONS DEFINITIONS -------------------------


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
print('X értékei:\n',X)
print('Y értékei:\n',Y)
'''




