# Importing Libraries
import streamlit as st
import io
import numpy as np
from PIL import Image 
import tensorflow as tf



import os
import numpy as np
import pandas as pd
import time
import cv2

import app1
import app1_2
import app2
import app3
import app4
import app5

#image_rootpath='Images/'

st.set_page_config(
    page_title="Omdena Algeria Chapter phase 2",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded",
)
PAGES=	{	
"Algeria Local Chapter":app1,
"Algeria Chapter Part_2":app1_2,
"Indoor Climate Factors":app2,
"Diseases and Pests Detection":app3,
"Recommendation Systems":app4,
"Contributors":app5,			
		}

st.sidebar.title("Choose your option to navigate")
selection=st.sidebar.radio("Go to",list(PAGES.keys()))
page=PAGES[selection]
page.app()
