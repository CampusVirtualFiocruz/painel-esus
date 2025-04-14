def get_elderly_base():
    return f"""
    select * from read_parquet('./dados/output/idoso.parquet')
"""