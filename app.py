from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return "Welcome to the Diabetes Prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    features = np.array([[
        data["Pregnancies"], data["Glucose"], data["BloodPressure"],
        data["SkinThickness"], data["Insulin"], data["BMI"],
        data["DiabetesPedigreeFunction"], data["Age"]
    ]])
    prediction = model.predict(features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
