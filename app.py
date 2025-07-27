from flask import Flask, render_template, request
import pickle
import numpy as np
from num2words import num2words  # Added for converting numbers to words

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # make sure this exists with your form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the trained model and model columns
        model = pickle.load(open("house_price_model.pkl", "rb"))
        model_columns = pickle.load(open("model_columns.pkl", "rb"))

        # Retrieve form data in the order of model_columns
        input_data = []
        for col in model_columns:
            value = request.form.get(col, 0)
            input_data.append(float(value))

        # Make prediction
        final_features = np.array(input_data).reshape(1, -1)
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        # Format price with commas
        formatted_price = "{:,.2f}".format(output)
        # Convert price to words in Indian format (no currency)
        price_in_words = num2words(output, lang='en_IN')

        return render_template('result.html', prediction_text=formatted_price, prediction_words=price_in_words)

    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)