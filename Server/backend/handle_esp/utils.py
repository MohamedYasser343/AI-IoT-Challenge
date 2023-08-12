import numpy
import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler

def predict_data(data):
    timestamp = pd.DataFrame(list(data.values('timestamp')))
    # data = pd.DataFrame(list(data.values('temperature', 'humidity',
    #                                      'light_intensity', 'ph', 'soil_moisture',
    #                                      'soil_temperature', 'water_temperature', 'flow_intensity')))
    data = pd.DataFrame(list(data.values('temperature')))
    data = data.astype('float32')
    
    timestamp.set_index('timestamp', inplace=True)
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)
    
    look_back = 7
    X_data, Y_data = create_dataset(data, look_back)
    X_new = numpy.reshape(X_data, (X_data.shape[0], 1, X_data.shape[1]))

    model = load_model()

    predictions = model.predict(X_new)
    # dates = data.index[-len(predictions):]

    # temperature_predictions = predictions[:, 0]
    # humidity_predictions = predictions[:, 1]
    
    temperature_predictions = scaler.inverse_transform(data)
    # humidity_predictions = scaler.inverse_transform(humidity_predictions.reshape(-1, 1)).flatten()
    
    result = {
        'temperature': temperature_predictions,
        # 'humidity': humidity_predictions,
    }
    
    return result
    
    
    
def load_model():
    with open('ai_models/time-series-prediction-model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)
