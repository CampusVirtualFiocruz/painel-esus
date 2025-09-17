"""Crianças.

Consultas relacionadas ao acompanhamento de crianças
(consultas, visitas de Agente Comunitário de Saúde (ACS), odontologia, marcos do desenvolvimento
etc.).

Responsabilidades principais:
- Totais (crianças atendidas/cadastradas) e séries de 12 meses.
- Distribuiçao por faixa etária e por raça/cor.
- Indicadores específicos (primeira consulta em 8 dias, consultas até 2 anos,
  visitas de Agente Comunitário de Saúde (ACS) em 30 dias/6 meses, registros de peso e altura, marcos, alimentação
  avaliada, procedimentos odontológicos).
- Listas nominais com paginação e exportação anonimizadas.
"""

import duckdb
from src.infra.db.repositories.utils.str_utils import anonymize_data_frame
from src.infra.db.settings.connection_duckdb import DuckDbHandler

from .sqls.children_queries import (
    get_medical_cares,
    get_total_card,
    get_total_ubs,
    sql_acs_visit_until_6m,
    sql_acs_visit_until_30d,
    sql_appointments_until_2_years,
    sql_by_age_children,
    sql_by_race_children,
    sql_dental_appointments_until_12m,
    sql_dental_appointments_until_24m,
    sql_evaluated_feeding,
    sql_first_consult_8d,
    sql_get_nominal_list,
    sql_get_nominal_list_download,
    sql_high_weight_records,
    sql_milestone,
    sql_total_and_last_12_months,
)


class ChildrenRepository:
    """Implementa operações de leitura de dados de Crianças."""

    def __init__(self):
        self.session = DuckDbHandler()

    def total_card(
        self, cnes: int = None, equipe: int = None, category: str = "atentidas"
    ):
        """Retorna totais agrupado por localização."""
        sql = get_total_card(cnes, equipe)
        return self.session.fetchall(sql)

    def get_total_children(self, cnes: int = None, equipe: int = None):
        """Retorna total de crianças por UBS/equipe."""
        return self.session.fetchall(get_total_ubs(cnes, equipe))

    def get_total_twelve_months_children(self, cnes: int = None, equipe: int = None):
        """Retorna acumulado e último 12 meses de crianças atendidas."""
        return self.session.fetchall(sql_total_and_last_12_months(cnes, equipe))

    def get_by_age(self, cnes: int = None, equipe: int = None):
        """Indicadores por faixa etária."""
        return self.session.fetchall(sql_by_age_children(cnes, equipe))

    def get_by_race(self, cnes: int = None, equipe: int = None):
        """Indicadores por raça/cor."""
        return self.session.fetchall(sql_by_race_children(cnes, equipe))

    def total_medical_cares(self, cnes: int = None, equipe: int = None):
        """Total de atendimentos médicos para o público infantil."""
        sql = get_medical_cares(cnes, equipe)
        con = duckdb.connect()
        result = con.sql(sql).fetchall()
        return result

    def get_first_consult_8d(self, cnes: int = None, equipe: int = None):
        """Total de primeira consulta em até 8 dias de vida."""
        return self.session.fetchall(sql_first_consult_8d(cnes, equipe))

    def get_appointments_until_2_years(self, cnes: int = None, equipe: int = None):
        """Atendimentos até os 2 anos de idade."""
        return self.session.fetchall(sql_appointments_until_2_years(cnes, equipe))

    def get_acs_visit_until_30d(self, cnes: int = None, equipe: int = None):
        """Visitas de ACS até 30 dias do nascimento."""
        return self.session.fetchall(sql_acs_visit_until_30d(cnes, equipe))

    def get_acs_visit_until_6m(self, cnes: int = None, equipe: int = None):
        """Visitas de ACS até 6 meses de vida."""
        return self.session.fetchall(sql_acs_visit_until_6m(cnes, equipe))

    def get_dental_appointments_until_12m(self, cnes: int = None, equipe: int = None):
        """Consultas odontológicas até 12 meses."""
        return self.session.fetchall(sql_dental_appointments_until_12m(cnes, equipe))

    def get_dental_appointments_until_24m(self, cnes: int = None, equipe: int = None):
        """Consultas odontológicas até 24 meses."""
        return self.session.fetchall(sql_dental_appointments_until_24m(cnes, equipe))

    def get_high_weight_records(self, cnes: int = None, equipe: int = None):
        """Registros de peso e altura no acompanhamento infantil."""
        return self.session.fetchall(sql_high_weight_records(cnes, equipe))

    def get_milestone(self, cnes: int = None, equipe: int = None):
        """Indicadores de marco do desenvolvimento."""
        return self.session.fetchall(sql_milestone(cnes, equipe))

    def get_evaluated_feeding(self, cnes: int = None, equipe: int = None):
        """Avaliação de alimentação em consultas/visitas."""
        return self.session.fetchall(sql_evaluated_feeding(cnes, equipe))

    def get_nominal_list(
        self,
        cnes: int = None,
        equipe: int = None,
        page: int = 0,
        page_size: int = 10,
        nome: str = None,
        cpf: str = None,
        nome_unidade_saude: int = None,
        q: str = None,
        sort: list[dict] = None,
    ) -> list[dict]:
        """Retorna lista nominal (items e metadados de paginação).

        Parâmetros:
        - cnes, equipe: filtros por unidade e equipe.
        - page, pagesize: paginação.
        - nome, cpf, query (q): filtros de busca textual (query aplica em
          múltiplas colunas como nome/CPF/CNS).
        - sort: lista de dicts com chaves field e direction.
        """

        try:
            page = int(page)
        except (TypeError, ValueError):
            page = 0

        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            page_size = 10

        query = sql_get_nominal_list(
            cnes=cnes,
            equipe=equipe,
            page=page,
            page_size=page_size,
            nome=nome,
            cpf=cpf,
            nome_unidade_saude=nome_unidade_saude,
            q=q,
            sort=sort,
        )

        result = self.session.fetchall(query)
        columns = [col[0] for col in self.session.get_description()]
        items = [dict(zip(columns, row)) for row in result]

        count_query = (
            sql_get_nominal_list(
                cnes=cnes,
                equipe=equipe,
                page=page,
                page_size=page_size,
                nome=nome,
                cpf=cpf,
                nome_unidade_saude=nome_unidade_saude,
                sort=sort,
            )
            .replace("SELECT *", "SELECT COUNT(*) as total")
            .split("ORDER BY")[0]
        )

        total = self.session.fetchone(count_query)[0]

        return {
            "items": items,
            "itemsCount": total,
            "itemsPerPage": page_size,
            "page": page,
            "pagesCount": (total + page_size - 1) // page_size,
        }

    def get_nominal_list_download(self, cnes: int = None, equipe: int = None):
        """Gera DataFrame para exportação da lista nominal.

        Os dados sensíveis são anonimizados.
        """
        response = self.session.fetch_df(sql_get_nominal_list_download(cnes, equipe))
        response = response.apply(anonymize_data_frame, axis=1)
        return response
