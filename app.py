import streamlit as st
import pandas as pd

# -------------------------------
# App Title
# -------------------------------
st.title("ATM Cash Refill Optimization Prediction")
st.write("This application predicts whether an ATM needs a cash refill based on input details.")

# -------------------------------
# User Inputs
# -------------------------------
st.header("Enter ATM Details")

amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
currentBalance = st.number_input("Current ATM Balance", min_value=0.0, value=50000.0)
hour = st.slider("Hour of Transaction", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# -------------------------------
# Simple Logic-based Prediction
# -------------------------------
if st.button("Predict Refill Requirement"):

    # Simple condition (demo logic)
    if currentBalance < 20000 or amount > 10000:
        st.error("🚨 ATM Cash Refill Required")
    else:
        st.success("✅ ATM Cash Level is Sufficient")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.write("ATM Cash Refill Prediction System | Streamlit Demo")
