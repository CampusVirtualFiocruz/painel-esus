
from enum import Enum

class AcuteInfectionType(Enum):
    INFECCOES=1
    EXANTEMATICA=2
    RESPIRATORIA=3
    INESPECIFICA=4
    GASTROINTESTINAL=5
    
    def get_label(value):
        return {
            1: 'Infecções',
            2: 'Exantemática',
            3: 'Respiratória',
            4: 'Inespecífica',
            5: 'Gastrointestinal',
        }[value]
  
class DiseaseCode:
    def __init__(
        self,
        code: str,
        description: str,
        type: str
) -> None:
        self.code = code
        self.description = description
        self.type = type
        
class Cid(DiseaseCode):
    def __init__(self, code: str, description: str, type: str) -> None:
        super().__init__(code, description, type)
        
class Ciap(DiseaseCode):
    def __init__(self, code: str, description: str, type: str) -> None:
        super().__init__(code, description, type)        
        
  
class DiseaseCodeMeta(type):
    
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            header = True
            with open('../../../files/Infeccoes_agudas_sindromes.csv', 'r') as f:
                while 1:
                    row = f.readline()
                    if not row:
                        break
                    if not header:
                        row = row.split(",")
                        if row[0].strip() == "CID":
                            cls._instances[cls].list.append(
                                Cid(
                                    code=row[1].strip(),
                                    description=row[2].strip(),
                                    type=row[4].strip()
                                )
                            )
                            cls._instances[cls].list.append(
                                Ciap(
                                    code=row[3].strip(),
                                    description=row[2].strip(),
                                    type=row[4].strip()
                                )
                            )
                        elif row[0].strip() == "CIAP":
                            cls._instances[cls].list.append(
                                Ciap(
                                    code=row[3].strip(),
                                    description=row[2].strip(),
                                    type=row[4].strip()
                                )
                            )
                    else:
                        header = False
        return cls._instances[cls]        
       
class AcuteInfectionsCollection(metaclass=DiseaseCodeMeta):
    list = []
    
    def __init__(self) -> None:
        pass
    
    def __str__(self) -> str:
        return [ str(cbo) for cbo in self.list]