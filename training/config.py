import numpy as np

best_params = {
    'learning_rate': np.float64(0.2632967408189152),
    'max_depth': 7,
    'n_estimators': 150,
    'objective' : 'reg:squarederror',
    'tree_method' : 'hist',
}

model_path = "../models/model.pkl"
sc_path = "../models/sc.pkl"