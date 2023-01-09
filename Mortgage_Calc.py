import streamlit as st
import numpy_financial as np
from datetime import datetime



st.set_page_config(page_title="Mortgage Payment Calculator", page_icon=":tada:", layout="centered")

#----Header Section ----

st.title("Mortgage Payment Calculator")
st.write("[Mortgage Rates!](https://www.nerdwallet.com/mortgages/mortgage-rates)")
st.markdown("""---""")


with st.container():
   purchasePrice = st.number_input('Purchase Price $$', value=500000, min_value=1, max_value=None, step=25000, key='pur_price')         # Input purchase price
   st.write(f'${purchasePrice:,.2f}')
   dwnPmt_pct = st.number_input('Down Pmt %', value=0.2, min_value=0.0, max_value=None, step=0.025, key='dwn_pmtpct')                   # Input down payment %
   st.write(f'{dwnPmt_pct:.2%}')                                                                                                        # Write down payment as %
   dwnPmt = purchasePrice * dwnPmt_pct                                                                                                  # Calc down payment
   dwnPmnt = st.number_input('$$ Down', value=dwnPmt, key='dwn_pmnt')                                                                   # Print down payment in $$
   st.write(f'${dwnPmnt:,.2f}')
   lnAmt = purchasePrice - dwnPmnt                                                                                                      # Calc loan amount
   loanAmt = st.number_input('Loan Amt $', lnAmt, key='lon_amnt')                                                                       # Print the loan amount
   st.write(f'${loanAmt:,.2f}')
   intRate = st.number_input('Annual Interest rate', value=0.065, min_value=None, max_value=None, step=0.0025, key='int_rate')           # Input Loan Interest Rate
   st.write(f'{intRate:.2%}')                                                                                                             # Write Interest rate as %
   loanTerm = st.number_input('Loan term (years)', value=30, key='loan_term')                                                             # Input term of loan
   numPmt = st.number_input('Number of Payments per year', value=12, key='num_pmt')                                                       # Input number of payments per year
   totPmt = st.number_input('Total Number of Payments',loanTerm * numPmt, key='tot_pmt')                                                  # Input total number of payments
   
   mrgtPmt = np.pmt(intRate/numPmt, totPmt, lnAmt)                                                                                        # Calc the mortgage payment
   totInterest = lnAmt - (-mrgtPmt*totPmt)                                                                                                # Calc total interest
    
   st.write(f'Mortgage Payment (Principal + Interest):   ${-mrgtPmt:,.2f}')                                                               # Write mortgage payment
   st.write(f'Sum of Payments:   ${-mrgtPmt*totPmt:,.2f}')                                                                                # Write Sum of Mortgage Payments
   st.write(f'Total Interest Cost:   ${-totInterest:,.2f}')                                                                               # Write Total Interest Payments

   st.markdown("""---""")                                                                                                                 # Create Markdown Line on Page

with st.expander("Calculate PITI"):                                                                                                       # Initialize PITI Payment Expander
    st.write(f'Mortgage Payment:   ${-mrgtPmt:,.2f}')                                                                                     # Write Monthly Mortgate Principal + Interest
    
    prpTaxes = st.number_input('Annual Property Taxes', value=5000.00, min_value=0.00, max_value=None, step=0.10, key='prp_tax')          # Input Annual Taxes
    st.write(f'Annual Property Taxes: ${prpTaxes:,.2f}')                                                                                  # Write Annual Taxes Expressed as Dollars
    
    prpInsurance = st.number_input('Annual Property Insurance', value=1000.00, min_value=0.00, max_value=None, step=0.10, key='prp_ins')  # Input Annual Taxes
    st.write(f'Annual Property Insurance: ${prpInsurance:,.2f}')                                                                          # Write Annual Insurance Expressed as Dollars

    prpHOA = st.number_input('Annual HOA Dues', value=0.00, min_value=0.00, max_value=None, step=0.10, key='prp_hoa')                      # Input Annual HOA
    st.write(f'Annual HOA Dues: ${prpHOA:,.2f}')                                                                                           # Write Annual HOA Dues Expressed as Dollars

    prpTaxesMo = prpTaxes / 12                                                                                                             # Calc Monthly Taxes
    prpInsuranceMo = prpInsurance / 12                                                                                                     # Calc Monthly Insurance
    prpHOAMo = prpHOA / 12                                                                                                                 # Calc Monthly HOA Dues

    st.markdown("""---""")
    st.subheader('-- Summary --')
    st.write(f'Mortgage Payment (Principal + Interest):   ${-mrgtPmt:,.2f}')
    st.write(f'Annual Property Taxes: ${prpTaxesMo:,.2f}')
    st.write(f'Annual Property Insurance: ${prpInsuranceMo:,.2f}')
    st.write(f'Annual HOA Dues: ${prpHOAMo:,.2f}')

    moPITI = -mrgtPmt + prpTaxesMo + prpInsuranceMo + prpHOAMo

    st.write(f'Total Monthly PITI Payment : ${moPITI:,.2f}')

with st.sidebar:
    st.write(f'Mortgage Payment:   ${-mrgtPmt:,.2f}')                                                                                     # Write Monthly Mortgate Principal + Interest  
    st.write(f'Annual Property Taxes: ${prpTaxes:,.2f}')                                                                                  # Write Annual Taxes Expressed as Dollar
    st.write(f'Annual Property Insurance: ${prpInsurance:,.2f}')                                                                          # Write Annual Insurance Expressed as Dollar
    st.write(f'Annual HOA Dues: ${prpHOA:,.2f}')                                                                                           # Write Annual HOA Dues Expressed as Dollars                                                                                                         # Calc Monthly HOA Dues

    st.markdown("""---""")
    st.subheader('-- Summary --')
    st.write(f'(Principal + Interest):   ${-mrgtPmt:,.2f}')
    st.write(f'Annual Property Taxes: ${prpTaxesMo:,.2f}')
    st.write(f'Annual Property Insurance: ${prpInsuranceMo:,.2f}')
    st.write(f'Annual HOA Dues: ${prpHOAMo:,.2f}')

    st.write(f'Total Monthly PITI Payment : ${moPITI:,.2f}')