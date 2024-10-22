# tests/test_data_processing.py

import unittest
import os
from src.data_processing import load_fraud_data

class TestDataProcessing(unittest.TestCase):

    def test_load_fraud_data(self):
        fraud_data_path = "../data/raw/Fraud_Data.csv"
        ip_address_path = "../data/raw/IpAddress_to_Country.csv"
        creditcard_data_path = "../data/raw/creditcard.csv"
        
        fraud_data, ip_address_data, creditcard_data = load_fraud_data(fraud_data_path, ip_address_path, creditcard_data_path)
        
        self.assertIsNotNone(fraud_data, "Failed to load Fraud Data")
        self.assertIsNotNone(ip_address_data, "Failed to load IP Address Data")
        self.assertIsNotNone(creditcard_data, "Failed to load Credit Card Data")

if __name__ == "__main__":
    unittest.main()
