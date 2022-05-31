#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageFont, ImageDraw


# ### Variaveis

# In[2]:


nome_ir = ('SUPER HOMEM DO PLANETA KRIPTON (Placet 88888)')
data_ev = ('11/05/2022, quarta-feira')
horario = ('19:00h')
evento = ('INICIAÇÃO')
#evento = ('ELEVAÇÃO')
#evento = ('EXALTAÇÃO')


# In[3]:


img1 = Image.open("convite9_tit_no_txt.png")#Fundo Marmore, titulo e Logo

#img1 = Image.open("convite7_no_txt_lg.png")#Fundo Marmore e Logo
#img1 = Image.open("convite8_no_txt.png")#Fundo templo
#img1 = Image.open("convite7_no_txt.png")#Fundo Marmore
#img1 = Image.open("convite-no-txt.png")#Fundo Azul
#img1 = Image.open("convite9_tit_no_txt.png")#Fundo Marmore, titulo e Logo


# In[4]:


txt_fontn = ImageFont.truetype('Lato-Regular.ttf', 16)
txt_fontb = ImageFont.truetype('Lato-Bold.ttf', 16)
txt_fontb_tit = ImageFont.truetype('Lato-Bold.ttf', 20)


# In[5]:


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


# In[6]:


ed_img1 = ImageDraw.Draw(img1)


# ### Posicionamento dos textos

# In[7]:


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


# In[8]:


img1.save('result_image.png')

