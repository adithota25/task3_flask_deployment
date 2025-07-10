# Task 3 – Model Deployment using Flask (CodTech Data Science Internship)

## 📌 Description:
This task demonstrates the deployment of a machine learning model using **Flask**, a lightweight web framework in Python.  
We trained a **Logistic Regression** model using the **Pima Indians Diabetes dataset** to predict whether a person is likely to have diabetes based on input features.

---

## ✅ Steps Performed:
1. Loaded dataset from a public GitHub CSV link
2. Trained a Logistic Regression classifier
3. Exported the trained model using `joblib` as `diabetes_model.pkl`
4. Created a REST API using Flask:
   - `/` → Welcome message
   - `/predict` → Accepts JSON data and returns prediction
5. Tested the API using Postman or `curl`

---

## 🧰 Technologies Used:
- Python
- Scikit-learn
- Flask
- Pandas, NumPy
- Joblib (for model saving)

---

## 📁 Files Included:
- `task3_flask_deployment.ipynb`: Notebook with full model training process
- `diabetes_model.pkl`: Trained Logistic Regression model
- `app.py`: Flask application code to serve the model
- `README.md`: Documentation for Task 3

---

## ▶️ How to Run the Flask App:

1. Make sure `app.py` and `diabetes_model.pkl` are in the same folder
2. Open your terminal or command prompt
3. Run the Flask app:
```bash
python app.py
👩‍💻 Author:
Thota Adisrilakshmi
CodTech Data Science Internship
July 2025
