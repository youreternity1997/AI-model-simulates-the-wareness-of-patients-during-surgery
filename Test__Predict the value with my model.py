from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np
import pandas as pd
import joblib
import pickle

# 定義一個以 Pandas 讀入資料的函式
def load_document_data():
    csv_path = "./NTUH_OR69_Raw_Data_9_test_surgerys.csv"
    return pd.read_csv(csv_path)
anesthesia_test_set_original = load_document_data()
anesthesia_test_set_original = anesthesia_test_set_original.replace([-1,'-1','--'],[np.nan,np.nan,np.nan])
anesthesia_test_set_original = anesthesia_test_set_original.fillna(method='bfill')
print(anesthesia_test_set_original.head())

class process_data(BaseEstimator, TransformerMixin): 
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X, y=None):
        X_copy = X.copy()
        del X_copy ['Time']
        del X_copy ['ABP_Dia']
        del X_copy ['ABP_Sys']
        del X_copy ['ABP_Mean']
        del X_copy ['RESP']
        del X_copy ['SR']
        del X_copy ['MAC']
        del X_copy ['Awareness']
        del X_copy ['A_Doctor_value']    
        del X_copy ['B_Doctor_value']  
        del X_copy ['C_Doctor_value']  
        del X_copy ['Average_doctor_value']  
        return X_copy

if __name__ == '__main__':
    my_model_loaded = joblib.load("./my_model.pkl")
    my_model_loaded_predict = my_model_loaded.predict(anesthesia_test_set_original[-1:])[0]
    print('Final data=', anesthesia_test_set_original[-1:])
    print('BIS=', anesthesia_test_set_original[-1:]['BIS'])
    print('predicted value=', my_model_loaded_predict)

