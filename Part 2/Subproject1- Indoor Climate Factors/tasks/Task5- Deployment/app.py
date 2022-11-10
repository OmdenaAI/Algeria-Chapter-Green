
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import tensorflow as tf
from tensorflow import keras as tfk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('Agg')
# matplotlib.use('TKAgg')


st.title('Greenhouse Climate Forecast')


def prediction(file):
    
    #get data from user
    future_data = pd.read_csv(file)    

    #below dataframe containes X_max & X_min of each feature of the Entire dataset during training 
    #which will be used for normalizing the values
    #it also contains ideal upper & lower limt values
    
    parameter_df = pd.DataFrame({
    'X_max' : [50.0, 100.0, 477.0, 1473.0, 45.4, 36.0],
    'X_min' : [0.7, 21.0, 0.0, 188.0, 8.2, 0.0],
    'U_limit' : [27.0, 75.0, 500.0, 1000.0, 25.0, 20.0],
    'L_limit' : [18.0, 65.0, 400.0, 400.0, 20.0, 10.0],
    'parameters' : ['indoor_temp', 'indoor_humidity', 'indoor_lighting', 'indoor_CO2', 'soil_temp', 'soil_moisture']   
    })

    parameter_df = parameter_df.set_index('parameters')

    #Preprocessing future data
    future_data['datetime'] = pd.to_datetime(future_data['date'] + ' ' + future_data['time'])
    future_data['datetime'] = pd.to_datetime(future_data['datetime'], format='%d.%m.%Y %H:%M:%S')
    future_data = future_data.drop(['date', 'time'], axis = 1)
    future_data = future_data.set_index('datetime')    

    #Normalizing future data
    future = (future_data-parameter_df['X_min'])/(parameter_df['X_max']-parameter_df['X_min'])
    future = np.expand_dims(future, axis=0)

    #importing model:
    model = tfk.models.load_model('model_1D_win_5Stride.h5')

    #prediction
    future_predictions = model.predict(future)

    return future_data, future_predictions, parameter_df

def postprocess_n_plot(future_data, future_predictions, parameter_df):

    #postprocessing
    df_norm = pd.DataFrame(future_predictions.reshape(future_predictions[0].shape), columns = future_data.columns)

    #removing normalizing
    future_pred = round((df_norm* (parameter_df['X_max']-parameter_df['X_min'])) + parameter_df['X_min'], 1)

    #adding datetime index
    last_time_stamp = future_data.reset_index()['datetime'][len(future_data)-1]
    timestamplist = [last_time_stamp + timedelta(minutes=i) for i in range(1,6)]
    future_pred['datetime'] = timestamplist
    future_pred = future_pred.set_index('datetime')
    merged_dataset = pd.concat([future_data, future_pred])

    #plotting the chart
    for i in range(6):
        parameter_name = future_pred.columns.to_list()[i]
        st.subheader("Parameter: {}".format(parameter_name))

        chart_data = pd.DataFrame()
        chart_data['Forecast Value'] = merged_dataset[parameter_name]
        future_list = list(future_data[parameter_name])
        future_list = np.append(future_list, [np.nan]*5)
        chart_data['Input Data'] = future_list                        
        
        st.line_chart(chart_data[-120:])  #plotting only last 2 hrs of data with forecast        

        if future_pred.iloc[:,i].mean() > parameter_df['U_limit'][i]:
            st.error("Upper limit of forecasted {} is exceeded".format(parameter_name))            
        elif future_pred.iloc[:,i].mean() < parameter_df['L_limit'][i]:
            st.error("Lower limit of forecasted {} is exceeded".format(parameter_name))            

    #return future_pred, future_data

def main():   

    future_data = pd.DataFrame()
    future_pred = pd.DataFrame()
    
    file = st.file_uploader("Select input file", type = ['csv'], help = 'Input File should have 1 day worth of data i.e. 1440 rows')

    if st.button("Diagnose"):
        future_data, future_predictions, parameter_df = prediction(file)
        postprocess_n_plot(future_data, future_predictions, parameter_df)       


if __name__=='__main__':
    main()