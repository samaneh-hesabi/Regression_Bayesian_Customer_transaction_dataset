import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns

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