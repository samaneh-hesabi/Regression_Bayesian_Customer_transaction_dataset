<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Bayesian Regression Analysis on California Housing Dataset</div>

## 1. Project Overview
This project implements a Bayesian linear regression analysis on the California Housing dataset. It provides a probabilistic approach to understanding the relationships between various housing features and median house values, offering uncertainty estimates and posterior distributions for model parameters.

## 1.1 Dataset Description
The project uses the California Housing dataset, which contains the following features:
- MedInc: Median income in block group
- HouseAge: Median house age in block group
- AveRooms: Average number of rooms per household
- AveBedrms: Average number of bedrooms per household
- Population: Block group population
- AveOccup: Average number of household members
- Latitude: Block group latitude
- Longitude: Block group longitude

Target Variable: MedHouseVal (Median house value)

## 1.2 Source Code Structure

### 1.2.1 data_loader.py
This module handles all data-related operations:
- `load_california_data()`: Loads and preprocesses the California Housing dataset
  - Loads raw data from scikit-learn
  - Standardizes features using StandardScaler
  - Returns feature matrix and target variable
- `get_feature_descriptions()`: Provides detailed descriptions of dataset features

### 1.2.2 bayesian_regression.py
Implements the core Bayesian regression analysis:
- `build_bayesian_regression_model()`: Creates and runs the Bayesian linear regression model
  - Defines priors for model parameters
  - Implements the linear model
  - Performs MCMC sampling
- `plot_posterior_distributions()`: Visualizes posterior distributions of model parameters
- `plot_feature_importance()`: Creates feature importance plots with credible intervals
- `calculate_regression_metrics()`: Computes various regression metrics
  - RMSE, MAE, R², MAPE
  - Bayesian R²
- `plot_metrics()`: Visualizes model performance metrics

### 1.2.3 main.py
Orchestrates the entire analysis pipeline:
- Creates results directory
- Loads and preprocesses data
- Builds and runs the Bayesian model
- Calculates and displays metrics
- Generates visualizations
- Handles error cases

## 1.3 Usage
To run the analysis:
```bash
python main.py
```

The script will:
1. Load and preprocess the data
2. Build the Bayesian regression model
3. Generate visualizations
4. Save results in the 'results' directory

## 1.4 Dependencies
The project requires the following Python packages:
- pandas: Data manipulation and analysis
- numpy: Numerical computations
- pymc: Bayesian modeling and MCMC sampling
- scikit-learn: Data preprocessing and metrics
- matplotlib: Plotting
- seaborn: Statistical visualizations
- arviz: Bayesian analysis visualization

## 1.5 Output
The analysis generates the following outputs in the `results` directory:
- `posterior_distributions.png`: Posterior distributions of model parameters
- `trace_plot.png`: MCMC trace plots for parameter convergence
- `feature_importance.png`: Feature importance with 95% credible intervals
- `metrics.png`: Model performance metrics visualization

## 1.6 Model Details
The Bayesian regression model includes:
- Normal priors for intercept (alpha) and coefficients (betas)
- Half-Normal prior for error term (sigma)
- MCMC sampling with 2000 samples and 1000 tuning steps
- Posterior analysis using ArviZ

## 1.7 Error Handling
The code includes comprehensive error handling:
- Data loading and preprocessing errors
- Model building and sampling errors
- Metric calculation errors
- Plotting errors
- Directory creation errors 