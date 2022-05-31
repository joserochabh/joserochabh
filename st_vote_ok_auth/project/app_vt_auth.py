import streamlit as st
import Lbs001
import sqlite3 as sql3
from datetime import datetime
# Verifica se o usuario ja votou e caso negativo, registra o voto
def grava_voto(placet,escolha,data_hora):
    pass





#############
# Variaveis #
#############
#chapas = [242001,]
chapas = [242001,242002]
pleito = 100
quant_ch = len(chapas)
titulo_eleic = 'Eleição da Loja Templarios do Oeste'
data_e_hora_atuais = datetime.now()
data_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
count = 1
#autoriza = 'no'
#st.text(autoriza)
# Construção da pagina:
st.header(titulo_eleic)

# Lista as CHAPAS
for codchapa in chapas:
    chap = Lbs001.lista_chapa(codchapa)
    st.subheader('Chapa {}: {}'.format(count, chap[1]))
    st.text('Veneravel Mestre: {}'.format(chap[2]))
    st.text('Primeiro vigilante: {}'.format(chap[3]))
    st.text('Segundo vigilante: {}'.format(chap[4]))
    count += 1
    st.write('-----')

st.header('Escolha a sua opção e vote:')
with st.form(key="login1"):
    if quant_ch == 1:
        voto = st.radio('Escola uma opçã:', ['Chapa1', 'Voto em branco', 'Voto Nulo'])
    if quant_ch == 2:
        voto = st.radio('Escola uma opção:', ['Chapa1', 'Chapa2', 'Voto em branco', 'Voto Nulo'])
    placet = st.text_input("Digite o numero do seu Placet (apenas numeros)")
    senha = st.text_input("Digite a sua senha", type="password")
    login1 = st.form_submit_button(label = "Vote")
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
                if (senha == passwd) and (placet == placet):
                    st.success("Ir∴ reconhecido!!!")
                    ###########################
                    # Inicia Cadastro
                    ##########################
                    data_e_hora_atuais = datetime.now()
                    data_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')        
                    result = Lbs001.lista_reg2(placet,'VOTANTE_RG')
                    if result == placet:
                        msg = 'O Ir∴ cuja o placet é {} já votou nessa eleição.'.format(placet)
                        st.warning(msg)
                    else:
                        msg1 = Lbs001.insere_reg_votante(placet, voto, data_hora, pleito)
                        msg2 = Lbs001.insere_reg_voto(placet, voto, data_hora, pleito)
                        st.success(msg2)
                        st.text("Placet = {}, voto = {}, Data = {}".format(placet,voto,data_hora))
                    
                    ###########################
                    # Finaliza Cadastro
                    ###########################                                                          
                else:
                    st.error("O placet ou a senha está incorretos".format(test_usr))
    except sql3.IntegrityError:
        st.error("Todos os campos deverão ser preenchidos") 

   

    