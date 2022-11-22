import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import base64





def app():
    st.title("🌱 Omdena Algeria Chapter 🌱")
    st.write("\n")
    st.write("\n")
    st.markdown("Collaborate, Learn, Build, Grow",)
    st.subheader("Part:2 🌾Building an Intelligent Control System for Greenhouses")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    """### gif from local file"""
    file_ = open("images/part2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
    # st.image(img1)
    st.write("\n")
    st.header("🔍Problem Statement")
    st.markdown("""
        - The management of all equipment under one control system, including heating, venting, and irrigation, is a hard task in terms of systems management and data collection. As a seasonal grower with product cycles of up to two years in duration, patience is necessary. It takes time to collect the data for these systems to work and learn.

        - Greenhouse environments are also challenging for technology implementation due to broad temperature and humidity ranges, which influence both the electronic and mechanical components that contribute to their ongoing development. This can be a frustration for staff trying to complete their weekly plans.

        - AI solutions for greenhouse growers are still in their initial phases of development. The integration of intelligent control systems requires changes to processes, which can be disruptive to production, so flexibility and managing expectations are important to manage the greenhouses effectively.
        """)
    st.write("\n")
    st.header("🎯Goal")
    st.markdown("""
        Build a strong community for sharing knowledge of AI and ML models in agriculture.\n 
        Decide the best values for managing the levels of temperature, humidity, the use of water, the light and other parameters inside the greenhouse.\n
        Notify the growers when there are issues within the crop relating to growth rate, pests, and disease.
        """)
    st.write("\n")
    st.write("### 1 Indoor Climate Conditions prediction")
    img=Image.open("images/Greenhouse-monitoring.jpg")
    # newsize=(280,300)
    # img1=img.resize(newsize)
    st.image(img,use_column_width='always')
    st.markdown("""
        - Growing crops in controlled environments lets us grow larger quantities and better-quality produce, year-round. Modern horticulture is built and thrives on this principle. One of the most important aspects of growing in a protected environment, such as a greenhouse, is climate control.
        - Improving climate control in your greenhouse helps prevent diseases, boosts plant growth, increases quality and even saves energy.
        - By controlling the immediate environment, crops are easily grown without the persistence of outdoor pathogens and pests.
        - A Time series forecasting model is developed which can forecast the climate conditions within the next 5 minutes.
        - If any of the forecasted values of climate factors are below conditions suitable for tomato growth, an error message is triggered. In actual conditions the necessary actuators can be activated to bring the conditions to suitable values. In the model built here, an error message stating the parameter is displayed.
        """)
    st.write("\n")
    st.write("### 2 Disease Detection on plant leaves")
    img2=Image.open("images/leaf_diseases.png")
    # newsize=(280,300)
    # img1=img.resize(newsize)
    st.image(img2,use_column_width='always')
    st.markdown("""
        - Agricultural productivity is something on which Greenhouse economy highly depends.
        - This is the one of the reasons that disease detection in plants plays an important role in agriculture field, as having disease in plants are quite natural.
        - If proper care is not taken in this area then it causes serious effects on plants and due to which respective product quality, quantity or productivity is affected.
        - A VGG16 and EfficientNet image classification model is developed which can detect whether a tomato leaf is healthy or infected along with the disease type if its affected.
        - The **EfficientNetB3** trained on the **Plant Expert data consisting of 54 classes** got an **Accuracy of 98%**
        """)
    st.write("\n")
    st.write("### 3 Irrigation recommendation system")
    img3=Image.open("images/rec_irrigation.jpg")
    # newsize=(280,300)
    # img1=img.resize(newsize)
    st.image(img3,use_column_width='always')
    st.markdown("""
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
        """)
    st.header("📊Directory Structure")
    st.code("""
        ├── Part 2
        │   ├── Subproject1- Indoor Climate Factors
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results

        │   ├── Subproject2- Diseases and Pests Detection
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results

        │   ├── Subproject3- Recommendation Systems
        │     ├── Reports
        │     ├── src
        │       ├── data
        │       ├── documents
        │       ├── references
        │       ├── tasks
        │          ├── Task1- Research
        │          ├── Task2- EDA
        │          ├── Task3- Preprocessing
        │          ├── Task4- Model Building
        │          └── Task5- Deployment
        │       ├── visualizations
        │       └── results
        │
        └── README.md
        """)
    st.write("\n")
    st.header("🌐Website")
    link='Check out this [link](https://github.com/OmdenaAI/Algeria-Chapter-Green/tree/main/Part%202)'
    st.markdown(link,unsafe_allow_html=True)
    st.markdown("© 2022 Omdena")

    
