from .cidadao_equipe import cidadao_equipe
from .equipes_join import equipes_join

equipes = f"""
with
	cidadao_equipe as ( {cidadao_equipe} ),
	equipes as ( {equipes_join} ) 
select
	*
from
	equipes
"""
