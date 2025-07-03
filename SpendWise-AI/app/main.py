
from utils import clean_data, categorize_transactions
from visuals import generate_dashboard
from prompts import generate_summary

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
        
st.markdown("---")
st.markdown("## 💬 Share Your Feedback")
st.markdown("Help us improve SpendWise AI by sharing your thoughts 💡")
st.markdown("[📝 Fill out the feedback form here](https://forms.gle/zsWrxDVqo87QKfzFA)")
