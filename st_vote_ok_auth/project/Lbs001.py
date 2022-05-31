import sqlite3 as sql3
from datetime import datetime
import os
import base64

############################
# Autor: Jose Rocha BH ∴    #
# jose.rocha@gmail.com     #
############################
############################
#         FUNÇÕES          #
############################
# No aplicativo use:
# import Lbs001
#
# Para usar uma das funções use:
#
# Lbs.cria_db("DBNAME")
############################
# Verifica se tabela existe ( retorna o nome da tabela ou "Inexistente")
def tbl_existe(db_name,tbl_name):
    db_name = db_name
    tbl_name = tbl_name
    conn = sql3.connect(db_name)
    cursor = conn.cursor()
    #cursor.execute("SELECT tbl_name = ? FROM db_name = ? WHERE type='table';",(tbl_name,db_name,))
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = (cursor.fetchall())
    for tabela in tabelas:
        if tabela[0] == tbl_name:
            return(tabela[0])
        else:
            msg = "Inexistente"
            return(msg)
    conn.close()
    
    
# Cria a base de dados sqlite3
def cria_db(db_name):
    db_name = db_name
    conn = sql3.connect(db_name)
    conn.close()
    msg = db_name + " Criado"
    print(msg)
    return(msg)

#Cria tabela VOTO_RG no banco de dados
def cria_tbl_voto(db_name,tbl_name):
    db_name = db_name
    tbl_name = tbl_name
    conn = sql3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE {} (voto TEXT NOT NULL, datavoto TEXT NOT NULL, pleito INTEGER)'.format(tbl_name))
    conn.close()
    msg = "A Tabela {} foi criada no banco de dados {}".format(tbl_name, db_name)
    return(msg)

#Cria a tabela VOTANTE_RG
def cria_tbl_votante(db_name,tbl_name):
    db_name = db_name
    tbl_name = tbl_name
    conn = sql3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE {} (placet INTEGER PRIMARY KEY, datavoto TEXT NOT NULL, pleito INTEGER)'.format(tbl_name))
    conn.close()
    msg = "A Tabela {} foi criada no banco de dados {}".format(tbl_name, db_name)
    #print(msg)
    return(msg)

# Cria tabela USUARIOS
def cria_tbl(db_name,tbl_name):
    db_name = db_name
    tbl_name = tbl_name
    conn = sql3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE {} (placet INTEGER PRIMARY KEY, nome TEXT NOT NULL, datanasc TEXT NOT NULL, senha TEXT NOT NULL)'.format(tbl_name))
    conn.close()
    msg = "Tabela " + tbl_name + " criada" + " no database " + db_name
    print(msg)
    return(msg)

# Cria a tabela CHAPA
def cria_tbl_chapa(db_name,tbl_name):
    db_name = db_name
    tbl_name = tbl_name
    conn = sql3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE {} (codchapa INTEGER PRIMARY KEY, nome_chapa TEXT NOT NULL, veneravel TEXT NOT NULL, vigilante1 TEXT NOT NULL, vigilante2 TEXT NOT NULL, loja TEXT NOT NULL)'.format(tbl_name))
    conn.close()
    msg = "A Tabela {} foi criada no banco de dados {}".format(tbl_name, db_name)
    return(msg)

#Funcao teste Insere dados na tabela USUARIO
def insere_reg(placet, nome, datanasc, senha):
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()

    placet = placet
    nome = nome
    datanasc = str(datanasc)
    senha = str(senha)

    cursor.execute("""INSERT INTO USUARIO(placet, nome, datanasc, senha) VALUES(?,?,?,?)""",(placet, nome, datanasc, senha))
    conn.commit()
    conn.execute("PRAGMA busy_timeout = 3000")
    conn.close()
    msg = "O usuário de placet num: " + str(placet) + " Foi registrado"
    return(msg)

# Insere voto na tavela VOTO_RG
def insere_reg_voto(placet, voto, data_hora, pleito):
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()

    placet = placet
    voto = voto
    data_hora = str(data_hora)

    cursor.execute("""INSERT INTO VOTO_RG(voto, datavoto, pleito) VALUES(?,?,?)""",(voto, data_hora, pleito))
    conn.commit()
    conn.execute("PRAGMA busy_timeout = 3000")
    conn.close()
    msg = ('O voto do {} foi registrado.'.format(placet))
    return(msg)

# Insere na tabela VOTANTE_RG o placet do votante.
def insere_reg_votante(placet, voto, data_hora, pleito):
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()

    placet = placet
    voto = voto
    data_hora = str(data_hora)

    cursor.execute("""INSERT INTO VOTANTE_RG(placet, datavoto, pleito) VALUES(?,?,?)""",(placet, data_hora, pleito))
    conn.commit()
    conn.execute("PRAGMA busy_timeout = 3000")
    conn.close()
    msg = ('O voto do {} foi registrado.'.format(placet))
    return(msg)

