import streamlit as st
import Lbs001
import numpy as np
import pandas as pd



def app():
 
    st.subheader("Remover usuário")

    with st.form(key="form2"):
        st.subheader("Informe o placet")
        placet = st.text_input("Placet")
        #enviar1 = st.form_submit_button(label = "Verificar")
        #remover1 = st.form_submit_button(label = "Remover")
        col1, col2 = st.columns(2)
        with col1:
            enviar1 = st.form_submit_button(label = "Verificar")
        with col2:
            remover1 = st.form_submit_button(label = "Remover")            
        
        if enviar1:
            #Busca registro
            test_usr = Lbs001.lista_reg(placet)
            if test_usr is None:
                st.error("O registro não existe ou o placet não foi informado".format(test_usr))
            else:
                result = Lbs001.ret_reg_cmpl(placet)
                st.text("Placet: {}".format(result[0]))
                st.text("Nome: {}".format(result[1]))
                st.text("Data nasc.: {}".format(result[2]))
            
        if remover1:
            test_usr = Lbs001.lista_reg(placet)
            if test_usr is None:
                st.error("O registro não existe ou o placet não foi informado".format(test_usr))
            else:
                #st.info("Chamando a função del_reg para o reg {}".format(placet))
                msg = Lbs001.del_reg(placet)           
                st.success(msg)