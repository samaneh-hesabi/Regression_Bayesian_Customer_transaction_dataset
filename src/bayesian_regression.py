import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def build_bayesian_regression_model(X, y):
    """
    Build and run a Bayesian linear regression model.
    
    Args:
        X (pd.DataFrame): Feature matrix
        y (pd.Series): Target variable
        
    Returns:
        tuple: (model, trace) containing the PyMC model and trace
    """
    n_features = X.shape[1]
    
    with pm.Model() as model:
        # Priors
        alpha = pm.Normal('alpha', mu=0, sigma=10)
        betas = pm.Normal('betas', mu=0, sigma=10, shape=n_features)
        sigma = pm.HalfNormal('sigma', sigma=1)
        
        # Linear model
        mu = alpha + pm.math.dot(X, betas)
        
        # Likelihood
        likelihood = pm.Normal('y', mu=mu, sigma=sigma, observed=y)
        
        # Sample
        trace = pm.sample(2000, tune=1000, return_inferencedata=True)
        
    return model, trace

def plot_posterior_distributions(trace, feature_names):
    """
    Plot posterior distributions of the model parameters.
    
    Args:
        trace: PyMC trace object
        feature_names: List of feature names
    """
    # Plot posterior distributions
    az.plot_posterior(trace, var_names=['alpha', 'betas', 'sigma'])
    plt.tight_layout()
    plt.savefig('results/posterior_distributions.png')
    plt.close()
    
    # Plot trace
    az.plot_trace(trace, var_names=['alpha', 'betas', 'sigma'])
    plt.tight_layout()
    plt.savefig('results/trace_plot.png')
    plt.close()

def plot_feature_importance(trace, feature_names):
    """
    Plot feature importance based on posterior distributions.
    
    Args:
        trace: PyMC trace object
        feature_names: List of feature names
    """
    # Get posterior means and 95% credible intervals
    posterior = trace.posterior
    betas_mean = posterior.betas.mean(dim=('chain', 'draw')).values
    betas_lower = posterior.betas.quantile(0.025, dim=('chain', 'draw')).values
    betas_upper = posterior.betas.quantile(0.975, dim=('chain', 'draw')).values
    
    # Create DataFrame for plotting
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Mean': betas_mean,
        'Lower': betas_lower,
        'Upper': betas_upper
    })
    
    # Sort by absolute mean value
    importance_df['AbsMean'] = np.abs(importance_df['Mean'])
    importance_df = importance_df.sort_values('AbsMean', ascending=False)
    
    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Mean', y='Feature', data=importance_df)
    plt.errorbar(
        importance_df['Mean'],
        range(len(importance_df)),
        xerr=[importance_df['Mean'] - importance_df['Lower'],
              importance_df['Upper'] - importance_df['Mean']],
        fmt='none',
        color='black'
    )
    plt.axvline(x=0, color='red', linestyle='--')
    plt.title('Feature Importance with 95% Credible Intervals')
    plt.tight_layout()
    plt.savefig('results/feature_importance.png')
    plt.close()

def calculate_regression_metrics(model, trace, X, y):
    """
    Calculate various regression metrics for the Bayesian model.
    
    Args:
        model: PyMC model
        trace: PyMC trace object
        X (pd.DataFrame): Feature matrix
        y (pd.Series): Target variable
        
    Returns:
        dict: Dictionary containing various regression metrics
    """
    try:
        # Get posterior means of parameters
        alpha_mean = trace.posterior['alpha'].mean().values
        betas_mean = trace.posterior['betas'].mean(dim=('chain', 'draw')).values
        
        # Calculate predictions using posterior means
        y_pred = alpha_mean + np.dot(X, betas_mean)
        
        # Calculate metrics
        metrics = {
            'RMSE': np.sqrt(mean_squared_error(y, y_pred)),
            'MAE': mean_absolute_error(y, y_pred),
            'R2': r2_score(y, y_pred),
            'MAPE': np.mean(np.abs((y - y_pred) / y)) * 100
        }
        
        # Calculate Bayesian R-squared
        var_y = np.var(y)
        var_resid = np.var(y - y_pred)
        metrics['Bayesian_R2'] = 1 - (var_resid / var_y)
        
        return metrics
    
    except Exception as e:
        print(f"Error calculating metrics: {str(e)}")
        return {
            'RMSE': np.nan,
            'MAE': np.nan,
            'R2': np.nan,
            'MAPE': np.nan,
            'Bayesian_R2': np.nan
        }

def plot_metrics(metrics, save_path='results/metrics.png'):
    """
    Plot the calculated metrics in a bar chart.
    
    Args:
        metrics (dict): Dictionary of metrics to plot
        save_path (str): Path to save the plot
    """
    try:
        # Filter out NaN values
        valid_metrics = {k: v for k, v in metrics.items() if not np.isnan(v)}
        
        if not valid_metrics:
            print("No valid metrics to plot")
            return
            
        plt.figure(figsize=(10, 6))
        plt.bar(valid_metrics.keys(), valid_metrics.values())
        plt.title('Regression Model Performance Metrics')
        plt.xticks(rotation=45)
        plt.ylabel('Value')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
    except Exception as e:
        print(f"Error plotting metrics: {str(e)}") 