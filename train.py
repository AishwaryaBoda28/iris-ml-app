"""
Train Iris Flower Prediction Model
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

data = load_iris()
X = data.data
y = data.target

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model trained & saved successfully!")
