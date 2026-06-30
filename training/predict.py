from utils import load_model
from xgboost import XGBRegressor
from config import model_path, sc_path
from sklearn.preprocessing import StandardScaler
import pandas as pd

def predict(trip_distance, PULocationID, DOLocationID, duration):
    model = load_model(model_path)
    sc = load_model(sc_path)
    features = pd.DataFrame({
        "trip_distance":[trip_distance],
        "PULocationID":[PULocationID],
        "DOLocationID":[DOLocationID],
        "duration":[duration]
    })
    features[['duration','trip_distance']] = sc.transform(features[['duration','trip_distance']])
    prediction = model.predict(features)

    return prediction

if __name__ == "__main__":
    prediction = predict(2.8,237,68,759)
    print(f"predicted fare amount = {prediction}")
