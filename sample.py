import streamlit as st
from PIL import Image

image0 = Image.open('pic0.jpg')
image1 = Image.open('pic1.jpg')
image2 = Image.open('pic2.jpg')

st.image(image0, caption="divination_sample")
st.image(image1, caption="divination_sample")
st.image(image2, caption="divination_sample")