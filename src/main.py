import os
from data_loader import load_california_data, get_feature_descriptions
from bayesian_regression import (
    build_bayesian_regression_model,
    plot_posterior_distributions,
    plot_feature_importance
)

def main():
    # Create results directory if it doesn't exist
    os.makedirs('results', exist_ok=True)
    
    # Load data
    X, y = load_california_data()
    feature_names = X.columns.tolist()
    
    # Build and run Bayesian regression model
    print("Building Bayesian regression model...")
    model, trace = build_bayesian_regression_model(X, y)
    
    # Plot results
    print("Plotting results...")
    plot_posterior_distributions(trace, feature_names)
    plot_feature_importance(trace, feature_names)
    
    # Print feature descriptions
    print("\nFeature Descriptions:")
    for feature, description in get_feature_descriptions().items():
        print(f"{feature}: {description}")
    
    print("\nAnalysis complete! Results saved in the 'results' directory.")

if __name__ == "__main__":
    main() 