import streamlit as st
from PIL import Image, ImageFont, ImageDraw


def app():
    st.title("Adm. Estrela de Davi II nº 242")
    st.header('Gerar um convite')

    # usar a lib click==7.1.2 versão mais alta dá erro de execução

    cvt_branco = st.selectbox(
        "Escolha um modelo de convite",
        ('convite9.png', 'convite8.png', 'convite7.png'))

    evento = st.selectbox(
        "Escolha um evento",
        ('INICIAÇÃO', 'ELEVAÇÃO', 'EXALTAÇÃO'))

    #evento = st.text_input('Entre com o tipo de evento, ex.  INICIAÇÃO, ELEVAÇÃO OU EXALTAÇÃO')

    nome_ir = st.text_input('Nome do Ir:. e o placet, ex.   JOSÉ CARLOS ROCHA (99999)')

    data_ev = st.text_input('Entre com a data do evento, ex.   09/05/2022, quarta-feira')

    horario = st.text_input('Entre com o horario do evento, ex.   19:00')


    def gera_convite(nome_ir, data_ev, horario, evento, cvt_branco):
        
        nome_ir = nome_ir.upper()
        data_ev = data_ev
        horario = horario
        evento = evento
        cvt_branco = cvt_branco
        
        # Fundo do convite
        #====================================
        img1 = Image.open(cvt_branco)

        # Fontes
        # =======
        txt_fontn = ImageFont.truetype('Lato-Regular.ttf', 16) # Normal
        txt_fontb = ImageFont.truetype('Lato-Bold.ttf', 16) # Negrito
        txt_fontb_tit = ImageFont.truetype('Lato-Bold.ttf', 20) # Negrito

        # textos
        # =======
        text1 = "Convida todos os MAÇONS REGULARES para participar da Sessão"
        text2 = "Magna de                            DO IRMÃO:"
        text3 = nome_ir
        text4 = 'a ser realizada no dia                                                as                 em nosso'
        text5 = 'templo 602 situado a Av. Brasil, 478, B. Sta Efigênia, Belo Horizonte MG'
        text6 = 'Contamos com a presença de todos os IIr:. para estreitar ainda mais os'
        text7 = 'laços que nos unem, abrilhantando a sessão.'
        text8 = 'Fraternalmente,'
        text9 = 'Fernando C. Queiroz, Ven:. Mestre'
        text10 = 'Cassio F. L. Marques, 1º V:.'
        text11 = 'Aduvaldo E. Silva, 2º V:.'
        text12 = data_ev
        text13 = horario
        text14 = evento

        ed_img1 = ImageDraw.Draw(img1)

        # Posiciona textos
        # ================
        # ((col, lin), texto, (R, G, B), Fonte)
        ed_img1.text((155, 240), text1, (1, 1, 1), font=txt_fontn)#Fixo
        ed_img1.text((155, 260), text2, (1, 1, 1), font=txt_fontb)
        ed_img1.text((155, 320), text3, (1, 1, 1), font=txt_fontb)
        ed_img1.text((155, 370), text4, (1, 1, 1), font=txt_fontn)
        ed_img1.text((155, 395), text5, (1, 1, 1), font=txt_fontn)
        ed_img1.text((155, 425), text6, (1, 1, 1), font=txt_fontn)
        ed_img1.text((155, 455), text7, (1, 1, 1), font=txt_fontn)
        ed_img1.text((155, 485), text8, (1, 1, 1), font=txt_fontn)
        # Assinado:
        ed_img1.text((270, 550), text9, (1, 1, 1), font=txt_fontn)
        ed_img1.text((155, 590), text10, (1, 1, 1), font=txt_fontn)
        ed_img1.text((450, 590), text11, (1, 1, 1), font=txt_fontn)
        # Data e hora
        ed_img1.text((305, 370), text12, (1, 1, 1), font=txt_fontb)
        ed_img1.text((520, 370), text13, (1, 1, 1), font=txt_fontb)
        # Evento
        ed_img1.text((235, 260), text14, (1, 1, 1), font=txt_fontb)

        # Gera imagem
        # ============
        img1.save('convite_image.png')

    if st.button('Gerar convite'):
        st.write('Clique com o botão direito do mouse e salve a imagem gerada.')
        gera_convite(nome_ir, data_ev, horario, evento, cvt_branco)
        convite_img = Image.open('convite_image.png')
        st.image(convite_img, caption='Convite gerado')
    
