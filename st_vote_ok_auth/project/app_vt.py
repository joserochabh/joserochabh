import streamlit as st
import Lbs001
import sqlite3 as sql3
from datetime import datetime

#############
# Variaveis #
#############
#chapas = [242001,]
chapas = [242001,242002]
quant_ch = len(chapas)
titulo_eleic = 'Eleição da Loja A:.R:.L:. Estrela de Davi II 242'
data_e_hora_atuais = datetime.now()
data_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

# Construção da pagina:
st.header(titulo_eleic)
count = 1
col1, col2 = st.beta_columns(2)
# Uma Chapa
for codchapa in chapas:
    chap = Lbs001.lista_chapa(codchapa)
    st.text('Chapa {}: {}'.format(count, chap[1]))
    st.text('Veneravel Mestre: {}'.format(chap[2]))
    st.text('Primeiro vigilante: {}'.format(chap[3]))
    st.text('Segundo vigilante: {}'.format(chap[4]))
    count += 1
    st.write('-----')

if quant_ch == 1:
    escolha = st.radio('Escola a opção e vote:', ['Chapa1', 'Voto em branco', 'Voto Nulo'])
    if st.button('Vote'):
        data_e_hora_atuais = datetime.now()
        data_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        st.success('Voce votou {}  -  {}.'.format(escolha, data_hora))

if quant_ch == 2:
    escolha = st.radio('Escola a opção e vote:', ['Chapa1', 'Chapa2', 'Voto em branco', 'Voto Nulo'])
    if st.button('Vote'):
        data_e_hora_atuais = datetime.now()
        data_hora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')        
        st.success('Voce votou {}  -  {}.'.format(escolha, data_hora))   

    