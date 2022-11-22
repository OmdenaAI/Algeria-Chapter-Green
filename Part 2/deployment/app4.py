import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("models/3_RecommendationSystems/rf_model.h5", "rb"))

def app():
    st.title("🌱 Omdena Algeria Chapter 🌱")
    st.write("\n")
    st.write("\n")
    st.markdown("Collaborate, Learn, Build, Grow")
    st.write("\n")
    st.title("Recommendation System for Water Management")
    
    
    croplist = ["Wheat", "Ground Nuts", "Garden flowers", "Maize", "Paddy", "Potato","Pulse", "Suger Cane", "Coffee"]
    crop_type = st.selectbox("Crop Type", croplist)
    crop_days = st.number_input('Number of days passed after the crop was sown')
    soil_moisture = st.number_input('Current Soil Moisture (DHT11 Reading)')
    temp = st.number_input('Current Temperature (°C)')
    humid = st.number_input('Current Humidity (%)')
    submit = st.button("Submit")
    if submit:
        param1 = croplist.index(crop_type) + 1
        param2 = int(crop_days)
        param3 = soil_moisture
        param4 = temp
        param5 = humid

        op = model.predict(np.array([param1, param2, param3, param4, param5]).reshape(1, -1))
        if op[0] == 0:
            st.success('Your crop is irrigated!', icon="✅")
        else:
            st.warning('Your crop needs irrigation!', icon="⚠️")
