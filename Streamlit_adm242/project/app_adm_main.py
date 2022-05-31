import streamlit as st
from PIL import Image, ImageFont, ImageDraw
import streamlit_authenticator as stauth
from pages import home, ger_conv


# ============================
# Inicia app com autenticação
# Funciona com streamlit 1.8.0
# ============================
names = ['Jose Rocha','Alexandre Tomaz', 'Fernando Queiroz', 'Cassio Marques']
usernames = ['jrocha','atomaz','fqueiroz','cmarques']
hashed_passwords = [
     "$2b$12$MUG3iVanSv17GkZykDf.EOumChDTZfzqdZjeCoyT6E.sZkGUBd0Bq",
     "$2b$12$lLzwFxyHu6K1YOS1hlgfhukThkWh/i.VjLpVJYdl5qY/g7nWHiAN.",
     "$2b$12$ZwxWyx2XIDEuJCMoG0ZPIeAMWNLn1JR2wX5Ad6HwCEMA.O1qVUAla",
     "$2b$12$w7dGJJHe7IhI3pl9MH086.9Yd72xk1fP929UYNEigh.mvBUE9Q/.S"
]
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'ed242_cook_aut','--------X-ed242----',cookie_expiry_days=1)
name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Bem-vindo *%s*' % (name))
   
    menu1 = ["Home", "Gerar convite",]
    escolha = st.sidebar.selectbox("Escolha", menu1)
    if escolha == "Home":
        home.app()
    elif escolha == "Gerar convite":
        ger_conv.app()
    
    
        
elif authentication_status == False:
    st.error('Usuario ou senha incorretos.')
elif authentication_status == None:
    st.warning('Entre com o seu usuario e senha.')