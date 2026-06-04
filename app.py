import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model
model = pickle.load(open('best_big_mart_model.pkt', 'rb'))

st.title('Big Mart Sales Prediction App')

st.markdown('Enter the product and outlet details to predict sales:')

# Input fields based on the training features
item_identifier = st.number_input('Item Identifier (Encoded)', value=156)
item_weight = st.number_input('Item Weight', value=12.8)
item_fat_content = st.selectbox('Item Fat Content', options=[0, 1], format_func=lambda x: 'Low Fat' if x == 0 else 'Regular')
item_visibility = st.number_input('Item Visibility', value=0.06)
item_type = st.number_input('Item Type (Encoded)', value=4)
item_mrp = st.number_input('Item MRP', value=140.0)
outlet_identifier = st.number_input('Outlet Identifier (Encoded)', value=9)
outlet_establishment_year = st.number_input('Outlet Establishment Year', value=1999)
outlet_size = st.selectbox('Outlet Size', options=[0, 1, 2], format_func=lambda x: ['High', 'Medium', 'Small'][x])
outlet_location_type = st.selectbox('Outlet Location Type', options=[0, 1, 2], format_func=lambda x: f'Tier {x+1}')
outlet_type = st.number_input('Outlet Type (Encoded)', value=1)

if st.button('Predict Sales'):
    features = np.array([[item_identifier, item_weight, item_fat_content, item_visibility, item_type, 
                          item_mrp, outlet_identifier, outlet_establishment_year, 
                          outlet_size, outlet_location_type, outlet_type]])
    prediction = model.predict(features)
    st.success(f'Predicted Item Outlet Sales: {prediction[0]:.2f}')