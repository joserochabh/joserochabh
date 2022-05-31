import streamlit as st
import numpy as np
import pandas as pd
import pandas_profiling
import Lbs001



def app():
    st.subheader("Lista de usuários")
    ##### Listar USUARIOS #######        
    users_lst = Lbs001.lists_tb('USUARIO')
    #st.text(users_lst)
    df = pd.DataFrame(users_lst, columns =['Placet', 'Nome', 'Data_nasc', 'Passwd'])
    st.dataframe(df)