import pandas as pd

df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("Original Shape:", df.shape)

df = df.dropna()

print("After Cleaning:", df.shape)

df.to_csv(
    "data/processed/cleaned.csv",
    index=False
)

print("Preprocessing completed")
