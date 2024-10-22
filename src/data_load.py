import pandas as pd

def load_fraud_data(fraud_data_path):
    """ Load the fraud dataset. """
    try:
        fraud_data = pd.read_csv(fraud_data_path)
        print("Fraud data loaded successfully!")
        return fraud_data
    except FileNotFoundError:
        print(f"File not found: {fraud_data_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {fraud_data_path}")
        return None
    except Exception as e:
        print(f"Error loading fraud data: {e}")
        return None

def load_address_data(ip_address_path):
    """ Load the IP address dataset. """
    try:
        address_data = pd.read_csv(ip_address_path)
        print("Address data loaded successfully!")
        return address_data
    except FileNotFoundError:
        print(f"File not found: {ip_address_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {ip_address_path}")
        return None
    except Exception as e:
        print(f"Error loading address data: {e}")
        return None

def load_creditcard_data(creditcard_data_path):
    """ Load the credit card dataset. """
    try:
        creditcard_data = pd.read_csv(creditcard_data_path)
        print("Credit card data loaded successfully!")
        return creditcard_data
    except FileNotFoundError:
        print(f"File not found: {creditcard_data_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {creditcard_data_path}")
        return None
    except Exception as e:
        print(f"Error loading credit card data: {e}")
        return None
    
