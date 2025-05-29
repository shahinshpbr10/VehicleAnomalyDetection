import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

data = pd.read_csv('engine_data.csv')
X = data[['engine_temp', 'rpm']]
y = data['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)


prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print(f"Model Accuracy: {round(accuracy * 100, 2)}%")


joblib.dump(model, "model.pkl")
print("Model saved to model.pkl")

mlflow.set_experiment("Vehicle Anomaly Testing")

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")
    print("Model logged to MLflow")
    

