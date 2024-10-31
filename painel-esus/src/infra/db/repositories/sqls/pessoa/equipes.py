from .cidadao_equipe import cidadao_equipe
from .equipes_join import equipes_join
from .pessoas_id import pessoas_id
equipes = f"""
with
	pessoas_id as ( {pessoas_id} ),
	cidadao_equipe as ( {cidadao_equipe} ),
	equipes as ( {equipes_join} ) 
select
	*
from
	equipes
"""
