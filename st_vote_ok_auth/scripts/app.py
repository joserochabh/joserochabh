
import streamlit as st
import Lbs001
from pages import home, cad_usr, lst_usr, cria_vt, lst_vt, login
import sqlite3 as sql3
import SessionState

autoriza = (login.app())

if autoriza == "yes":   
    menu1 = ["Home", "Cadastro usuario", "Lista usuario", "Cria Vt", "Lista Vt"]
    escolha = st.sidebar.selectbox("Escolha", menu1)
    if escolha == "Home":
        home.app()
    elif escolha == "Cadastro usuario":
        cad_usr.app()
    elif escolha == "Lista usuario":
        lst_usr.app()
    elif escolha == "Cria Vt":
        cria_vt.app()
    elif escolha == "Lista Vt":
        lst_vt.app()

 

