import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score
 
iris = load_iris()
x = iris.data
y= iris.target

print("data shape: ", x.shape)
print("classes:", iris.target_names)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=True)
print("training flowers: ", x_train.shape[0])
print("testing flowers: ", x_test.shape[0])

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print("Data Scaled")

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
print("Model trained")

predictions = model.predict(x_test)
print("f1 score: ", f1_score(y_test, predictions, average='weighted'))

print("\n confusion matrix:")
print(confusion_matrix(y_test, predictions))

print("\n detailed report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))