import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

file_path = 'House Price India.csv'  
data = pd.read_csv(file_path)

print("Dataset Overview:")
print(data.head())

features = ['number of bedrooms', 'number of bathrooms', 'living area', 'lot area', 
            'number of floors', 'waterfront present', 'condition of the house', 
            'grade of the house', 'Area of the house(excluding basement)', 
            'Area of the basement', 'Built Year', 'Number of schools nearby', 
            'Distance from the airport']
X = data[features]  
y = data['Price']   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()

import joblib
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as 'house_price_model.pkl'")
