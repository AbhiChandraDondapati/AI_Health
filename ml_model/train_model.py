import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generate synthetic patient data
np.random.seed(42)
X = np.random.rand(1000, 5)  # 1000 patients, 5 health features
y = np.random.choice([0, 1], size=(1000,))  # Binary treatment recommendation (0 or 1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model
with open("ml_model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved in ml_model/model.pkl")
