
import streamlit as st
import streamlit_authenticator as stauth
import Lbs001
from pages import home, cad_usr, rem_usr, lst_usr, cria_ch, lst_ch, login, apura_vt
import sqlite3 as sql3




names = ['Jose Rocha','Alexandre Tomaz']
usernames = ['jrocha','atomaz']
hashed_passwords = [
    "$2b$12$MQt5V8WPzy05YXwtEQ.2euUe3BIEoF5tTFTyK5nKdzJJiaV9nXbwq", 
    "$2b$12$5b1x27aIw2XVGd20PcwfceJdRBwt6wYk99E7H0o6/TAoyXY6FtJnu"
]
authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'stl_aut_ck','--------X----------',cookie_expiry_days=1)
name, authentication_status = authenticator.login('Login','main')

if authentication_status:
    st.write('Welcome *%s*' % (name))

    menu1 = ["Home", "Cadastro usuario", "Remove usuario", "Listar usuario", "Cria chapa eleição", "Lista chapas eleição", "Apuração de eleição"]
    escolha = st.sidebar.selectbox("Escolha", menu1)
    if escolha == "Home":
        home.app()
    elif escolha == "Cadastro usuario":
        cad_usr.app()
    elif escolha == "Remove usuario":
        rem_usr.app()
    elif escolha == "Listar usuario":
        lst_usr.app()
    elif escolha == "Cria chapa eleição":
        cria_ch.app()
    elif escolha == "Lista chapas eleição":
        lst_ch.app()
    elif escolha == "Apuração de eleição":
        apura_vt.app()
    
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')



