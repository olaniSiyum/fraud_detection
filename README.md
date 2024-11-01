# fraud_detection_for_e-commerce_and_bank_transactions

This project focuses on building, evaluating, and explaining machine learning models to detect fraudulent transactions. The project is structured into three main tasks:

1. Model Training and Evaluation
2. Model Selection
3. Model Explainability using SHAP and LIME

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Data](#data)
4. [Installation](#installation)
5. [Notebook Structure](#notebook-structure)
6. [Model Explainability](#model-explainability)
7. [Results](#results)

---

## Project Overview

This project aims to accurately classify transactions as fraudulent or non-fraudulent using a machine learning model. The dataset used in this project is highly imbalanced, as fraud cases are rare compared to legitimate transactions. We use techniques like Random Forest and Gradient Boosting for classification and employ SHAP (Shapley Additive Explanations) and LIME (Local Interpretable Model-agnostic Explanations) to explain the models' predictions.

---

## Requirements

- Python 3.8 or higher
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `shap`, `lime`

---

## Data

The project uses Three main datasets:

- **Credit Card Data**: Contains credit card transaction records for fraud detection.
- **Fraud Data**: An additional fraud-focused dataset to improve model generalizability.
- **IPAddress**:

---

## Installation

To set up the environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/olaniSiyum/fraud_detection.git
   cd fraud_detection
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Install SHAP and LIME for model explainability:
   ```bash
   pip install shap lime
   ```

---

## Notebook Structure

The project consists of the following main notebooks:

1. **eda.ipynb**:
   - Load the data
   - data cleaning
   - explatory analysis
2. **model_building_and_training.ipynb**:

   - Loads and preprocesses the data.
   - Trains and evaluates several models, including Random Forest and Gradient Boosting.
   - Logs metrics such as accuracy, precision, recall, and AUC-ROC for each model.

3. **model_selection.ipynb**:

   - Compares Random Forest and Gradient Boosting models based on evaluation metrics.
   - Selects the best-performing model based on AUC-ROC and F1-score for further analysis.

4. **model_explainability.ipynb**:
   - Uses SHAP and LIME to interpret the selected model's predictions.
   - Generates visualizations for feature importance, dependence, and local explanations for individual predictions.

---

## Model Explainability

### Using SHAP for Model Interpretation

SHAP values provide a unified measure of feature importance, explaining the contribution of each feature to the prediction.

#### Steps to Use SHAP:

1. **Summary Plot**: Shows the global importance of features across all predictions.
2. **Force Plot**: Visualizes the contribution of each feature for an individual prediction.
3. **Dependence Plot**: Shows the relationship between a feature and the model's output.

Code examples for using SHAP:

```python
import shap
shap.initjs()

# Initialize the SHAP explainer for the Random Forest model
explainer = shap.TreeExplainer(random_forest_model)
shap_values = explainer.shap_values(X_test_creditcard)

# Generate SHAP Summary Plot
shap.summary_plot(shap_values, X_test_creditcard)

# Generate SHAP Force Plot for an individual prediction
shap.force_plot(explainer.expected_value[1], shap_values[1][0], X_test_creditcard.iloc[0])
```
