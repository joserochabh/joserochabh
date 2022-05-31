# Load important libraries 
import pandas as pd
import streamlit as st
from PIL import Image, ImageFont, ImageDraw

def app():
    st.title("Adm. Estrela de Davi II nº 242")
    logo = Image.open('ed242_180x180.png')
    
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image(logo, caption=None)
    with col3:
        st.write("")
    