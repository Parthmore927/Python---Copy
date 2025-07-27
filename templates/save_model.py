import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Path to your dataset
file_path = 'C:/Users/Aryan/Desktop/Python/House Price India.csv'

# Function to train and save the model
def train_model():
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        print("Dataset columns:", df.columns)

        # Update the feature and target column names
        feature_columns = ['number of bedrooms', 'number of bathrooms', 'living area', 'lot area', 'number of floors']
        target_column = 'Price'

        # Check if the feature columns exist in the dataset
        if not set(feature_columns).issubset(df.columns):
            raise KeyError(f"Some feature columns are missing in the dataset: {feature_columns}")

        # Prepare the features (X) and target (y)
        X = df[feature_columns]
        y = df[target_column]

        # Train the model
        model = LinearRegression()
        model.fit(X, y)

        # Save the trained model
        model_path = 'house_price_model.pkl'
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)

        print(f"Model trained and saved successfully to {model_path}!")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the dataset file exists at the specified path.")
    except KeyError as e:
        print(f"Error: {e}. Please check the column names in your dataset.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to make predictions using the saved model
def predict(features):
    try:
        # Load the saved model
        with open('house_price_model.pkl', 'rb') as file:
            model = pickle.load(file)

        # Ensure the model is loaded correctly
        if isinstance(model, LinearRegression):
            print("Model loaded successfully!")
        else:
            print("Error: Loaded model is not a LinearRegression model.")

        # Make prediction (reshape the features array to match the input shape expected by the model)
        prediction = model.predict([features])  # Features must be in 2D format
        print(f"Predicted Price: {prediction[0]}")

    except FileNotFoundError:
        print("Error: The model file 'house_price_model.pkl' is not found.")
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

# Main flow
if __name__ == "__main__":
    # Train the model (run this once to save the model)
    train_model()

    # Example of making a prediction (make sure to pass correct feature values)
    features = [3, 2, 1500, 2000, 2]  # Example input for prediction (bedrooms, bathrooms, living area, lot area, floors)
    predict(features)
