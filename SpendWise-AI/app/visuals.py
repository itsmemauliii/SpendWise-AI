
import streamlit as st
import plotly.express as px

def generate_dashboard(df):
    fig = px.pie(df, names="Category", values="Amount", title="Spending by Category")
    st.plotly_chart(fig, use_container_width=True)

    trend = df.groupby(df["Date"].dt.to_period("W"))["Amount"].sum().reset_index()
    trend["Date"] = trend["Date"].astype(str)
    fig2 = px.line(trend, x="Date", y="Amount", title="Weekly Spending Trend")
    st.plotly_chart(fig2, use_container_width=True)
