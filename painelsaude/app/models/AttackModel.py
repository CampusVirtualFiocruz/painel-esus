from .CheckPresense import CheckPresence, PipelineModel
import re
import traceback
import sys


class BaseDiseaseModel(CheckPresence):
    def __init__(self, cids):
        self.cids = set(cids)
        self.total = 0

    def checkPresence(self, row):
        pattern = r'\W+'
        cids = set(re.split(pattern, row['ds_filtro_cids']))
        ciaps = set(re.split(pattern, row['ds_filtro_ciaps']))
        # print( cids )
        cidsPresence = self.cids & cids
        ciapsPresence = self.cids & ciaps
        if len(cidsPresence) > 0 or len(ciapsPresence) > 0:
            # print(row['ds_filtro_cids'])
            self.total += 1

    def calcPercent(self):
        percent = round((self.total/self.totalRegistro)*100, 2)
        return [percent, 100-percent]

    def toJson(self):
        percent = self.calcPercent()
        return {
            self.label: {
                "com_consulta": percent[0],
                "com_consulta_abs": self.total,
                "sem_consulta": percent[1],
                "sem_consulta_abs": self.totalRegistro,

            }
        }


class HeartAttack(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['I21', 'I21.0', 'I21.1', 'I21.2',  'I21.3', 'I21.4', 'I21.9',
                         'I210', 'I211', 'I212', 'I213', 'I214', 'I219'])
        self.label = 'Infarto Agudo do Miocárdio'
        self.totalRegistro = totalRegistro


class BrainStroke(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['I64'])
        self.label = 'Acidente Vascular Encefálico'
        self.totalRegistro = totalRegistro


class KidneyDisease(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['I12', 'I129', 'I13', 'I130', 'I131', 'I132', 'I139', 'N083',
                          'N179', 'N18', 'N180', 'N188', 'N189', 'N19', 'U14', 'U99',
                          'U88', 'U90'])
        self.label = 'Doença renal'
        self.totalRegistro = totalRegistro


class CoronaryDisease(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['I24', 'I248', 'I249', 'I25', 'I251', 'I258', 'I259', 'I518',
                          'I519', 'I110', 'I119', 'I130', 'I132', 'I50', 'I500', 'I509'])
        self.label = 'Doença Coronariana'
        self.totalRegistro = totalRegistro


class VascularBrainDisease(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['G46', 'G468', 'I67', 'I678',
                          'I679', 'I68', 'I688', 'I69', 'I699'])
        self.label = 'Doença Cerebrovascular'
        self.totalRegistro = totalRegistro


class DiabeticRetinopathy(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['H360', 'F83'])
        self.label = 'Retinopatia diabética'
        self.totalRegistro = totalRegistro


class Neuropathy(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['G57', 'G578', 'G579', 'G58', 'G590', 'G598', 'G61', 'G628',
                          'G629', 'G63', 'G632', 'G633'])
        self.label = 'Neuropatia'
        self.totalRegistro = totalRegistro


class OcclusiveArterialDisease(BaseDiseaseModel):
    def __init__(self, totalRegistro):
        super().__init__(['I73', 'I738', 'I739'])
        self.label = 'Doença Arterial Oclusiva'
        self.totalRegistro = totalRegistro


class HeartAttackModel(PipelineModel):
    def __init__(self, totalRegistros):
        super().__init__()
        self.list = [
            HeartAttack(totalRegistros),
            BrainStroke(totalRegistros),
            KidneyDisease(totalRegistros),
            CoronaryDisease(totalRegistros),
            VascularBrainDisease(totalRegistros)
        ]


class DiabeticDiseaseModel(PipelineModel):
    def __init__(self, totalRegistros):
        super().__init__()
        self.list = [
            DiabeticRetinopathy(totalRegistros),
            KidneyDisease(totalRegistros),
            CoronaryDisease(totalRegistros),
            VascularBrainDisease(totalRegistros),
            Neuropathy(totalRegistros),
            OcclusiveArterialDisease(totalRegistros)
        ]


class SummaryPipelineModel(PipelineModel):
    def __init__(self) -> None:
        super().__init__()
        self.result = []

    def checkPresence(self, obj, row):
        pattern = r'\W+'
        cids = set(re.split(pattern, row['ds_filtro_cids']))
        ciaps = set(re.split(pattern, row['ds_filtro_ciaps']))
        cidsPresence = obj.cids & cids
        ciapsPresence = obj.cids & ciaps
        if len(cidsPresence) > 0 or len(ciapsPresence) > 0:
            return True
        return False


class HeartAttackSummaryModel(SummaryPipelineModel):
    def __init__(self, totalRegistros, base):
        super().__init__()
        self.list = [
            HeartAttack(totalRegistros),
            BrainStroke(totalRegistros),
            KidneyDisease(totalRegistros),
            CoronaryDisease(totalRegistros),
            VascularBrainDisease(totalRegistros)
        ]

    def pipelineFn(self, row):

        res = {
            "nome": row["nome"],
            "idade": row["nu_idade"],
            "Infarto Agudo do Miocárdio": False,
            "Acidente Vascular Encefálico": False,
            "Doença renal": False,
            "Doença Coronariana": False,
            "Doença Cerebrovascular": False,
        }
        map_key = {
            "0": "Infarto Agudo do Miocárdio",
            "1": "Acidente Vascular Encefálico",
            "2": "Doença renal",
            "3": "Doença Coronariana",
            "4": "Doença Cerebrovascular",
        }
        try:
            for idx, i in enumerate(self.list):
                if self.checkPresence(i, row):
                    res[map_key[str(idx)]] = True
        except Exception as ex:
            traceback.print_exc(file=sys.stdout)

        self.result.append(res)


class DiabeticDiseaseSummaryModel(SummaryPipelineModel):
    def __init__(self, totalRegistros, base):
        super().__init__()
        self.list = [
            DiabeticRetinopathy(totalRegistros),
            KidneyDisease(totalRegistros),
            CoronaryDisease(totalRegistros),
            VascularBrainDisease(totalRegistros),
            Neuropathy(totalRegistros),
            OcclusiveArterialDisease(totalRegistros)
        ]

    def pipelineFn(self, row):

        res = {
            "nome": row["nome"],
            "idade": row["nu_idade"],
            "Retinopatia diabética": False,
            "Doença renal": False,
            "Doença Coronariana": False,
            "Doença Cerebrovascular": False,
            "Neuropatia": False,
            "Doença Arterial Oclusiva": False,
        }
        map_key = {
            "0": "Retinopatia diabética",
            "1": "Doença renal",
            "2": "Doença Coronariana",
            "3": "Doença Cerebrovascular",
            "4": "Neuropatia",
            "5": "Doença Arterial Oclusiva",
        }
        try:
            for idx, i in enumerate(self.list):
                if self.checkPresence(i, row):
                    res[map_key[str(idx)]] = True
        except Exception as ex:
            traceback.print_exc(file=sys.stdout)

        self.result.append(res)
