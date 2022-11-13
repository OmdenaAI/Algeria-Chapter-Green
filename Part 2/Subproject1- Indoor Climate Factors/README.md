# Indoor Climate Conditions Forecasting

<p align="center">
  <img width="1000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/climate-basics.jpg"
</p>

- The dataset considered has 9 months worth of data from **June 2017** to **Feb 2018**. The **remaining three months**, farmers utilise the time for **cultivation of field** for improved soil quality.

## 1.0 Pre-processing
- The date and time column were combined to get timestamp details for each row.
- No missing data was found.
- Outliers were detected and plotted using Box plot.
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/outlier.png)
- Using IQR method, the outliers were handled. The plot below shows the cleaned data:
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/cleaned%20data.png)

## 2.0 Exploratory Data Analysis
- A plot of all features vs time shows that there are data missing between two time intervals.
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/time%20vs%20feature%20showing%20missing%20dates.png)
- A new feature "delta" was created to find the time difference between consecutive rows which revealed there to be **20** number of "time jumps" in the dataset.
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/delta%20timestamps.png)
- Using curve fitting within scipy library, a curve was fitted for all the features and missing data was imputed.
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/curve%20fitting.png)

### 2.1 Insights from data
- The plot of Indoor temperature and Soil temperature over period of time is shown below:
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/indoor%20temp%20vs%20soil%20temp.png)
	- The soil tempertaure distribution is similar to the indoor temperature and has lower variance compared to indoor temperature suggesting effective usage of irrigation.
- The moisture content in soil is significantly lower in the soil compared to indoor air as the same gets absorbed directly by the crops.
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/RH%20vs%20soil%20moisture.png)

- A plot of all features showing its distribution at day and night was plotted as shown below:
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/day%20night%20performance.png)
	- The temperature conditions at night are lower than day as expected for both inside the climate house as well as soil.
	- The variance in indoor humidity is considerably less at night than at day
	- Indoor lighting has been kept consistent acorss day and night except during winter conditions when the lighting was lower at night compared to day.
	- Indoor CO2 concentration was kept consistently higher for improved productivity during day as we ll as night.
	- The moisture content in soil has varied significantly during hotter conditions as compared to winter.

## 3.0 Modeling
- We have considered Bi-Directional LSTM model with 1D Convolution added.
- The model is provided input of 1440 rows i.e. one day worth of data and model forecasts climate conditions for next 5 minutes.
- A sample forecast is shown below:
![](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/prediction.png)

## 4.0 Application
- In application, there would be a database connected to the complete monitoring and control systems which would take in every minute data of all factors. Based on this, for every 1 day data, forecast can be made for next 5 minutes to ascertain climate conditions within the Greenhouse
- Here, we have made provision in the application to take a 1 day input from the user and forecast values.
- Below is snapshot of the same showing forecast values alongwith trigger warning for parameters crossing set limits:
<p align="center">
  <img width="1000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/images/streamlit_app.jpg"
</p>

## 5.0 AGC Dataset:
- The project initially started on Algeria Greenhouse Challenge (AGC) dataset for which Data Processing, EDA, Feature Selection were performed.
- The analysis of the same can be found [here](https://github.com/sanjayd89/Algeria_GreenHouse/tree/main/Sub%20Project%201%20-%20Indoor%20Climate%20Condition/AGC%20Dataset)
- However, it was found that data was available for only 5 month period. 
- Model developed on only 5 month period would not perform well for forecasting conditions throughout the year. Hence, we went with current dataset which has 9 months worth of data.
	
## 6.0 Contributors
| <a href="https://github.com/sanjayd89"><img src="https://avatars.githubusercontent.com/sanjayd89" width=150px height=150px /></a>| <a href="https://github.com/souhila98"><img src="https://avatars.githubusercontent.com/souhila98" width=150px height=150px /></a>| <a href="https://github.com/Vice777"><img src="https://avatars.githubusercontent.com/Vice777" width=150px height=150px /></a>|
| :---: | :---: | :---: |
| **[Sanjay Dubey](https://github.com/sanjayd89)**| **[Djazila Souhila Korti](https://github.com/souhila98)**| **[Vivek Dharewa](https://github.com/Vice777)**|
| <a href="https://www.linkedin.com/in/sanjay-dubey-78318022/"><img src="https://mpng.subpng.com/20180324/vhe/kisspng-linkedin-computer-icons-logo-social-networking-ser-facebook-5ab6ebfe5f5397.2333748215219374063905.jpg" width="32px" height="32px"></a>| <a href="https://www.linkedin.com/in/djazila-souhila-korti-1470521b9"><img src="https://mpng.subpng.com/20180324/vhe/kisspng-linkedin-computer-icons-logo-social-networking-ser-facebook-5ab6ebfe5f5397.2333748215219374063905.jpg" width="32px" height="32px"></a>| <a href="https://www.linkedin.com/in/vivek-dharewa-69baaa165/"><img src="https://mpng.subpng.com/20180324/vhe/kisspng-linkedin-computer-icons-logo-social-networking-ser-facebook-5ab6ebfe5f5397.2333748215219374063905.jpg" width="32px" height="32px"></a>|

