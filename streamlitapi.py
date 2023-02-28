import streamlit as st
import pandas as pd

#model = pickle.load(open('C:/Users/hp/Desktop/ML Project/random_forest_model.pkl', 'rb'))

import joblib

model = joblib.load('modeltobeused.sav') # Load your model using joblib


def main():
    st.title('Car Pricing Prediction Solution')

    #input varibles
    Year = st.text_input('Year')
    Present_Price = st.text_input('Present_Price')
    Kms_Driven = st.text_input('Kms_Driven')
    Owner = st.text_input('Owner')
    Fuel_Type_Diesel = st.text_input('Fuel_Type_Diesel')
    Fuel_Type_Petrol = st.text_input('Fuel_Type_Petrol')
    Seller_Type_Individual = st.text_input('Seller_Type_Individual')
    Transmission_Manual = st.text_input('Transmission_Manual')

    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[Year, Present_Price, Kms_Driven, 
                                         Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output = round(makeprediction[0],2)
        st.sucess('You Can Sell Your Car for {}'.format(output))

    if __name__ =='__main__':
        main()