import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from config import sc_path
import pickle

def save_model(path,model):
    with open(path,'wb') as f:
        pickle.dump(model, f)

def load_model(path):
    with open(path,'rb') as f:
        model = pickle.load(f)
    return model

def load_dataset():
    path = "../datasets/processed/"
    datasets = os.listdir(path)

    df = pd.read_parquet(path+datasets[-1])
    X = df.drop(columns=['fare_amount'])
    y = df['fare_amount']

    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2, random_state = 43)

    sc = StandardScaler()
    sc.fit(X_train[['duration','trip_distance']])
    X_train[['duration','trip_distance']] = sc.transform(X_train[['duration','trip_distance']])
    X_test[['duration','trip_distance']] = sc.transform(X_test[['duration','trip_distance']])
    
    with open(sc_path,'wb') as f:
        pickle.dump(sc,f)
    print(f"saved standard scaler to {sc_path}")
    
    return X_train,X_test,y_train,y_test
