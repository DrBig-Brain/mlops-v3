from utils import load_model
from xgboost import XGBRegressor
from config import model_path, sc_path
from sklearn.preprocessing import StandardScaler
import pandas as pd
from schema import PredictionInput
def predict(input_data: PredictionInput):
    model = load_model(model_path)
    sc = load_model(sc_path)
    features = pd.DataFrame({
        "trip_distance" : [input_data.trip_distance],
        "PULocationID" : [input_data.PULocationID],
        "DOLocationID" : [input_data.DOLocationID],
        "duration" : [input_data.duration]
    })
    features[['duration','trip_distance']] = sc.transform(features[['duration','trip_distance']])
    prediction = model.predict(features)

    return prediction

if __name__ == "__main__":
    trip_distance =7.37
    PULocationID = 138
    DOLocationID = 75
    duration = 730
    prediction = predict(PredictionInput(trip_distance=trip_distance ,PULocationID= PULocationID, DOLocationID=DOLocationID, duration=duration))
    print(f"predicted fare amount = {prediction}")
