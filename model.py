import streamlit as st
st.set_page_config(layout="wide")
import pickle
import pandas as pd

from PIL import Image

with open('model6.pkl' , 'rb') as f:
    model = pickle.load(f)


title = '<p style="font-weight:bold; color:Black; font-size:45px;">Hazardous Asteroid Classifier</p>'
st.markdown(title, unsafe_allow_html=True)

asteroid = Image.open('images/banner.jpg')
st.image(asteroid, use_column_width = 'always')

st.markdown("***")

prompt_1 = '<p style="font-weight:bold; color:Black; font-size:22px;">Absolute Magnitude: </p>'

st.markdown(prompt_1, unsafe_allow_html=True) 

q_1 = st.text_input(' ', key = 1, max_chars=280)


prompt_2 = '<p style="font-weight:bold; color:Black; font-size:22px;">Minimum Diameter (in Miles): </p>'

st.markdown(prompt_2, unsafe_allow_html=True) 

q_2 = st.text_input(' ', key = 2, max_chars=280)


prompt_3 = '<p style="font-weight:bold; color:Black; font-size:22px;">Maximum Diameter (in Miles): </p>'

st.markdown(prompt_3, unsafe_allow_html=True) 

q_3 = st.text_input(' ', key = 3, max_chars=280)


prompt_4 = '<p style="font-weight:bold; color:Black; font-size:22px;">Minimum Orbit Intersection Distance (MOID): </p>'

st.markdown(prompt_4, unsafe_allow_html=True) 

q_4 = st.text_input(' ', key = 4, max_chars=280)


prompt_5 = '<p style="font-weight:bold; color:Black; font-size:22px;">Perihelion Distance: </p>'

st.markdown(prompt_5, unsafe_allow_html=True) 

q_5 = st.text_input(' ', key = 5, max_chars=280)


button = st.button('Enter')

dict = {"Absolute Magnitude": q_1, "Est Dia in Miles(min)": q_2, "Est Dia in Miles(max)": q_3, "Minimum Orbit Intersection": q_4, "Perihelion Distance": q_5}

dict = pd.Series(dict)

dict = dict.to_frame().T

if button: 
	sub_title = '<p style="font-weight:bold; color:Black; font-size:30px;">Hazardous?</p>'

	st.markdown(sub_title, unsafe_allow_html=True)

	prediction = model.predict(dict)

	no = '<p style="color:Black; font-size:25px;">No</p>'
	yes = '<p style="color:Black; font-size:25px;">Yes</p>'

	if prediction == [0]:
		st.markdown(no, unsafe_allow_html=True)
	else:
		st.markdown(yes, unsafe_allow_html=True)



