from .oral_health_queries import (
    first_appointment,
    conclued_treatment,
    extraction
)
import duckdb

def run(sql):
    con = duckdb.connect()
    return con.sql(sql).fetchall()
    
def test_first_appointment():
    sql = first_appointment(None, None, 'atendidas')
    result1 = run(sql)
    print(result1)
    
    sql = first_appointment(26, None, 'atendidas')
    result2 = run(sql)
    print(result2)
    
    assert result1[0][1] > result2[0][1]
    
def test_conclued_treatment():
    sql = conclued_treatment(None, None, 'atendidas')
    result1 = run(sql)
    print(result1)
    
    sql = conclued_treatment(26, None, 'atendidas')
    result2 = run(sql)
    print(result2)
    
    assert result1[0][1] > result2[0][1]    
    
def test_extraction():
    sql = extraction(None, None, 'atendidas')
    result1 = run(sql)
    print(result1)
    
    sql = extraction(26, None, 'atendidas')
    result2 = run(sql)
    print(result2)
    
    assert result1[0][1] > result2[0][1]      