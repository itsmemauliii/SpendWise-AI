
import pandas as pd

def clean_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.lower()
    df = df.rename(columns={"amount": "Amount", "description": "Description"})
    df["Date"] = pd.to_datetime(df["date"], errors="coerce")
    df.dropna(subset=["Amount", "Description"], inplace=True)
    return df

def categorize_transactions(df):
    categories = {
        "swiggy|zomato|restaurant": "Food & Dining",
        "uber|ola|fuel": "Transport",
        "netflix|spotify|prime": "Subscriptions",
        "flipkart|amazon|myntra": "Shopping"
    }
    df["Category"] = "Other"
    for pattern, cat in categories.items():
        df.loc[df["Description"].str.contains(pattern, case=False, na=False), "Category"] = cat
    return df
