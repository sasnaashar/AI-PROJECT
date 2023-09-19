# Import the necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: House size (in square feet) and corresponding prices (in thousands of dollars)
X = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]).reshape(-1, 1)
y = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])

# Create a linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(X, y)

# Predict the price of a house with size 2000 square feet
predicted_price = model.predict([[2000]])

# Print the predicted price
print("Predicted price for a 2000 sq. ft. house:", predicted_price[0])


