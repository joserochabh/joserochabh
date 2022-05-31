import numpy as np
import Lbs001
import sqlite3 as sql3

db_name = 'USUARIO_ED242.db'
# Cria tabela VOTOS_RG
Lbs001.cria_tbl_voto(db_name, 'VOTO_RG')

# Cria tabela VOTANTE_RG
Lbs001.cria_tbl_votante(db_name, 'VOTANTE_RG')