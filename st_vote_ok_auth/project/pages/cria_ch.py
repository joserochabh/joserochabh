import streamlit as st
import numpy as np
import Lbs001
import sqlite3 as sql3



def app():
    #cria_tbl_chapa("USUARIO_ED242","CHAPAS")
    st.subheader("Cadastro de eleição(Chapa)")
    db_name = "USUARIO_ED242.db"
    tbl_name = "CHAPAS"
    #tbl = Lbs001.tbl_existe(db_name,tbl_name)
    #if tbl != tbl_name:
    #    Lbs001.cria_tbl_chapa(db_name,tbl_name)
    #    st.text("Tabela criada")
    #else:
    #    st.text("Já existe")
    with st.form(key="form1"):
        codchapa = st.text_input("Cod. chapa")
        nome_chapa = st.text_input("Nome da chapa")
        veneravel = st.text_input("Veneravel")
        vigilante1 = st.text_input("Primeiro Vigilante")
        vigilante2 = st.text_input("Segundo Vigilante")
        loja = st.text_input("Nome da loja")
        
        enviar = st.form_submit_button(label = "Enviar")
    try:
        if enviar:
            #Verifica se o user existe
            test_chapa = Lbs001.lista_reg_chapa(codchapa)
            if test_chapa is None:
                Lbs001.insere_reg_chapa(codchapa, nome_chapa, veneravel, vigilante1, vigilante2, loja)
                st.success("A chapa {} foi criada".format(nome_chapa))
            else:
                st.error("A chapa código {} já existe".format(codchapa))

    except sql3.IntegrityError:
        st.error("Todos os campos deverão ser preenchidos")

    
