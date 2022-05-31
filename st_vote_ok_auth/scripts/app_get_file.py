import streamlit as st
import Lbs001

st.text('Download de arquivo')
st.markdown(Lbs001.get_file('apuracao1.docx', 'Documento de apuração'), unsafe_allow_html=True)
