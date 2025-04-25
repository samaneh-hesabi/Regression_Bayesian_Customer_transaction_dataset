<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Data Documentation</div>

## 1. Data Directory Structure
This directory contains all data-related files for the Bayesian Regression Analysis project.

## 1.1 Directory Structure
```
data/
├── raw/              # Original dataset
│   └── original_dataset.csv  # Raw customer transaction data
└── processed/        # Cleaned and processed data
    └── processed_data.csv    # Preprocessed dataset ready for analysis
```

## 1.2 Dataset Description
The customer transaction dataset contains the following features:

### 1.2.1 Raw Data (`raw/original_dataset.csv`)
- Transaction amount
- Customer demographics
- Time-based features
- Product categories
- Payment methods

### 1.2.2 Processed Data (`processed/processed_data.csv`)
- Standardized numerical features
- Encoded categorical variables
- Engineered features
- Cleaned and validated data

## 1.3 Data Processing Pipeline
1. Data loading from `raw/original_dataset.csv`
2. Data cleaning and validation
3. Feature engineering
4. Data standardization
5. Saving processed data to `processed/processed_data.csv`

## 1.4 Data Usage
The processed data is used by:
- `src/data_loader.py` for loading and preprocessing
- `src/bayesian_regression.py` for model training
- `src/main.py` for the analysis pipeline

## 1.5 Data Privacy
- All customer identifiers have been anonymized
- Sensitive information has been removed or masked
- Data is used only for analysis purposes

# 2. Data Description

## 2.1 Original Dataset
The raw dataset contains customer transaction information including:
- Transaction amounts
- Customer demographics
- Transaction timestamps
- Product categories
- Other relevant features

## 2.2 Processed Dataset
The cleaned dataset includes:
- Removed missing values
- Standardized features
- Encoded categorical variables
- Normalized numerical features
- Feature engineering results

## 2.3 Data Dictionary

| Column Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| Customer_ID | String (UUID) | Unique identifier for each customer | 3f524cd7-ff15-4aad-a81e-b0e4dc0753a9 |
| Name | String | Customer's full name | Jacob Perez |
| Age | Integer | Customer's age | 51 |
| Gender | String | Customer's gender | Female |
| Email | String | Customer's email address | beckerkim@gmail.com |
| Phone_Number | String | Customer's contact number | 804-453-8707 |
| Address | String | Customer's complete address | 45596 Joann Causeway, Lake Alexmouth, NM 33597 |
| Purchase_Amount | Float | Amount spent in the transaction | 164.99 |
| Last_Purchase_Date | Date | Date of the most recent purchase | 2021-01-05 |
| Preferred_Payment_Method | String | Customer's preferred payment method | Credit Card |
| Feedback_Score | Integer | Customer satisfaction score (1-5) | 1 |
| Loyalty_Member | Boolean | Whether customer is a loyalty program member | No |

# 3. Data Version Control
- Original data files should never be modified
- All data transformations should be documented
- Processed data can be regenerated from the original data using the preprocessing pipeline 