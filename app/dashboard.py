
import streamlit as st
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

st.title("Live Fraud Detection Dashboard")

DATA_PATH = r".\stream_predictions.csv"

@st.cache_data(ttl=30)  # refresh every 30s
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.write(f"Total Transactions Scored: {len(df)}")
st.write(f"Frauds Detected by Model: {df['fraud_prediction'].sum()}")

st.line_chart(df["fraud_probability"])

st.write("Sample Predictions:")
st.dataframe(df.tail(15))

if "fraud_label" in df.columns:
    st.write("Confusion matrix:")
    cm = confusion_matrix(df["fraud_label"], df["fraud_prediction"])
    st.write(cm)
    st.write("Classification report:")
    st.text(classification_report(df["fraud_label"], df["fraud_prediction"]))
    rocauc = roc_auc_score(df["fraud_label"], df["fraud_probability"])
    st.write(f"ROC-AUC: {rocauc:.4f}")
