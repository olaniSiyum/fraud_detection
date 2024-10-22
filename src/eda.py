# src/eda.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_univariate(df, numeric_cols, categorical_cols):
    """
    Plot univariate distributions for numeric and categorical columns.
    
    Parameters:
    df (DataFrame): The dataframe containing the data.
    numeric_cols (list): List of numeric columns to plot.
    categorical_cols (list): List of categorical columns to plot.
    """
    # Plot distributions for numeric columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

    # Plot counts for categorical columns
    for col in categorical_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col)
        plt.title(f"Count Plot of {col}")
        plt.show()

def plot_bivariate(df, target_col, numeric_cols):
    """
    Plot bivariate relationships between features and target variable.
    
    Parameters:
    df (DataFrame): The dataframe containing the data.
    target_col (str): The target variable (e.g., 'class').
    numeric_cols (list): List of numeric columns to analyze.
    """
    # Correlation heatmap for numeric columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")
    plt.show()
    
    # Boxplots for numeric columns vs. target variable
    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=target_col, y=col, data=df)
        plt.title(f"{col} vs {target_col}")
        plt.show()

if __name__ == "__main__":
    # Load cleaned fraud data
    fraud_data_cleaned = pd.read_csv("../data/processed/fraud_data_cleaned.csv")

    # Specify numeric and categorical columns
    numeric_cols = ['purchase_value', 'age']
    categorical_cols = ['browser', 'source', 'sex']
    
    # Target column
    target_col = 'class'

    # Univariate analysis
    plot_univariate(fraud_data_cleaned, numeric_cols, categorical_cols)

    # Bivariate analysis
    plot_bivariate(fraud_data_cleaned, target_col, numeric_cols)
