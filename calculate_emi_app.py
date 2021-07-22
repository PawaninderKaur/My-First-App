# Write the code for creating the EMI calculator app
import streamlit as st
def calculated_emi(p,n,r):
  emi = p*(r/100) * (1+r/100)**n / ((1+r/100)**n -1)
  st.write("EMI calculated as: ",round(emi,3))
st.title("EMI Calculator App")

principal = st.slider("Loan Amount",1000.0,100000.0)
tenure = st.slider("Tenure in Years",1,30)
roi = st.slider("Interest Rate (%P.A)",1,15)
n = tenure*12
r = roi/12
if st.button("Calculate"):
  calculated_emi(principal,n,r)