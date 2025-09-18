from typing import Literal


class InstalationStatus:
    _instance = None

    total = 0
    progress = 0
    status: Literal["Cancelado", "Não iniciado", "Instalando", "Instalado"] = "Não iniciado"

    base_generator_len = 0
    base_generator = 0
    indicators = 0
    indicators_len = 0
    logs = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.reset()
        return cls._instance

    def set_indicators_len(self, total):
        self.indicators_len = total

    def set_base_generator_len(self, total):
        self.base_generator_len = total

    def set_total(self, total):
        self.total = total

    def update_base_progress(self):
        self.base_generator+=1
        self._update_progress()

    def update_indicators_progress(self):
        self.indicators += 1
        self._update_progress()

    def _update_progress(self):
        num = self.base_generator + self.indicators
        if num > 0 and self.total > 0: 
            self.progress = round(
                (
                    num
                )/self.total,
                2
            )
        else:
            self.progress = 0

    def _calc_base_progress(self):
        if self.base_generator > 0 and self.total > 0:
            return round((
                self.base_generator/self.base_generator_len
            ),2)
        else:
            return 0

    def _calc_indicators_progress(self):
        if self.indicators > 0 and self.total > 0:
            return round((
                self.indicators/self.indicators_len
            ),
            2)
        else:
            return 0

    def cancel(self):
        self.status = "Cancelado"

    def next(self):
        if self.status == "Cancelado":
            self.status = "Instalando"
        elif self.status == 'Não iniciado':
            self.status = "Instalando"
        elif self.status == "Instalando":
            self.status = "Instalado"
        elif self.status == "Instalado":
            self.status = "Instalado"

    def reset(self):
        self.total = 0
        self.progress = 0
        self.status = "Não iniciado"
        self.base_generator = 0
        self.indicators = 0
        self.logs = []

    def add_log(self, log, time):
        self.logs.append(
            {"tabela": log, "tempo": str(time)}
        )

    def to_dict(self):
        return {
            "progresso_instalacao": {
                "status": self.status,
                "percentual": self.progress,
            },
            "jobs": [
                {"nome": "Gerando Base", "percentual": self._calc_base_progress() },
                {"nome": "Calculando indicadores", "percentual": self._calc_indicators_progress()},
            ],
            "logs": self.logs
        }


def test_singleton():
    s1 = InstalationStatus()
    s1.total = 10
    assert s1.total == 10

    s2 = InstalationStatus()
    assert s2.total == 10

    s2.reset()
    assert s1.total == 0
    assert s2.total == 0

def test_progress():
    s2 = InstalationStatus()
    s2.set_total(10)
    s2.update_base_progress()

    assert s2.progress == 0.1

    s2.update_base_progress()

    assert s2.progress == 0.2

    s2.update_base_progress()
    s2.update_indicators_progress()
    s2.update_indicators_progress()

    assert s2.progress == 0.5
    assert s2.base_generator == 3
    assert s2.indicators == 2

def test_next():
    s = InstalationStatus()
    assert s.status == 'Não iniciado'
    s.next()
    assert s.status == "Instalando"
    s.next()
    assert s.status == "Instalado"
    s.next()
    assert s.status == "Instalado"

def test_dict():
    s = InstalationStatus()
    s.set_total(10)
    s.update_base_progress()

    dict = s.to_dict()
    assert dict["progresso_instalacao"]["status"] == "Não iniciado"
    assert dict["progresso_instalacao"]["percentual"] == 0.1

    s.next()
    dict = s.to_dict()

    print(dict["jobs"])
    assert dict["progresso_instalacao"]["status"] == "Instalando"
    assert dict["jobs"][0]["percentual"] == 0.1
    assert dict["jobs"][1]["percentual"] == 0.0

    s.update_indicators_progress()
    dict = s.to_dict()
    assert dict["jobs"][0]["percentual"] == 0.1
    assert dict["jobs"][1]["percentual"] == 0.1
    assert dict["progresso_instalacao"]["percentual"] == 0.2

    s.add_log('tb_fat_ok', '00:30:00')
    print(s.to_dict())
