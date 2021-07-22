# Write the code for creating the Improvised EMI calculator app
import streamlit as st

def calculate_emi(p,n,r):
  emi = p*(r/100) * (1+r/100)**n / ((1+r/100)**n -1)
  st.write("EMI calculated as: ",round(emi,3))
st.title("EMI Calculator App")
def calculate_overstanding_balance(p,n,r,m):
  balance = p*(1 + r/100)**n - (1+r/100)**m / ((1+r/100)**n -1)
  st.write("Outstanding Loan Balance Calculated as: ",round(balance,3))
st.title("Outstanding Loan Balance App")
principal = st.slider("Loan Amount",1000.0,100000.0)
tenure = st.slider("Tenure in Years",1,30)
roi = st.slider("Interest Rate (%P.A)",0,15)
m = st.slider("Outstanding Loan Balance in Months",1,12)
n = tenure*12
r = roi/12
if st.button("Calculate"):
  calculate_emi(principal,n,r)
elif st.button("Balance"):
  calculate_overstanding_balance(p,n,r,m)