#Insere registros na tabela CHAPAS
def insere_reg_chapa(codchapa, nome_chapa, veneravel, vigilante1, vigilante2, loja):
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    codchapa = codchapa
    nome_chapa = nome_chapa
    veneravel = veneravel
    vigilante1 = vigilante1
    vigilante2 = vigilante2
    loja = loja
    cursor.execute("""INSERT INTO CHAPAS(codchapa, nome_chapa, veneravel, vigilante1, vigilante2, loja) VALUES(?,?,?,?,?,?)""",(codchapa, nome_chapa, veneravel, vigilante1, vigilante2, loja))
    conn.commit()
    conn.execute("PRAGMA busy_timeout = 3000")
    conn.close()
    msg = "A chapa {} Foi registrada".format(nome_chapa)
    return(msg)

# Lists todos registros de uma tabela
def lists_tb(tbl_name):
    tbl_name = tbl_name
    regs_lst = []
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    #cursor.execute(""" SELECT * FROM clientes; """)
    #for linha in cursor.fetchall():
    #    print(linha)
    # Faz o mesmo trabalho que as 3 linhas acima
    for linha in cursor.execute("SELECT * FROM {}".format(tbl_name)):
        regs_lst.append(linha)
    conn.close()
    return(regs_lst)

# Altera um registro
def altera_reg(placet, nome, datanasc, senha):
    import sqlite3 as sql3
    placet = placet
    nome = nome
    datanasc = datanasc
    senha = str(senha)
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE USUARIO SET nome = ?, datanasc = ?, senha = ? WHERE placet = ?",(nome, datanasc, senha, placet))
    conn.commit()
    conn.close()
    msg = "O registro de placet numero " + str(placet) + " foi alterdo"
    return(msg)

# Apaga um registro baseado em um placet
def del_reg(placet):
    import sqlite3 as sql3
    placet = placet
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USUARIO WHERE placet = ?",(placet,))
    conn.commit()
    msg = "O usuário de placet {} foi removido".format(placet)
    #msg = 'Registro com placet numero ' + str(placet) + ' removido'
    conn.close()
    return(msg)

#Verifica a existencia de um placet
def lista_reg(placet):
    placet = placet
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute("SELECT * FROM USUARIO WHERE placet = ?",(placet,)):
        if linha[0] == placet:
            result = linha[0]
            return(result)
        else:
            result = ""
            return(result)
    conn.close()

#Verifica a existencia de um registro baseado em um placet e uma tabela
def lista_reg2(placet,tbl_name):
    placet = placet
    tbl_name = tbl_name
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute('SELECT * FROM {} WHERE placet="{}"'.format(tbl_name,placet)):
        if linha[0] == placet:
            result = linha[0]
            return(result)
        else:
            result = ""
            return(result)
    conn.close()

#Retorna um codigo de chapa se esse existir
def lista_reg_chapa(codchapa):
    codchapa = codchapa
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute("SELECT * FROM CHAPAS WHERE codchapa = ?",(codchapa,)):
        if linha[0] == codchapa:
            result = linha[0]
            return(result)
        else:
            result = ""
            return(result)
    conn.close()

#Retorna um registro inteiro baseado em um codigo de chapa
def lista_chapa(codchapa):
    codchapa = codchapa
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute("SELECT * FROM CHAPAS WHERE codchapa = ?",(codchapa,)):
        if linha[0] == codchapa:
            result = linha
            return(result)
        else:
            result = ""
            return(result)
    conn.close()

#Retorna um nome da tabela tbl_name apartir do placet    
def encontra_nome(placet,tbl_name):
    placet = placet
    tbl_name = tbl_name
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute('SELECT * FROM {} WHERE placet="{}"'.format(tbl_name,placet)):
        if linha[0] == placet:
            result = linha[1]
            return(result)
        else:
            result = ""
            return(result)
    conn.close()

# Retorna um registro da tabela usuario baseado em um placet
def ret_reg_cmpl(placet):
    placet = placet
    import sqlite3 as sql3
    conn = sql3.connect('USUARIO_ED242.db')
    cursor = conn.cursor()
    for linha in cursor.execute("SELECT * FROM USUARIO WHERE placet = ?",(placet,)):
        return(linha)
    conn.close()

# Disponibiliza arquivo para download
def get_file(bin_file, file_label='File'):
    import os
    import base64
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
