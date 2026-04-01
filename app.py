from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    features = [
        int(data['age']),
        int(data['sex']),
        int(data['cp']),
        int(data['trestbps']),
        int(data['chol']),
        int(data['fbs']),
        int(data['restecg']),
        int(data['thalach']),
        int(data['exang']),
        float(data['oldpeak']),
        int(data['slope']),
        int(data['ca']),
        int(data['thal'])
    ]

    input_data = np.array([features])

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        result = f"⚠️ High Risk of Heart Disease ({prob*100:.2f}%)"
        color = "red"
    else:
        result = f"✅ Low Risk ({(1-prob)*100:.2f}%)"
        color = "green"

    return render_template('index.html', prediction_text=result, color=color)


# API version (bonus feature)
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    input_data = np.array([list(data.values())])
    prediction = model.predict(input_data)[0]
    return jsonify({'prediction': int(prediction)})


if __name__ == "__main__":
    app.run(debug=True)