from .cidadao_equipe import cidadao_equipe
from .equipes_join import equipes_join
from .lista_cidadao_pec_from_fichas import lista_cidadao_pec_from_fichas
from .pessoas_id import pessoas_id

equipes = f"""
with
	cidadao_equipe as ( {cidadao_equipe} ),
	equipes as ( {equipes_join} ) 
select
	*
from
	equipes
"""
