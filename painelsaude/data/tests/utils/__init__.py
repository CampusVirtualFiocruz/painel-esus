from typing import List, Any

def join( list: List[Any], sep:str = ',') -> str:
    if not list:
        list = [ '']
        
    return f'{sep}'.join(list)

def surround( text: str, sep:str = '|') ->str :
    return f'{sep}{text}{sep}'