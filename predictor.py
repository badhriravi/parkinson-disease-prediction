from joblib import dump, load
import numpy as np
import pickle
def predict_class(input_data):
  saved_scaler = load('models/std_scaler.bin')
  saved_model  = pickle.load(open('models/svc_model.sav', 'rb'))
  # changing input data to a numpy array
  data = np.asarray(input_data)
  # reshape the numpy array
  data = data.reshape(1,-1)
  # standardize the data
  std_data = saved_scaler.transform(data)
  prediction = saved_model.predict(std_data)
  
  if (prediction[0] == 0):
    result = "The Person does not have Parkinsons Disease"
  else:
    result = "The Person has Parkinsons Disease "
  return result

  # test case [119.992,157.302,74.997,0.00784,0.00007,0.0037,0.00554,0.01109,0.04374,0.426,0.02182,0.0313,0.02971,0.06545,0.02211,21.033,1,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654]