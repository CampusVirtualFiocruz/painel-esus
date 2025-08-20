import json

import duckdb

from .hipertension_diabetes_queries import (
    by_gender,
    by_race,
    exams_table,
    get_number_of_patients,
    get_total,
)


def test_total():
    total = duckdb.query(get_total("diabetes")).fetchone()
    total_ubs = duckdb.query(get_total("diabetes", 25)).fetchone()
    assert total[0] > total_ubs[0]

    total = duckdb.query(get_number_of_patients("diabetes")).fetchone()
    total_ubs = duckdb.query(get_number_of_patients("diabetes", 25)).fetchone()
    assert total[0] > total_ubs[0]
    assert total[1] > total_ubs[1]

def test_gender():
    total = duckdb.query(by_gender("hipertensao")).fetchall()
    assert len(total) > 0

    total = duckdb.query(by_gender("hipertensao", 25)).fetchall()
    assert len(total) > 0


def test_race():
    total = duckdb.query(by_race("hipertensao")).fetchall()
    assert len(total) > 0

    print(total)

    total = duckdb.query(by_race("hipertensao", 25)).fetchall()
    assert len(total) > 0


def test_total_exams():
    total = duckdb.query(exams_table("diabetes")).fetchall()
    assert len(total) > 0

    print(json.dumps(total, indent=4))
