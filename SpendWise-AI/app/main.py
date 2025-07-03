
import streamlit as st
from app.utils import clean_data, categorize_transactions
from app.visuals import generate_dashboard
from app.prompts import generate_summary

st.set_page_config(page_title="SpendWise AI", layout="wide")

st.title("💸 SpendWise AI – Your Personal Finance Copilot")

uploaded_file = st.file_uploader("Upload your bank/expense CSV file", type=["csv"])

if uploaded_file:
    df = clean_data(uploaded_file)
    df = categorize_transactions(df)
    st.subheader("📊 Your Spending Breakdown")
    generate_dashboard(df)
    
    with st.expander("📬 Weekly AI Summary"):
        summary = generate_summary(df)
        st.markdown(summary)
