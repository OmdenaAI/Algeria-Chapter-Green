import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd

df = pd.read_excel('Green_Algeria_Project_Contributions.xlsx')
   
def app():
    st.title("🌱 Omdena Algeria Chapter")
    img=Image.open("images/omdena_algeria.png")
#     newsize=(280,300)
#     img1=img.resize(newsize)
    st.write("\n")
    st.write("\n")
    st.markdown("""Collaborate, Learn, Build, Grow """)
    
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image(img,use_column_width='always')
    st.write("\n")
    st.write("\n")
    st.header("Omdena Algeria Chapter Lead 👩‍🏫👩‍👩‍💻💼")
    st.image("https://media-exp1.licdn.com/dms/image/C5603AQH-HKA9Nni2rQ/profile-displayphoto-shrink_800_800/0/1662582238000?e=2147483647&v=beta&t=EE4CTMSBgPQYJvB4vraMP2YaVOXJDhG7ZVhA3Tt0ndk") 
    st.markdown(
       """
       Omdena Algeria Chapter 🌐Website: https://omdena.com/local-chapters/algeria-local-chapter/
       """)
    st.header("🤞Contributors")
    st.dataframe(df)
    st.write("\n")
    st.header("🌐Website")
    link='check out this [link](https://omdena.com/local-chapters/algeria-local-chapter/)'
    st.markdown(link,unsafe_allow_html=True)
    st.markdown("© 2022 Omdena")
