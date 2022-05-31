import streamlit as st
import numpy as np
import sqlite3 as sql3
import Lbs001



def app():
    st.subheader("Cadastro de usuários")
    with st.form(key="form1"):
        placet = st.text_input("Placet")
        nome = st.text_input("Nome")
        datanasc = st.text_input("Data de nasc.(DDMMAAAA)")
        senha = st.text_input("Digite uma senha", type="password")
        senhaconfirm = st.text_input("Confirme a senha", type="password")
        enviar = st.form_submit_button(label = "Enviar")
    try:
        if enviar:
            if senha == senhaconfirm:
                #Verifica se o user existe
                test_usr = Lbs001.lista_reg(placet)
                if test_usr is None:
                    Lbs001.insere_reg(placet, nome, datanasc, senha)
                    st.success("O usuário de placet {} foi criado".format(placet))
                else:
                    st.error("O registro {} já existe".format(test_usr))

            else:
                st.error("A senha do usuário de placet {} estão diferentes".format(placet))
    except sql3.IntegrityError:
        st.error("Todos os campos deverão ser preenchidos")