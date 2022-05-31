import streamlit as st
import Lbs001
import sqlite3 as sql3


def app():
    with st.sidebar.form(key="login1"):
        autoriza = 'no'
        placet = st.text_input("Placet")
        senha = st.text_input("Digite uma senha", type="password")
        login1 = st.form_submit_button(label = "Enviar")
        logout = st.form_submit_button(label = "Logout")

        try:
            if login1:
                #Busca registro
                test_usr = Lbs001.lista_reg(placet)
                if test_usr is None:
                    st.error("O registro não existe ou o placet não foi informado".format(test_usr))
                else:
                    result = Lbs001.ret_reg_cmpl(placet)
                    placet = result[0]
                    passwd = result[3]
                    #st.info('placet : {}'.format(placet))
                    #st.info('placet : {}'.format(passwd))
                    if (senha == passwd) and (placet == 99999):
                        st.success("Login OK!!!")
                        ###########################
                        # Inicia Cadastro
                        ###########################
                        autoriza = 'yes'
                        
                        return(autoriza)
                        ###########################
                        # Finaliza Cadastro
                        ########################### 
                    elif (senha == passwd) and (placet != 99999):
                        st.error("{} não é administrador".format(placet)) 
                                            
                    else:
                        st.error("O placet ou a senha está incorretos".format(test_usr))

        except sql3.IntegrityError:
            st.error("Todos os campos deverão ser preenchidos")