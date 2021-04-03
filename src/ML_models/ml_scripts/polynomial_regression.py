import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score

import os

# VARIABLES
filename = 'FuelConsumption.csv'
features = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']
variable_to_predict = 'CO2EMISSIONS'
#test_size = 0.2
#degree = 2
#interaction_only = False  # Products that have not only one feature
#include_bias = True
#normalize = False

def runPolyRegression(test_size, degree, interaction_only, include_bias, normalize):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    myfile=os.path.join(this_folder, "FuelConsumption.csv")
    filename = 'FuelConsumption.csv'
    features = ['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']
    variable_to_predict = 'CO2EMISSIONS'

    # READ FILE
    df = pd.read_csv(myfile)

    # LOAD FEATURES
    feature_df = df[features]
    X = np.asarray(feature_df)

    # LOAD FEATURE TO BE PREDICTED
    y = np.asarray(df[variable_to_predict])

    # TRAIN TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=4)

    # LOAD MODEL
    poly = PolynomialFeatures(degree=degree, interaction_only=interaction_only, include_bias=include_bias)
    train_x_poly = poly.fit_transform(X_train)
    clf = linear_model.LinearRegression(normalize=normalize)
    clf.fit(train_x_poly, y_train)
    """
    # The coefficients
    print ('Coefficients: ', clf.coef_)
    print ('Intercept: ',clf.intercept_)"""

    # MAKE PREDICTIONS
    test_x_poly = poly.fit_transform(X_test)
    y_hat = clf.predict(test_x_poly)

    # GET METRICS
    results = []
    meanAbsoluteError = np.mean(np.absolute(y_hat - y_test))
    results.append(meanAbsoluteError)
    residualSumOfSquares = np.mean((y_hat - y_test) ** 2)
    results.append(residualSumOfSquares)
    R2score = r2_score(y_hat , y_test)
    results.append(R2score)
    print("Mean absolute error: %.2f" % np.mean(np.absolute(y_hat - y_test)))
    print("Residual sum of squares (MSE): %.2f" % np.mean((y_hat - y_test) ** 2))
    print("R2-score: %.2f" % r2_score(y_hat , y_test) )
    return results