import pandas as pd
import requests
import time
import csv

# Config
API_URL = "http://127.0.0.1:8000/predict"
DATA_PATH = "data/X_test.csv"
OUTPUT_LOG = "stream_predictions.csv"

# Load your data and set up for streaming
df = pd.read_csv(DATA_PATH)
features = [
    'Unnamed: 0', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount',
    'Hour', 'Day', 'UserTxnCount', 'UserAmountMean', 'UserAmountStd', 'TimeSinceLastTxn'
]


# Optionally, limit to a small set for demo:
# df = df.sample(100, random_state=1)

with open(OUTPUT_LOG, mode='w', newline='') as log_file:
    writer = csv.writer(log_file)
    writer.writerow(["row_index", "fraud_label", "fraud_probability", "fraud_prediction"])
    for i, row in df.iterrows():
        txn = row[features].to_dict()
        try:
            resp = requests.post(API_URL, json=txn)
            result = resp.json()
            writer.writerow([i, row["Class"], result["fraud_probability"], result["fraud_prediction"]])
            print(f"Txn {i}: Actual={row['Class']} | Pred={result['fraud_prediction']} | Prob={result['fraud_probability']:.4f}")
        except Exception as e:
            print(f"Failed at row {i}: {e}")
        time.sleep(0.1)  # remove or adjust sleep for faster/slower streaming
        
