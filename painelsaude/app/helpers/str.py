import os
import re

def treatNames( str='' ):
    check = os.getenv('ANONIMIZAR', False)
    
    if check and str:
        return re.sub(r'[a-zA-Z0-9]', '*', str)
    return str

def strToData( data ):
    if data is not None:
        return f'{data[:4]}-{data[4:6]}-{data[6:8]} 00:00:00'
    return ''