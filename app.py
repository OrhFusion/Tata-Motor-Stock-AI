from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from the form
    try:
        open_val = float(request.form['Open'])
        low_val = float(request.form['Low'])
        high_val = float(request.form['High'])
        volume_val = float(request.form['Volume'])
        
        # Prepare the input for the model
        input_data = np.array([[open_val, low_val, high_val, volume_val]])
        
        # Make a prediction
        prediction = model.predict(input_data)
        
        # Return the result
        return render_template('index.html', prediction_text=f'Predicted Close Price: {prediction[0]:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text='Error in prediction: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)
