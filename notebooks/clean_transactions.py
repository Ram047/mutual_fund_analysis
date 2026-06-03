import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Fix date format
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Amount must be positive
df = df[df["amount_inr"] > 0]

# Valid KYC values
valid_kyc = ["Verified", "Pending"]
df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned successfully")
print(df.shape)