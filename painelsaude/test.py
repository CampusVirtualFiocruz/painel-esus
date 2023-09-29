import os
from app import app
from app.models.BaseConfig import BaseConfig
from app.models.conexao import Conexao
from app.models.infections.individual_care import get_invidual_cares, get_invidual_cares_not_in, get_all_cares

host = os.getenv('HOST',)
dataBase = os.getenv('DATABASE')
user = os.getenv('USER')
passwd = os.getenv('PASSWORD')
port = os.getenv('PORT')

con = Conexao( host, dataBase,  user, passwd, port)
infeccoes = ['D09',
 'S76',
 'S02',
 'D10',
 'J960',
 'D70',
 'R53',
 'R438',
 'M791',
 'A084',
 'D01',
 'R508',
 'R33',
 'J04',
 'R82',
 'J100',
 'J06',
 'J12',
 'A09',
 'J159',
 'A03',
 'J111',
 'R529',
 'R77',
 'J00',
 'J16',
 'R74',
 'U04',
 'U071',
 'R21',
 'J02',
 'L18',
 'B972',
 'R80',
 'J03',
 'R05',
 'J09',
 'D11',
 'A90',
 'J18',
 'R08',
 'R50',
 'R97',
 'R509',
 'J029',
 'R01',
 'J118',
 'J158',
 'J14',
 'R28',
 'A01',
 'A08',
 'J10',
 'J969',
 'R430',
 'B34',
 'J399',
 'L20',
 'R431',
 'R76',
 'M255',
 'D06',
 'R43',
 'A76',
 'J15',
 'R520',
 'J459',
 'B97',
 'R07',
 'B349',
 'A92',
 'R11',
 'R02',
 'S29',
 'J96',
 'U049',
 'J13',
 'R81',
 'B342',
 'R432',
 'A77',
 'R96',
 'R83',
 'J11',
 'U072',
 'R04',
 'J039',
 'J17']

dt = get_invidual_cares(con, [], infeccoes)#.to_csv('/tmp/atendimentos.csv')

todos = get_all_cares(con, [])

todos_size = todos.shape[0]
in_size = len(dt.co_seq_fat_atd_ind.unique().tolist())
print( f'Todos atendimentos: {todos_size}')

dt2 = get_invidual_cares_not_in(con, [], infeccoes)#.to_csv('/tmp/atendimentos_no.csv')
not_in_size = dt2.shape[0]

print( f'Todos atendimentos NOT IN: {not_in_size}')
print( f'Todos atendimentos IN: {in_size}')

assert (in_size+not_in_size) == todos_size
# dt_in = dt.co_seq_fat_atd_ind.unique().tolist()
# dt_not = dt2.co_seq_fat_atd_ind.unique().tolist()
# print(dt2.head())

