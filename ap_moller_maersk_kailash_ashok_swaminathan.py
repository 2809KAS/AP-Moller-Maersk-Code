# -*- coding: utf-8 -*-
"""AP Moller Maersk_Kailash Ashok Swaminathan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MFTPvbLjve_xgV8hvJvL1mYwyYg6TgbB
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

train_data = pd.read_excel("DS_ML Coding Challenge Dataset (1).xlsx", sheet_name="Training Dataset")

train_data['Month of Sourcing'] = pd.to_datetime(train_data['Month of Sourcing'], format='%b-%y')

label_encoders = {}
for column in train_data.select_dtypes(include='object').columns:
    le = LabelEncoder()
    train_data[column] = le.fit_transform(train_data[column])
    label_encoders[column] = le

X = train_data.drop(columns=['Sourcing Cost', 'Month of Sourcing'])
y = train_data['Sourcing Cost']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_val)

mse = mean_squared_error(y_val, y_pred)
print("Mean Squared Error:", mse)

test_data = pd.read_excel("DS_ML Coding Challenge Dataset (1).xlsx", sheet_name="Test Dataset")

test_data['Month of Sourcing'] = pd.to_datetime(test_data['Month of Sourcing'], format='%b-%y')

for column, le in label_encoders.items():
    test_data[column] = le.transform(test_data[column])

X_test = test_data.drop(columns=['Sourcing Cost', 'Month of Sourcing'])

test_predictions = rf_model.predict(X_test)

test_data['Predicted Sourcing Cost'] = test_predictions
print("\nPredicted Sourcing Cost for June 2021:")
print(test_data[['ProductType', 'Manufacturer', 'Area Code', 'Sourcing Channel', 'Product Size', 'Product Type', 'Predicted Sourcing Cost']])

from sklearn.linear_model import LinearRegression


lr_model = LinearRegression()
lr_model.fit(X_train, y_train)


y_pred_lr = lr_model.predict(X_val)


mse_lr = mean_squared_error(y_val, y_pred_lr)
print("Linear Regression Mean Squared Error:", mse_lr)


test_predictions_lr = lr_model.predict(X_test)

from sklearn.ensemble import GradientBoostingRegressor

gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train, y_train)

y_pred_gb = gb_model.predict(X_val)


mse_gb = mean_squared_error(y_val, y_pred_gb)
print("Gradient Boosting Regression Mean Squared Error:", mse_gb)


test_predictions_gb = gb_model.predict(X_test)

"""Training Dataset and Testing Dataset
Contains several columns including 'ProductType', 'Manufacturer', 'Area Code', 'Sourcing Channel', 'Product Size', 'Product Type', 'Month of Sourcing', and 'Sourcing Cost'.
Each row represents the sourcing of one unit of a particular product combination.

I used three regression techniques namely:
Random Forest: Random Forest is an ensemble learning method that builds multiple decision trees and combines their predictions.

Linear Regression: Linear Regression is a simple and interpretable algorithm that assumes a linear relationship between the input features and the target variable.

Gradient Boosting: Gradient Boosting Regression builds multiple decision trees sequentially, where each tree corrects the errors of the previous one.

Random Forest:
Mean Squared Error (MSE): 3147.85

Linear Regression:
Mean Squared Error (MSE): 4687.54

Gradient Boosting:
Mean Squared Error (MSE): 3308.77

Comparison and Explanation:

Random Forest and Gradient Boosting both perform relatively better than Linear Regression in terms of MSE.
Random Forest and Gradient Boosting provide similar predictions, but Random Forest tends to be more interpretable due to its ensemble nature.
Linear Regression may be not suitable according to given the data due to its linear assumption, resulting in higher MSE.
The choice between Random Forest and Gradient Boosting depends on factors such as interpretability, computational resources, and the specific characteristics of the dataset.

Final Approach:
Considering the performance metrics and the nature of the dataset, the final approach involves using Random Forest or Gradient Boosting for forecasting the June 21 test set. Both algorithms has offerred me relatively low MSE and detailed predictions for each combination of product attributes. But I would prefer Random Forest for the case when interpretability is important, while I would choose Gradient Boosting for higher predictive accuracy.
"""