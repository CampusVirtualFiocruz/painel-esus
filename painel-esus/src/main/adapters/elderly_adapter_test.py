from tkinter import E
from .elderly_adapter import ElderlyAdapter
from src.infra.db.repositories.elderly.elderly_repository import ElderlyRepository

repo = ElderlyRepository()
adapter = ElderlyAdapter()

def test_by_gender():
    resp = repo.by_gender()
    result = adapter.by_gender(resp)
    print(result)
    
def test_by_race():
    resp = repo.by_race()
    result = adapter.by_race(resp)
    print(result)    
    
def test_medical_appointment():
    resp = repo.medical_appointment()
    result = adapter.two_medical_appointment(resp)
    print(result)     
    
def test_height_records():
    resp = repo.height_records()
    result = adapter.two_height_records(resp)
    print(result)   
    
def test_acs_visits():
    resp = repo.acs_visits()
    result = adapter.two_acs_visits(resp)
    print(result)  

def test_dentist():
    resp = repo.dentist_appointment()
    result = adapter.dentist_appointment(resp)
    print(result)
    
def test_creatinine():
    resp = repo.creatinine()
    result = adapter.creatinine(resp)
    print(result)
    
def test_influenza():
    resp = repo.influenza_vaccines()
    result = adapter.influenza_vaccines(resp)
    print(result)    
    
def test_ivcf_20():
    resp = repo.ivcf_20()
    result = adapter.ivcf_20(resp)
    print(result)     
    
    
def test_card():
    resp = repo.total_card()
    result = adapter.total_card(resp)
    print(result)         