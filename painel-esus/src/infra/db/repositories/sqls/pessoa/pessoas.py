from .pessoas_id import pessoas_id
from .pessoas_list import pessoas_list

pessoas = f"""
with
	pessoas_id as ( {pessoas_id} ),
	pessoas as ( {pessoas_list} )
select
	*
from
	pessoas order by cidadao_pec asc
"""
