##### PART ONE #####

# Import some common packages
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# to make this notebook's output stable across runs
np.random.seed(42)

# Ignore warnings
import warnings
warnings.filterwarnings(action="ignore")

# Your code goes here for this section, make sure you also include the output to answer the above questions.
datasetURL = "https://www.kaggle.com/mohansacharya/graduate-admissions" # required url to download for CSV file. The TA will download and run your program.

def load_admission_data():
    return pd.read_csv("Admission_Predict_Ver1.1.csv", sep = ",")

admission = load_admission_data()

####################

##### PART TWO #####

# You might want to use the following package
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Your code goes here for this section.

# we do not need the serial numbers, get rid of them
admission.drop(labels = ["Serial No."], axis = 1, inplace = True)

# there is a space after the "Chance of Admit", we will get rid of it to make things easier
admission = admission.rename(columns = {"Chance of Admit ":"Chance of Admit", "LOR ":"LOR"})

# now we set y_train to equal to the Chance of Admit values, and X_train to equal the other features.
y_data = admission["Chance of Admit"].values
X_data = admission.drop(labels = ["Chance of Admit"], axis = 1, inplace = False).copy()

# now we scale the x-value features of the data
scaler = StandardScaler()
X_data[X_data.columns] = scaler.fit_transform(X_data[X_data.columns])

# split the training and testing data 80/20
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 0.2, random_state = 42)

####################

##### PART THREE #####

class MyLinearRegression:
    def __init__(self):
        self.theta = 0  # parameter vector, set after fit
        self.cost = 0  # cost function, set after every iteration
        self.alpha = 0.1  # learning rate, HYPERPARAM
        self.iterations = 250  # iterations, HYPERPARAM

    def fitUsingGradientDescent(self, X_train, y_train):
        # make copies of data so we do not modify them
        XTrain = X_train.copy()
        yTrain = y_train.copy()

        # initialize theta with correct number of columns
        # we have len(X_train.columns) features, plus one for intercept
        self.theta = np.random.randn(len(XTrain.columns)+1, 1)

        # add a column of 1's to X_train for intercept
        XTrain['intercept'] = 1

        return self.gradientDescent(X_train=XTrain,
                                    y_train=yTrain,
                                    theta=self.theta,
                                    alpha=self.alpha,
                                    iters=self.iterations)

    def gradientDescent(self, X_train, y_train, theta, alpha, iters):
        # INPUT:
        # alpha: the learning rate
        # iters: number of iterations
        #
        # OUTPUT:
        # theta: updated value for theta
        # cost: value of the cost function

        # initialize data
        m = len(X_train.index)
        X_b = X_train.copy()
        y = y_train.copy()

        # initialize list to store costs over iterations
        listIters = []
        listCosts = []

        # perform gradient descent loop
        for iteration in range(iters):
            first = X_b.transpose()
            second = X_b.dot(theta)
            third = second.sub(y, axis=0) # 400r x 1c
            gradients = (2 / m) * (first).dot(third)
            theta = theta - alpha * gradients # at this point theta is the correct vector

            # now we must calculate cost
            fourth = X_b.dot(theta)
            fifth = fourth.sub(y, axis=0)
            sixth = fifth.transpose()
            costMatrix = sixth.dot(fifth)

            # update cost with the only value in the costMatrix
            self.cost = costMatrix.values[0][0]
            listIters.append(iteration)
            listCosts.append(self.cost)

        # this is the finished theta vector for prediction
        self.theta = theta

        # return costs so we can plot
        return listIters, listCosts

    def predict(self, X_test):
        testParams = X_test.copy()

        # add a column of 1's to X_test for intercept
        testParams['intercept'] = 1

        # compute and return X_test.dot(theta) to find predicted y's
        predicted = testParams.dot(self.theta)
        return predicted

    def fitUsingNormalEquation(self, X_train, y_train):
        X = X_train.copy()
        y = y_train.copy()

        # add a column of 1's to X_test for intercept
        X['intercept'] = 1

        nonInverted = (X.transpose().dot(X))
        inverted = pd.DataFrame(np.linalg.pinv(nonInverted.values), nonInverted.columns, nonInverted.index)

        # finished theta vector
        theta = inverted.dot(X.transpose()).dot(y)
        self.theta = theta

        # calculate cost
        fourth = X.dot(theta)
        fifth = fourth.sub(y, axis=0)
        sixth = fifth.transpose()
        cost = sixth.dot(fifth)
        self.cost = cost

        # return the cost
        return cost

# initialize model object
myGradientDescentModel = MyLinearRegression()

# show that cost is decreasing as number of iterations increases
listIters, listCosts = myGradientDescentModel.fitUsingGradientDescent(X_train, y_train)
plt.plot(listIters, listCosts)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost vs. Training Iterations')
plt.show()

# set iterations to lower value so we can plot multiple curves on one chart
myGradientDescentModel.iterations = 20

# initialize plot
import matplotlib.pyplot as plt

# try every learning rate from 0.1 to 1, in increments of 0.1
learningRates = np.linspace(0.20, 0.22, 6)
for learningRate in learningRates:
    myGradientDescentModel.alpha = learningRate
    listIters, listCosts = myGradientDescentModel.fitUsingGradientDescent(X_train, y_train)
    plt.plot(listIters, listCosts, label='%.3f'%(learningRate))
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Error vs. Training Iterations')
plt.legend(loc='lower right')
plt.show()

######################

##### PART FOUR #####

myNormalEquationModel = MyLinearRegression()
myNormalEquationModel.fitUsingNormalEquation(X_train, y_train)
print("Cost, using normal equation: ", myNormalEquationModel.cost)

#####################

##### PART FIVE #####

from sklearn.metrics import mean_squared_error

# Use the built-in SGD Regressor model
from sklearn.linear_model import SGDRegressor
mySGDModel = SGDRegressor()
mySGDModel.fit(X_train,y_train)
y_predict = mySGDModel.predict(X_test)
mse = mean_squared_error(y_test, y_predict)
mySGDModel_rmse = np.sqrt(mse)
print("SGD Model RMSE: ", mySGDModel_rmse)

# myGradientDescentModel_rmse
myGradientDescentModel = MyLinearRegression()
myGradientDescentModel.alpha = 0.15
myGradientDescentModel.iterations = 100
myGradientDescentModel.fitUsingGradientDescent(X_train, y_train)
y_predict = myGradientDescentModel.predict(X_test)
mse = mean_squared_error(y_test, y_predict)
myGradientDescentModel_rmse = np.sqrt(mse)
print("My Gradient Descent Model RMSE: ", myGradientDescentModel_rmse)

# myNormalEquationModel_rmse
myNormalEquationModel = MyLinearRegression()
myNormalEquationModel.fitUsingNormalEquation(X_train, y_train)
y_predict = myNormalEquationModel.predict(X_test)
mse = mean_squared_error(y_test, y_predict)
myNormalEquationModel_rmse = np.sqrt(mse)
print("My Normal Equation Model RMSE: ", myNormalEquationModel_rmse)

#####################
