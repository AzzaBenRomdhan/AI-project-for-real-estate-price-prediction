import pickle
import numpy as np

# Charger le modèle ML
def load_model():
    with open('instance/xgb_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

def make_prediction(data):
    features = np.array([[
        data['lotSize'],
        data['bedrooms'],
        data['bathrooms'],
        data['garageSize'],
        data['yearOfBuild'],
    ]])
    prediction = model.predict(features)[0]
    prediction = float(prediction)
    return prediction
