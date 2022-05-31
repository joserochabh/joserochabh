import numpy as np
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth

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
    st.sidebar.title('Menu')

    with st.sidebar:
        st.radio('Select one:', [1, 2])

    st.title("Simple Streamlit App")

    st.write("Here's our first attempt at using data to create a table:")
    st.write(
        pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
    )

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
    
