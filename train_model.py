import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# File paths
dataset_path = 'C:/Users/Aryan/Desktop/Python/combined_city_data.csv'
model_path = 'C:/Users/Aryan/Desktop/Python/house_price_model.pkl'
columns_path = 'C:/Users/Aryan/Desktop/Python/model_columns.pkl'

try:
    # Load the dataset
    df = pd.read_csv(dataset_path)
    print("✅ Dataset loaded successfully.")
    print(f"📌 Shape: {df.shape}")
    print("📋 Columns:", df.columns.tolist())

    # Select features and target
    selected_columns = [
        'Area',
        'No. of Bedrooms',
        'Gymnasium',
        'SwimmingPool',
        'CarParking',
        'LiftAvailable',
        'PowerBackup'
    ]
    target_column = 'Price'

    # Drop missing values
    df = df[selected_columns + [target_column]].dropna()

    # Split features and target
    X = df[selected_columns]
    y = df[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("✅ Model trained successfully.")

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"📉 Mean Squared Error on test set: {mse:.2f}")

    # Save the model
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"💾 Model saved to: {model_path}")

    # Save the feature columns
    model_columns = X.columns.tolist()
    with open(columns_path, 'wb') as f:
        pickle.dump(model_columns, f)
    print(f"🧾 Model columns saved to: {columns_path}")

except FileNotFoundError:
    print("❌ CSV file not found. Please check the file path.")
except KeyError as e:
    print(f"❌ Missing column: {e}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
