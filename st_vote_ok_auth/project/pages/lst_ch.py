# Load important libraries 
import pandas as pd
import streamlit as st
import Lbs001

def app():
    ##### Listar USUARIOS ####### 
    st.subheader("Chapas para votações")
    chapas_lst = Lbs001.lists_tb('CHAPAS')
    #st.text(users_lst)
    df = pd.DataFrame(chapas_lst, columns =['codchapa', 'nome_chapa', 'veneravel', 'vigilante1', 'vigilante2', 'loja'])
    st.dataframe(df)