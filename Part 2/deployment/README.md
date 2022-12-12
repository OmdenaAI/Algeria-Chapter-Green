# Omdena Chapter Algeria GreenHouse -part2-deployment

<p align="center">
  <img width="1000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/images/greenhouse.jpg"
</p>

- This project is part of Omdena Algeria Local chapter.
<p align="center">
  <img width="400" src="https://dl.airtable.com/.attachmentThumbnails/4d15be073b801b2c02e8cb055c1a78af/11e9404d"
</p>

- The link to main repo can be found [here.](https://github.com/OmdenaAI/Algeria-Chapter-Green)
  
# 1.0 Aim:
- This project is focussed towards providing smart solutions to farmers for production of tomato inside a GreenHouse within the country of Algeria.
- Following are the three common challenges faced while growing tomato crops within a Greenhouse:
    1. Indoor Climate Conditions prediction
    2. Disease Detection on plant leaves
    3. Irrigation recommendation system

- The webpage link of the deployed project can be found [here.](https://green-algeria.streamlit.app/)
- Below is the homepage of the deployed project:
<p align="center">
  <img width="2000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/images/deployment01.JPG"
</p>
 
## 1.1 Indoor Climate Conditions prediction
<p align="center">
  <img width="2000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/images/Greenhouse-monitoring.jpg"
</p>

- Growing crops in controlled environments lets us grow larger quantities and better-quality produce, year-round. Modern horticulture is built and thrives on this principle. One of the most important aspects of growing in a protected environment, such as a greenhouse, is climate control.
- Improving climate control in your greenhouse helps prevent diseases, boosts plant growth, increases quality and even saves energy.
- By controlling the immediate environment, crops are easily grown without the persistence of outdoor pathogens and pests.
- A **Time series forecasting** model is developed which can forecast the climate conditions within the next **5 minutes**.
- If any of the forecasted values of climate factors are below conditions suitable for tomato growth, an error message is triggered. In actual conditions the necessary actuators can be activated to bring the conditions to suitable values. In the model built here, an error message stating the parameter is displayed.
- I have co-lead the team on this project. The link to readme file can be found [here](https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/Time%20Series%20Problem/Readme.md)

## 1.2 Disease Detection on plant leaves
<p align="center">
  <img width="2000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/images/leaf%20diseases.png"
</p>

- Agricultural productivity is something on which Greenhouse economy highly depends. 
- This is the one of the reasons that disease detection in plants plays an important role in agriculture field, as having disease in plants are quite natural. 
- If proper care is not taken in this area then it causes serious effects on plants and due to which respective product quality, quantity or productivity is affected.
- A **EfficientNetB3 and VGG16 image classification model** is developed which can detect whether a tomato leaf is healthy or infected along with the disease type if its affected. 
- The **EfficientNetB3** trained on the **Plant Expert data consisting of 54 classes** got an **Accuracy of 98%**

## 1.3 Irrigation recommendation system
<p align="center">
  <img width="2000" src="https://github.com/sanjayd89/Algeria_GreenHouse/blob/main/images/drip%20irrigation.jpg"
</p>

- Water availablity is always a challenge in desert regions of Algeria.
- Hence, it is very important to manage water requirements within a Greenhouse for irrigation purposes.
- Drip Irrigation, also known as trickle irrigation is most commonly used in regions with water scarcity.
- It works by delivering water slowly and directly to the plant root. The high efficiency of the system results from two primary factors:
    - They absorb the water into the soil before it can evaporate or runoff.
    - It only applies water where it is needed. For example, at the plant’s roots rather than everywhere. Drip systems are simple and relatively forgiving of errors in design and installation.
- Hence, it is a very effective method of watering plants. 
- For comparison purposes, the standard sprinkler system has an efficiency of around 75-85%. A Greenhouse Drip Irrigation System, in contrast, has an efficiency level of over 90%. 
- Over time, this difference in water delivery and efficiency will make a real difference in crop production levels quality, and in a company’s bottom line.
- A model is developed to predict instances when would irrigation required by the crops and supply the water accordingly.

