def gen_where_cnes_equipe(base_clause, cnes, equipe):
    clauses = []

    if base_clause:
        clauses.append(base_clause)

    if cnes:
        clauses.append(f" codigo_unidade_saude  = {cnes} ")

    if equipe:
        clauses.append(f" codigo_equipe = {equipe} ")

    return f"WHERE {' AND '.join(clauses)} " if clauses else ""
