# CARD DA LISTA NOMINAL
# Classificação do estado nutricional da última consulta

from typing import Optional

import polars as pl


def classificar_estado_nutricional(
    sexo: str, 
    idade_meses: int, 
    peso_kg: Optional[float]
) -> int:
    """Classifica o estado nutricional com base nas regras fornecidas."""
    
    if peso_kg is None:
        return 5  # Sem registro do peso
    
    sexo = sexo.upper()
    
    # Verifica se a idade está dentro do intervalo válido (0-36 meses)
    if idade_meses < 0 or idade_meses > 36:
        return 5  # Considera como sem registro se idade fora do intervalo
    
    # Dicionários com os limites para cada classificação
    limites_feminino = {
        1: {  # Peso elevado
            0: 4.2, 1: 5.5, 2: 6.6, 3: 7.5, 4: 8.2, 5: 8.8, 6: 9.3, 7: 9.8, 8: 10.2, 9: 10.5,
            10: 10.9, 11: 11.2, 12: 11.5, 13: 11.8, 14: 12.1, 15: 12.4, 16: 12.6, 17: 12.9,
            18: 13.2, 19: 13.5, 20: 13.7, 21: 14.0, 22: 14.3, 23: 14.6, 24: 14.8, 25: 15.1,
            26: 15.4, 27: 15.7, 28: 16.0, 29: 16.2, 30: 16.5, 31: 16.8, 32: 17.1, 33: 17.3,
            34: 17.6, 35: 17.9, 36: 18.1
        },
        2: {  # Peso adequado (limites inferiores)
            0: 2.4, 1: 3.2, 2: 3.9, 3: 4.5, 4: 5.0, 5: 5.4, 6: 5.7, 7: 6.0, 8: 6.3, 9: 6.5,
            10: 6.7, 11: 6.9, 12: 7.0, 13: 7.2, 14: 7.4, 15: 7.6, 16: 7.7, 17: 7.9, 18: 8.1,
            19: 8.2, 20: 8.4, 21: 8.6, 22: 8.7, 23: 8.9, 24: 9.0, 25: 9.2, 26: 9.4, 27: 9.5,
            28: 9.7, 29: 9.8, 30: 10.0, 31: 10.1, 32: 10.3, 33: 10.4, 34: 10.5, 35: 10.7, 36: 10.8
        },
        3: {  # Baixo peso (limites inferiores)
            0: 2.0, 1: 2.7, 2: 3.4, 3: 4.0, 4: 4.4, 5: 4.8, 6: 5.1, 7: 5.3, 8: 5.6, 9: 5.8,
            10: 5.9, 11: 6.1, 12: 6.3, 13: 6.4, 14: 6.6, 15: 6.7, 16: 6.9, 17: 7.0, 18: 7.2,
            19: 7.3, 20: 7.5, 21: 7.6, 22: 7.8, 23: 7.9, 24: 8.1, 25: 8.2, 26: 8.4, 27: 8.5,
            28: 8.6, 29: 8.8, 30: 8.9, 31: 9.0, 32: 9.1, 33: 9.3, 34: 9.4, 35: 9.5, 36: 9.6
        }
    }
    
    limites_masculino = {
        1: {  # Peso elevado
            0: 4.4, 1: 5.8, 2: 7.1, 3: 8.0, 4: 8.7, 5: 9.3, 6: 9.8, 7: 10.3, 8: 10.7, 9: 11.0,
            10: 11.4, 11: 11.7, 12: 12.0, 13: 12.3, 14: 12.6, 15: 12.8, 16: 13.1, 17: 13.4,
            18: 13.7, 19: 13.9, 20: 14.2, 21: 14.5, 22: 14.7, 23: 15.0, 24: 15.3, 25: 15.5,
            26: 15.8, 27: 16.1, 28: 16.3, 29: 16.6, 30: 16.9, 31: 17.1, 32: 17.4, 33: 17.6,
            34: 17.8, 35: 18.1, 36: 18.3
        },
        2: {  # Peso adequado (limites inferiores)
            0: 2.5, 1: 3.4, 2: 4.3, 3: 5.0, 4: 5.6, 5: 6.0, 6: 6.4, 7: 6.7, 8: 6.9, 9: 7.1,
            10: 7.4, 11: 7.6, 12: 7.7, 13: 7.9, 14: 8.1, 15: 8.3, 16: 8.4, 17: 8.6, 18: 8.8,
            19: 8.9, 20: 9.1, 21: 9.2, 22: 9.4, 23: 9.5, 24: 9.7, 25: 9.8, 26: 10.0, 27: 10.1,
            28: 10.2, 29: 10.4, 30: 10.5, 31: 10.7, 32: 10.8, 33: 10.9, 34: 11.0, 35: 11.2, 36: 11.3
        },
        3: {  # Baixo peso (limites inferiores)
            0: 2.1, 1: 2.9, 2: 3.8, 3: 4.4, 4: 4.9, 5: 5.3, 6: 5.7, 7: 5.9, 8: 6.2, 9: 6.4,
            10: 6.6, 11: 6.8, 12: 6.9, 13: 7.1, 14: 7.2, 15: 7.4, 16: 7.5, 17: 7.7, 18: 7.8,
            19: 8.0, 20: 8.1, 21: 8.2, 22: 8.4, 23: 8.5, 24: 8.6, 25: 8.8, 26: 8.9, 27: 9.0,
            28: 9.1, 29: 9.2, 30: 9.4, 31: 9.5, 32: 9.6, 33: 9.7, 34: 9.8, 35: 9.9, 36: 10.0
        }
    }
    
    if sexo == 'FEMININO':
        # Verifica peso elevado (classificação = 1)
        if peso_kg > limites_feminino[1].get(idade_meses, float('inf')):
            return 1
        
        # Verifica peso adequado (classificação = 2)
        lim_inf = limites_feminino[2].get(idade_meses, 0)
        lim_sup = limites_feminino[1].get(idade_meses, float('inf'))
        if lim_inf <= peso_kg <= lim_sup:
            return 2
        
        # Verifica baixo peso (classificação = 3)
        lim_inf = limites_feminino[3].get(idade_meses, 0)
        lim_sup = limites_feminino[2].get(idade_meses, float('inf'))
        if lim_inf <= peso_kg < lim_sup:
            return 3
        
        # Muito baixo peso (classificação = 4)
        return 4
    
    elif sexo == 'MASCULINO':
        # Verifica peso elevado (classificação = 1)
        if peso_kg > limites_masculino[1].get(idade_meses, float('inf')):
            return 1
        
        # Verifica peso adequado (classificação = 2)
        lim_inf = limites_masculino[2].get(idade_meses, 0)
        lim_sup = limites_masculino[1].get(idade_meses, float('inf'))
        if lim_inf <= peso_kg <= lim_sup:
            return 2
        
        # Verifica baixo peso (classificação = 3)
        lim_inf = limites_masculino[3].get(idade_meses, 0)
        lim_sup = limites_masculino[2].get(idade_meses, float('inf'))
        if lim_inf <= peso_kg < lim_sup:
            return 3
        
        # Muito baixo peso (classificação = 4)
        return 4
    
    else:
        return 5  # Sexo não reconhecido





def processar_dados_nutricionais(df: pl.DataFrame) -> pl.DataFrame:
    """Processa os dados e adiciona a classificação nutricional."""
    # Primeiro aplique a classificação numérica
    df = df.with_columns(
        pl.struct(['sexo', 'idade_meses', 'nu_peso_recente']).map_elements(
            lambda x: classificar_estado_nutricional(
                x['sexo'], 
                x['idade_meses'], 
                x['nu_peso_recente']
            ),
            return_dtype=pl.Int64
        ).alias('classificacao_nutricional')
    )
    
    # Depois adicione a descrição textual (agora com o mapeamento correto)
    classificacao_map = {
        1: "Peso elevado para a idade",
        2: "Peso adequado para a idade",
        3: "Baixo peso para a idade",
        4: "Muito baixo peso para a idade",
        5: "Sem registro do peso"
    }
    
    return df.with_columns(
        pl.col('classificacao_nutricional').replace(classificacao_map, default=None).alias('descricao_classificacao')
    )