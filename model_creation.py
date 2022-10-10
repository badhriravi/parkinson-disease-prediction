import numpy as np
import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

def model_creation():
  print("data loading and preprocessing started ... - ")
  parkinsons_data = pd.read_csv("parkinson_data.csv")
  print("getting more information about the dataset")
  print(parkinsons_data.info())
  X = parkinsons_data.drop(columns=['name','status'], axis=1)
  Y = parkinsons_data['status']
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
  print("data loading and preprocessing ended ... - ")

  print("model loading and training started ... - ")
  scaler = StandardScaler()
  scaler.fit(X_train)
  X_train = scaler.transform(X_train)
  X_test = scaler.transform(X_test)
  model = svm.SVC(kernel='linear')
  model.fit(X_train, Y_train)
  print("model loading and training ended ... - ")

  print("model testing and training training data accuracy started ... - ")
  X_train_prediction = model.predict(X_train)
  training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
  print('Accuracy score of training data : ', training_data_accuracy)
  X_test_prediction = model.predict(X_test)
  test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
  print('Accuracy score of test data : ', test_data_accuracy)
  print("model testing and training training data accuracy started ... - ")

  print("model and scaler saveing started ... - ")
  dump(model,'svc_model.sav')
  dump(scaler,'std_scaler.bin', compress=True)
  print("model and scaler saveing ended ... - ")
if __name__=="__main__":
  model_creation()

