import pandas as pd
def fill_values(df):
    df.loc[df['Loan_Status'] == 'Y', 'Credit_History'] = df.loc[df['Loan_Status'] == 'Y', 'Credit_History'].fillna(1.0)
    df.loc[df['Loan_Status'] == 'N', 'Credit_History'] = df.loc[df['Loan_Status'] == 'N', 'Credit_History'].fillna(0)
    df.loc[(df['ApplicantIncome'] < 3584.0), 'Gender'] = df.loc[(df['ApplicantIncome'] < 3584.0), 'Gender'].fillna('Female')
    df.loc[(df['ApplicantIncome'] > 3583.0), 'Gender'] = df.loc[(df['ApplicantIncome'] > 3583.0), 'Gender'].fillna('Male')
    df.Married = df.Married.fillna('Yes')
    df.loc[(df['Married'] == 'Yes'), 'Dependents'] = df.loc[(df['Married'] == 'Yes'), 'Dependents'].fillna(2)
    df.loc[(df['Married'] == 'No'), 'Dependents'] = df.loc[(df['Married'] == 'No'), 'Dependents'].fillna(0)
    df.Self_Employed = df.Self_Employed.fillna('No')
    df.LoanAmount = df.LoanAmount.fillna(df.LoanAmount.mean())
    df.Loan_Amount_Term = df.Loan_Amount_Term.fillna(360.0)
    df.Dependents = df.Dependents.astype(str)
    return df