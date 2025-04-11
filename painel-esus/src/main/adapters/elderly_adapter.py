# pylint: disable=C0103
from src.main.adapters.nominal_list_adapter import IdosoNominalListAdapter
from pprint import pprint

class ElderlyAdapter:

    def total_ubs(self, response):
        total= 0 
        if response is not None and len(response) > 0:
            total = response[0][0]
        
        return {
                'data': total,
            }
        
    def total_medical_cares(self, response):
        total= 0 
        if response is not None and len(response) > 0:
            total = response[0][0]
        
        return {
                'data': total,
            }
    
    def by_gender(self, response):
        result = { "data": [] }
        map_ = {}
        for resp in response:
            if resp[0] is not None and resp[1] is not None and resp[2] is not None:
                if resp[0] not in map_:
                    map_[resp[0]] = {
                        'feminino': 0,
                        'masculino': 0,
                        'indeterminado': 0
                    }
                
                map_[resp[0]][str(resp[1]).lower()] = resp[2]
        
        for key in map_.keys():
            _key = key.replace("a","-")
            _key += '-anos'
            value ={
                "tag": _key,
                "value": map_[key]
            }
            result["data"].append(value)
        
       
        return result
        
    def by_race(self, response):
        result = { "data": [] }
        map_ = {}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                result["data"].append({
                    "tag": str(resp[0]).lower(),
                    "value": resp[1]
                })
       
        return result
    
        
        
    def two_medical_appointment(self, response):
        result = {"data": [
            { "tag": "um-nenhum-registro", "value": 0},
            { "tag": "dois-mais-registros", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
    def two_height_records(self, response):
        result = {"data": [
            { "tag": "um-nenhum-registro", "value": 0},
            { "tag": "dois-mais-registros", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
    def two_acs_visits(self, response):
        result = {"data": [
            { "tag": "uma-nenhuma-visita", "value": 0},
            { "tag": "duas-mais-visitas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
                
    def creatinine(self, response):
        result = {"data": [
            { "tag": "sem-avaliacao", "value": 0},
            { "tag": "avaliadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
        
    def influenza_vaccines(self, response):
        result = {"data": [
            { "tag": "nao-vacinadas", "value": 0},
            { "tag": "vacinadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
        
    def dentist_appointment(self, response):
        result = {"data": [
            { "tag": "sem-consulta", "value": 0},
            { "tag": "consultadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
    
    def ivcf_20(self, response):
        result = {"data": [
            { "tag": "sem-avaliacao", "value": 0},
            { "tag": "avaliadas", "value": 0},
        ]}
        for resp in response:
            if resp[0] is not None and resp[1] is not None:
                if resp[0] == 0:
                    result['data'][0]['value'] = resp[1]
                else:
                    result['data'][1]['value'] = resp[1]
        
        return result
        
    def nominal_list(self, response):
        return IdosoNominalListAdapter(response)