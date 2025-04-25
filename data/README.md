<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">Data Directory Documentation</div>

This directory contains all data files used in the Bayesian Regression analysis of customer transaction data.

# 1. Directory Structure

## 1.1 raw/
Contains the original, unprocessed data:
- `original_dataset.csv`: The initial dataset before any preprocessing

## 1.2 processed/
Contains cleaned and processed data:
- `cleaned_dataset.csv`: The preprocessed dataset ready for analysis

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

# 3. Data Processing Pipeline
1. Raw data is loaded from `raw/original_dataset.csv`
2. Data preprocessing is performed (cleaning, transformation, etc.)
3. Processed data is saved to `processed/cleaned_dataset.csv`
4. The processed data is used for model training and analysis

# 4. Data Version Control
- Original data files should never be modified
- All data transformations should be documented
- Processed data can be regenerated from the original data using the preprocessing pipeline 