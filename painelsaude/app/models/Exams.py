from .CheckPresense import CheckPresence, PipelineModel
import re
import traceback
import sys
from collections import OrderedDict
from operator import getitem


class ExamStatus:
    def __init__(self):
        self.evaluated = 0
        self.requested = 0

    def checkPresence(self, row):

        if len(self.exams) == 0:
            return
        pattern = r'\W+'
        evaluatedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_avaliados']))
        requestedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_solicitados']))

        evaluatedProceduresPresence = self.exams & evaluatedProcedures
        # print(evaluatedProceduresPresence)
        requestedProceduresPresence = self.exams & requestedProcedures
        """
    - se o código do exame não estiver nas colunas solicitado e avaliado, 
    soma 1 solicitação pendente para o exame;
    """
        if len(requestedProceduresPresence) == 0 and len(evaluatedProceduresPresence) == 0:
            self.requested += 1
        else:
            """
            - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado,
            conta pendente nos avaliados do exame; 
            """
            if len(requestedProceduresPresence) > 0 and len(evaluatedProceduresPresence) == 0:
                self.evaluated += 1

    def toJson(self):
        return {
            "avaliados": self.evaluated,
            "solicitados": self.requested,
            "tipo": self.label
        }


class BloodPressure(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0301100039'])
        self.label = 'Aferição de PA'


class BloodGlucose(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010473', '0202010295', 'ABEX026'])
        self.label = 'Glicemia'


class Creatinine(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010317', 'ABEX003'])
        self.label = 'Creatinina'


class Urine(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010017', 'ABEX027'])
        self.label = 'EAS/EQU (urina rotina)'


class SodiumPotassium(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010635', '0202010600'])
        self.label = 'Sódio e potássio'


class TotalCholesterol(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010295'])
        self.label = 'Colesterol total'


class BloodCount(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202020380', 'ABEX028'])
        self.label = 'Hemograma'


class ECG(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0211020036'])
        self.label = 'Eletrocardiograma'


class Retinography(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0211060178', 'ABEX013'])
        self.label = 'Retinografia'


class GlycatedHemoglobin(ExamStatus):
    def __init__(self):
        super().__init__()
        self.exams = set(['0202010503', 'ABEX008'])
        self.label = 'Hemoglobina glicada'


class ArterialHypertensionExamsList():
    def __init__(self):
        self._res = []
        self.list = [
            BloodPressure(),
            BloodGlucose(),
            Creatinine(),
            Urine(),
            SodiumPotassium(),
            TotalCholesterol(),
            BloodCount(),
            ECG()
        ]

    def pipelineFn(self, row):
        for i in self.list:
            i.checkPresence(row)

    def getResponse(self):
        result = []
        for i in self.list:
            result.append(i.toJson())

        return result

    def checkPresence(self, exams, row, res, idx):

        if len(exams) == 0:
            return res
        pattern = r'\W+'
        evaluatedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_avaliados']))
        requestedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_solicitados']))

        evaluatedProceduresPresence = exams & evaluatedProcedures
        # print(evaluatedProceduresPresence)
        requestedProceduresPresence = exams & requestedProcedures
        """
    - se o código do exame não estiver nas colunas solicitado e avaliado, 
    soma 1 solicitação pendente para o exame;
    """
        if len(requestedProceduresPresence) == 0 and len(evaluatedProceduresPresence) == 0:
            res[idx][0] = 1
        else:
            """
            - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado,
            conta pendente nos avaliados do exame; 
            """
            if len(requestedProceduresPresence) > 0 and len(evaluatedProceduresPresence) == 0:
                res[idx][1] = 1

        return res

    def pipelineFnList(self, row):

        res = {
            "nome": row["no_cidadao"],
            "idade": row["nu_idade"],
            "Aferição de PA": [0, 0],
            "Glicemia": [0, 0],
            "Creatinina": [0, 0],
            "EAS/EQU (urina rotina)": [0, 0],
            "Sódio e potássio": [0, 0],
            "Colesterol total": [0, 0],
            "Hemograma": [0, 0],
            "Eletrocardiograma": [0, 0],
        }
        map_key = {
            "0": "Aferição de PA",
            "1": "Glicemia",
            "2": "Creatinina",
            "3": "EAS/EQU (urina rotina)",
            "4": "Sódio e potássio",
            "5": "Colesterol total",
            "6": "Hemograma",
            "7": "Eletrocardiograma",
        }
        try:
            for idx, i in enumerate(self.list):
                res = self.checkPresence(i.exams, row, res, map_key[str(idx)])

            self._res.append(res)
        except Exception as ex:
            traceback.print_exc(file=sys.stdout)

    def getResponselist(self):
        def _sort(x):
            if x['nome']:
                return str(x['nome'])
            else:
                return ''
        self._res = sorted(self._res, key=lambda x: _sort(x))
        return self._res


class DiabetesExamsList():
    def __init__(self):
        self._res = []
        self.list = [
            BloodGlucose(),
            GlycatedHemoglobin(),
            Retinography(),
            Creatinine(),
            Urine(),
            BloodCount(),
            BloodPressure(),
            TotalCholesterol()

        ]

    def pipelineFn(self, row):
        for i in self.list:
            i.checkPresence(row)

    def getResponse(self):
        result = []
        for i in self.list:
            result.append(i.toJson())

        return result

    def checkPresence(self, exams, row, res, idx):

        if len(exams) == 0:
            return res
        pattern = r'\W+'
        evaluatedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_avaliados']))
        requestedProcedures = set(
            re.split(pattern, row['ds_filtro_proced_solicitados']))

        evaluatedProceduresPresence = exams & evaluatedProcedures
        # print(evaluatedProceduresPresence)
        requestedProceduresPresence = exams & requestedProcedures
        """
    - se o código do exame não estiver nas colunas solicitado e avaliado, 
    soma 1 solicitação pendente para o exame;
    """
        if len(requestedProceduresPresence) == 0 and len(evaluatedProceduresPresence) == 0:
            res[idx][0] = 1
        else:
            """
            - se o código do exame  estiver nas coluna solicitado, mas não na coluna avaliado,
            conta pendente nos avaliados do exame; 
            """
            if len(requestedProceduresPresence) > 0 and len(evaluatedProceduresPresence) == 0:
                res[idx][1] = 1

        return res

    def pipelineFnList(self, row):

        res = {
            "nome": row["nome"],
            "idade": row["nu_idade"],
            "Glicemia": [0, 0],
            "Hemoglobina glicada":  [0, 0],
            "Retinografia":  [0, 0],
            "Creatinina":  [0, 0],
            "EAS/EQU (urina rotina)": [0, 0],
            "Hemograma":  [0, 0],
            "Aferição de PA":  [0, 0],
            "Colesterol total":  [0, 0],
        }
        map_key = {
            "0": "Glicemia",
            "1": "Hemoglobina glicada",
            "2": "Retinografia",
            "3": "Creatinina",
            "4": "EAS/EQU (urina rotina)",
            "5": "Hemograma",
            "6": "Aferição de PA",
            "7": "Colesterol total",
        }
        try:
            for idx, i in enumerate(self.list):
                res = self.checkPresence(i.exams, row, res, map_key[str(idx)])

            self._res.append(res)
        except Exception as ex:
            traceback.print_exc(file=sys.stdout)

    def getResponselist(self):
        self._res = sorted(self._res, key=lambda x: x['nome'])
        return self._res
