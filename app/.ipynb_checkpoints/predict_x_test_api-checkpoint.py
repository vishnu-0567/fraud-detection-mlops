import pandas as pd
import requests
import time
import csv

# Load your saved X_test and y_test
X_test = pd.read_csv("creditcard.csv")  # Export from notebook if needed

API_URL = "http://127.0.0.1:8000/predict"
OUT_LOG = "stream_predictions.csv"

features = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
    'Hour', 'Day', 'UserTxnCount', 'UserAmountMean', 'UserAmountStd', 'TimeSinceLastTxn'
]
with open(OUT_LOG, mode='w', newline='') as log_file:
    writer = csv.writer(log_file)
    writer.writerow(["fraud_label", "fraud_probability", "fraud_prediction"])
    for idx, row in X_test.iterrows():
        txn = row[features].to_dict()
        try:
            resp = requests.post(API_URL, json=txn)
            result = resp.json()
            writer.writerow([y_test.iloc[idx, 0], result['fraud_probability'], result['fraud_prediction']])
            print(f"Txn {idx}: Actual={y_test.iloc[idx, 0]} | Pred={result['fraud_prediction']} | Prob={result['fraud_probability']:.4f}")
        except Exception as e:
            print(f"Failed at row {idx}: {e}")
        # time.sleep(0.05)  # Uncomment for slower streaming effect if desired
