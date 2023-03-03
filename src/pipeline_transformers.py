from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
import math

class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_log = np.log(X[['LoanAmount', 'total_income']].astype(float))
        X.drop(['LoanAmount', 'total_income'], axis=1, inplace=True)
        return pd.concat([X, X_log], axis=1)