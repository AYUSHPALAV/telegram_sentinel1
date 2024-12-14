import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

class AdvancedMLClassifier:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
        self.is_fitted = False
    
    def prepare_training_data(self, X, y):
        """Prepare and scale training data"""
        X_scaled = self.scaler.fit_transform(X)
        self.is_fitted = True
        return train_test_split(X_scaled, y, test_size=0.2)
    
    def train(self, X, y):
        """Train the classification model"""
        X_train, X_test, y_train, y_test = self.prepare_training_data(X, y)
        self.model.fit(X_train, y_train)
        
        # Evaluate and save model
        accuracy = self.model.score(X_test, y_test)
        print(f"Model Accuracy: {accuracy}")
        
        # Ensure directory exists
        os.makedirs('models', exist_ok=True)
        
        # Save both model and scaler
        joblib.dump(self.model, 'models/scam_detection_model.pkl')
        joblib.dump(self.scaler, 'models/scaler.pkl')
    
    def load_model(self):
        """Load pre-trained model and scaler"""
        try:
            self.model = joblib.load('models/scam_detection_model.pkl')
            self.scaler = joblib.load('models/scaler.pkl')
            self.is_fitted = True
        except FileNotFoundError:
            print("No pre-trained model found. Please train the model first.")
            return False
        return True
    
    def classify(self, message, nlp_result):
        """Classify message risk"""
        if not self.is_fitted:
            print("Model not fitted. Training or loading a model first.")
            return 0.5  # Default risk score if not fitted
        
        features = np.array([
            nlp_result['text_length'],
            len(nlp_result['detected_threats']),
            nlp_result['complexity_score'],
            message.user.credibility_score
        ]).reshape(1, -1)
        
        features_scaled = self.scaler.transform(features)
        return self.model.predict_proba(features_scaled)[0][1]