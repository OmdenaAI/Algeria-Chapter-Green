# **:fountain: Water Level Forecasting-Team 1**
## 🧿 Introduction

The acqua alta, as the seasonal flooding is known, is a natural phenomenon, which has always been a feature of Venetian life.
Usually, tidal events have a very short duration. For example, when the high tide reaches a maximum value of 120 centimetres, it lasts an average of less than an hour and a half.
Even when there is high water, you can still move around the city walking on designated pedestrian routes - partly consisting in temporary elevated platforms - which can be used up to when the height of the tide reaches 120 centimetres.
During high tides, public water transport services work according to schedule, except in the event of very exceptional tides, although some routes may be modified when the height of the tide reaches 95 centimetres.
Flood information is provided in real time via the web and smartphones. To get information about the tidal levels in Venice, see the daily forecasts of the city’s tide monitoring and forecast centre.
Venezia is an Italian city built on a lagoon, a body of water separated from the sea by a strip of land. However, this city is frequently subject to flooding during
autumn and spring due to the "acqua alta",a tide that raises the water level to the point that the sea invades the city. This phenomenon causes great complications 
in the city. The forecast of the water level is therefore a fundamental task for the safeguard of the city of Venezia.

<p align="center">
  <img width="600" height="325" src="https://gdb.voanews.com/b384ca01-1fe0-4164-a739-9d507fa04d15_w1080_h608.jpg">
</p>


## :pushpin: **DATASET**

The dataset contains hourly measurements of the water level in Venezia from 1983-01-01 to 2016-01-01.

To load the dataset, use the following link: https://www.kaggle.com/datasets/lbronchal/venezia

Data Description:
Attribute Information:

datetime: date and hour of the measurement in utc time
level: level of the water in cm from the reference point


## **:bar_chart: MODULE WORKFLOW**

Load data

EDA implementation

Data Processing & Transformation

Preparation of Train, Valid and Test datasets

Build, Train & Evaluate the model.
![image](https://user-images.githubusercontent.com/65725230/193627592-a625f93e-263f-414e-9c56-3eaa21a51484.png)

## 🎯 Results

### Prediction Plots

#### MLP MODEL 1
 <p align="center">
  <img width="600" height="325" src="https://user-images.githubusercontent.com/66861391/193641941-1396b8de-839f-4481-877c-689411bad414.jpeg">
</p>

#### CNN
<p align="center">
  <img width="600" height="325" src="https://user-images.githubusercontent.com/66861391/193642199-55acbaa8-d564-4113-ae6c-6fe803ed91dd.jpeg">
</p>


#### GRU
<p align="center">
  <img width="600" height="325" src="https://user-images.githubusercontent.com/66861391/193642250-b9f0f9db-923f-4a71-a1c9-484aba8a9c9a.jpeg">
</p> 



#### LSTM
<p align="center">
  <img width="600" height="325" src="https://user-images.githubusercontent.com/66861391/193642310-b926200e-8987-497a-8e26-1a636303d455.jpeg">
</p>


#### CNN-LSTM
<p align="center">
  <img width="600" height="325" src="https://user-images.githubusercontent.com/66861391/193642369-9bbd707c-fba1-4865-bec5-c65e33c06c59.jpeg">
</p>



### :open_file_folder: Download and Unzip Contents from GitHub Repo

LEAD REPO - https://github.com/Surya-24/Water-Level-Forecasting


## **:shipit: CONTRIBUTORS**
1. [Freny Reji](https://github.com/freny24)
2. [Mada Sai Surya](https://github.com/Surya-24)
3. [Djazila Souhila Korti](https://github.com/souhila98)
4. [Boukerma Fedoua](https://github.com/Boukermafedoua)


