from .lista_cidadao_pec_from_fichas import lista_cidadao_pec_from_fichas
from .pessoas_id import pessoas_id
from .pessoas_list import pessoas_list

pessoas = f"""
with
	lista_cidadao_pec_from_fichas as ( {lista_cidadao_pec_from_fichas}),
	pessoas_id as ( {pessoas_id} ),
	pessoas as ( {pessoas_list} )
select
	*
from
	pessoas order by cidadao_pec asc
"""
