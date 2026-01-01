import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def prepare_data(file_path, test_size=0.2, random_state=42):
    """
    Data Preprocessing: Handles data loading, feature engineering, 
    dataset splitting, and feature scaling.
    """
    # 1. Load dataset
    data = pd.read_csv(file_path)
    
    # 2. Feature Selection: Define input features (X) and target variable (y)
    # Inputs: Longitudinal position, Prismatic coefficient, L/D ratio, etc.
    X = data[['LC', 'PC', 'LD', 'BDr', 'LB', 'Fr']].values
    # Target: Residuary resistance
    y = data['Rr'].values.reshape(-1, 1)
    
    # 3. Dataset Splitting: Segregate training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # 4. Feature Scaling: Standardize features for distance-based algorithms
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 5. Scaler Persistence: Export scaler to ensure consistency during deployment
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/feature_scaler.pkl')
    
    return X_train, X_test, X_train_scaled, X_test_scaled, y_train.ravel(), y_test.ravel()