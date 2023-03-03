import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_log = np.log(X[['LoanAmount', 'total_income']])
        X.drop(['LoanAmount', 'total_income'], axis=1, inplace=True)
        return pd.concat([X, X_log], axis=1)

with open('loan_XGBClass_pipe.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Loan Eligibility Predictor')
st.write('Complete this short form for an instant prediction!')

# create our form for the customer/user to fill out
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
loan_amount = st.number_input('Loan Amount', min_value=10, max_value=1000, value=150, step=1)
loan_term = st.number_input('Loan Amount Term', min_value=12, max_value=480, value=360, step=1)
credit_history = st.selectbox('Credit Standing', ['My credit is bad', 'My credit is good'])
property_area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])
total_income = st.number_input('Total Income', min_value=0, max_value=100000, value=5000, step=1)
responses = ['It may be difficult to get approved.','We can get you approved!']

if st.button('Make Prediction'):
    # prep inputted data
    credit_convert = {'My credit is bad':0,'My credit is good':1}
    credit_history = credit_convert[credit_history]
    input_data = {
    'Gender': [gender],
    'Married': [married],
    'Dependents': [dependents],
    'Education': [education],
    'Self_Employed': [self_employed],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area],
    'total_income': [total_income]
    }
    input_df = pd.DataFrame(input_data)

    # make and display our prediction
    prediction = model.predict(input_df)
    st.write(responses[prediction[0]])

    # display nice stock images and lead conversion attempt based on output.
    if prediction[0] == 0:
        st.image('https://cdn.discordapp.com/attachments/1046174858372972594/1081039612065103922/lesbian-couple-buy-new-house-agent-giving-cottage-keys-female-characters-holding-hands-homosexual-family-buying-real-estate-property-mortgage-loan-home-purchase-line-art-vector-illustration_107791-11139.png',
                 "That's what we're here for! Talk to one of our consultants for free today by dialing 123-321-1234")
    else:
        st.image('https://cdn.discordapp.com/attachments/1046174858372972594/1081038502315163648/happy-man-girl-and-dogs-in-front-of-house.png',
                 'Call us at 123-321-1234 to get one step closer to your dream home!')