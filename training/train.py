from xgboost import XGBRegressor
from utils import load_dataset, save_model
from evaluate import evaluate
from config import best_params, model_path
def train():
    X_train,X_test,y_train,y_test = load_dataset()
    model = XGBRegressor(
        n_estimators = best_params['n_estimators'],
        max_depth = best_params['max_depth'],
        learning_rate = best_params['learning_rate'],
        objective = best_params['objective'],
        tree_method = best_params['tree_method']
    )

    print("Training Model \n")
    model.fit(X_train,y_train)
    print("Finished Training Model\n")
    training_result = evaluate(model,X_test,y_test)

    print(f"Training Resutl:{training_result}")

    save_model(model_path,model)
    print(f"model saved to {model_path}")

if __name__ == "__main__":
    train()