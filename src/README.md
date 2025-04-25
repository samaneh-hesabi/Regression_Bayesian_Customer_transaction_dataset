<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Source Code Documentation</div>

This directory contains the main source code files for the Bayesian Regression analysis of customer transaction data.

# 1. Files Overview

## 1.1 main.py
The main entry point of the application. This script:
- Orchestrates the data loading, preprocessing, and model training pipeline
- Handles the execution flow of the entire analysis
- Generates and saves visualizations of the results

## 1.2 data_loader.py
Contains functions for data handling:
- Loading raw data from CSV files
- Data preprocessing and cleaning
- Feature engineering
- Data validation and integrity checks

## 1.3 bayesian_regression.py
Implements the core Bayesian regression model:
- Defines the probabilistic model structure
- Implements MCMC sampling
- Handles model inference and prediction
- Contains functions for model evaluation and diagnostics

## 1.4 __init__.py
Marks this directory as a Python package.

# 2. Usage
To run the analysis:
1. Ensure all dependencies are installed (see root requirements.txt)
2. Run `python main.py` from the project root directory
3. Results will be saved in the `results/` directory

# 3. Dependencies
All required dependencies are listed in the root `requirements.txt` file. 