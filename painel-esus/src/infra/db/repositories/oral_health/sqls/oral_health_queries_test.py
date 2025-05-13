import duckdb

from .oral_health_queries import (
    by_gender,
    by_race,
    conclued_treatment,
    extraction,
    first_appointment,
    get_total_card,
    get_total_ubs,
)


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

def test_by_race():
    sql = by_race(None, None, 'atendidas')
    result1 = run(sql)
    print(result1)

    sql = by_race(26, None, 'atendidas')
    result2 = run(sql)
    print(result2)

    assert result1[0][1] > result2[0][1]  


def test_by_gender():
    sql = by_gender(None, None, "atendidas")
    result1 = run(sql)

    sql = by_gender(26, None, "atendidas")
    result2 = run(sql)

    assert result1[1][2] > result2[1][2]


def test_by_total():
    sql = get_total_card(None, None)
    con = duckdb.connect()
    result1 = run(sql)
    print(result1)

    # sql = get_medical_cares(None, None)
    # con = duckdb.connect()
    # result1 = run(sql)

    result1 = {
        "atendidas": run(get_total_ubs(None, None, "atendidas"))[0][0],
        "cadastradas": run(get_total_ubs(None, None, "cadastradas"))[0][0],
    }
    print(result1)
