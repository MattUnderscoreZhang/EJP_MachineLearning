import pandas as pd
import numpy as np

###############
# IMPORT DATA #
###############

data_file = open("data.csv")
data = pd.read_csv(data_file, delimiter=' ', header=None).values
x1_list = data[0]
x2_list = data[1]
y_list = data[2]

#########################
# INITIALIZE PARAMETERS #
#########################

# model is y = t1 * x1 + t2 * exp(x2 / t3)
t1 = np.random.normal()
t2 = np.random.normal()
t3 = np.random.normal()
print("Parameters start at", t1, t2, t3)

#########
# TRAIN #
#########

learning_rate = 0.0001
batch_size = 100
n_epochs = 500
t1_grad = 0
t2_grad = 0
t3_grad = 0

for i in range(n_epochs):
    for iteration_n, (x1, x2, y) in enumerate(zip(x1_list, x2_list, y_list)):
        # calculate output using model
        y_predicted = t1 * x1 + t2 * (x2 + t3)
        # calculate loss
        loss = (y_predicted - y)**2
        # find gradients
        t1_grad += 2*(y_predicted - y) * x1
        t2_grad += 2*(y_predicted - y) * (x2 + t3)
        t3_grad += 2*(y_predicted - y) * t2
        # update parameters
        if (iteration_n+1)%batch_size == 0:
            t1 -= learning_rate * t1_grad / batch_size
            t2 -= learning_rate * t2_grad / batch_size
            t3 -= learning_rate * t3_grad / batch_size
            t1_grad = 0
            t2_grad = 0
            t3_grad = 0
            # print to screen
            print("Iteration", iteration_n+1, "- loss is", loss, "- parameters are", t1, t2, t3)
