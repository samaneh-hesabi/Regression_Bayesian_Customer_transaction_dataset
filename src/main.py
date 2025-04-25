import os
import sys
import numpy as np
from data_loader import load_california_data, get_feature_descriptions
from bayesian_regression import (
    build_bayesian_regression_model,
    plot_posterior_distributions,
    plot_feature_importance,
    calculate_regression_metrics,
    plot_metrics
)

def main():
    try:
        # Create results directory if it doesn't exist
        os.makedirs('results', exist_ok=True)
        
        # Load data
        print("Loading data...")
        X, y = load_california_data()
        feature_names = X.columns.tolist()
        print(f"Loaded data with {X.shape[0]} samples and {X.shape[1]} features")
        
        # Build and run Bayesian regression model
        print("\nBuilding Bayesian regression model...")
        model, trace = build_bayesian_regression_model(X, y)
        print("Model built successfully")
        
        # Calculate and display metrics
        print("\nCalculating model metrics...")
        metrics = calculate_regression_metrics(model, trace, X, y)
        
        print("\nModel Performance Metrics:")
        for metric, value in metrics.items():
            if np.isnan(value):
                print(f"{metric}: Could not be calculated")
            else:
                print(f"{metric}: {value:.4f}")
        
        # Plot results
        print("\nPlotting results...")
        plot_posterior_distributions(trace, feature_names)
        plot_feature_importance(trace, feature_names)
        plot_metrics(metrics)
        print("Plots saved to 'results' directory")
        
        # Print feature descriptions
        print("\nFeature Descriptions:")
        for feature, description in get_feature_descriptions().items():
            print(f"{feature}: {description}")
        
        print("\nAnalysis complete! Results saved in the 'results' directory.")
        
    except Exception as e:
        print(f"\nError during analysis: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 