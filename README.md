# fraud-detection-mlops
End-to-end credit card fraud detection ML pipeline with real-time scoring and monitoring
# End-to-End Credit Card Fraud Detection ML Pipeline 🚀

## Overview

A fully production-style machine learning solution for detecting credit card fraud in real time. This project features in-depth EDA, feature engineering, model training with XGBoost, REST API deployment using FastAPI, a transaction streaming simulator, and a live monitoring dashboard with Streamlit. It follows best practices for MLOps and is perfect as a portfolio centerpiece.

---

## Project Structure

- `notebooks/` – EDA & feature engineering notebooks
- `models/` – Saved trained models
- `app/api.py` – FastAPI app serving model predictions
- `simulate_stream.py` / `predict_x_test_api.py` – Scripts for generating and logging predictions via API
- `X_test.csv` – Exported test features for API batch prediction
- `stream_predictions.csv` – Log of predictions for dashboarding
- `app/dashboard.py` – Streamlit dashboard for live monitoring
- `screenshots/` – Project and result screenshots

---

## Quickstart ⚡

1. **Clone & Install**
    ```
    git clone [(https://github.com/vishnu-0567/Transaction-Fraud-Detection)]
    cd fraud-detection-mlops
    pip install -r requirements.txt
    ```

2. **Train Model & Export Artifacts**
    - Use notebooks for data prep, feature engineering, and model training.
    - Export final model to `models/fraud_xgb.joblib`.

3. **Serve Model as API**
    ```
    uvicorn app.api:app --reload
    ```

4. **Simulate Transactions or Batch-Predict Test Set (API Method)**
    - Ensure `X_test.csv` includes all features the model expects.
    ```
    python predict_x_test_api.py
    ```
    - Predictions are logged to `stream_predictions.csv`.

5. **Run Streamlit Dashboard**
    ```
    streamlit run app/dashboard.py
    ```
    - Open `http://localhost:8501` to see real-time model results and metrics.

---

## Example API Usage

**POST /predict**
{
"V1": -1.35980, "V2": -0.07, ..., "Amount": 149.62, "Hour": 0, "Day": 0, "UserTxnCount": 0, ...
}

text
**Sample Response**
{
"fraud_probability": 0.00005,
"fraud_prediction": 0
}

text

---

## Screenshots

![Dashboard Screenshot](screenshots/dashboard_sample.png)
![API Docs](screenshots/api_docs.png)
![SHAP Feature Importances](screenshots/shap_importance.png)

---

## Results

- **ROC-AUC:** 0.98+
- **Recall (fraud):** 0.83
- **Precision (fraud):** 0.80
- **Streaming and API-based scoring successful**
- **Live dashboard for monitoring and performance review**

---

## How to Extend

- Add email/SMS alerting for fraud spikes or model drift
- Integrate retraining triggers when performance drops
- Deploy API on cloud platform (AWS, Azure, GCP)
- CI/CD: automate model rebuild and redeployment

---

## Tech Stack

Python, pandas, scikit-learn, XGBoost, imbalanced-learn, FastAPI, Streamlit, SHAP

---

## License

MIT

---

*project by [Vishnu Vardhan].*
