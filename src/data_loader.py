import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

def load_california_data():
    """
    Load and preprocess the California Housing dataset.
    
    Returns:
        tuple: (X, y) where X is the feature matrix and y is the target variable
    """
    # Load the dataset
    california = fetch_california_housing()
    X = pd.DataFrame(california.data, columns=california.feature_names)
    y = pd.Series(california.target, name='MedHouseVal')  # Median house value
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X),
        columns=X.columns
    )
    
    return X_scaled, y

def get_feature_descriptions():
    """
    Get descriptions of the California Housing dataset features.
    
    Returns:
        dict: Dictionary mapping feature names to their descriptions
    """
    return {
        'MedInc': 'Median income in block group',
        'HouseAge': 'Median house age in block group',
        'AveRooms': 'Average number of rooms per household',
        'AveBedrms': 'Average number of bedrooms per household',
        'Population': 'Block group population',
        'AveOccup': 'Average number of household members',
        'Latitude': 'Block group latitude',
        'Longitude': 'Block group longitude'
    } 