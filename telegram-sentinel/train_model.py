import numpy as np
from telegram_sentinel.ml_classifier import AdvancedMLClassifier

def generate_sample_data():
    """Generate synthetic training data"""
    X = np.random.rand(1000, 4)  # Features
    y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Binary labels
    return X, y

def main():
    classifier = AdvancedMLClassifier()
    X, y = generate_sample_data()
    classifier.train(X, y)
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    main()