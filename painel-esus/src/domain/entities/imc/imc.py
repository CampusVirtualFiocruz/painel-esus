from src.errors import InvalidIMC


class IMC:
    total = 0.0
    total_registros = 0
    min = 0.0
    max = 0.0
    label = ""
    imc = ""

    def __imc_calc(self, weigh, height) -> float:
        if height == 0:
            return 0
        height = round(height / 100, 2)
        return round(float(weigh / (height * height)), 2)

    def __check_imc(self, imc: float) -> bool:
        if not imc or imc <= 1 or imc >= 9999:
            raise InvalidIMC("Other IMC")
        if self.min <= imc <= self.max:
            return True
        return False

    def check_presence(self, weigh, height):
        imc = self.__imc_calc(weigh, height)
        # # Não levava em consideracao o numero total de pessoas
        check_imc = self.__check_imc(imc)
        if check_imc:
            self.total += 1

    def statistics_response(self, total_registros):
        try:
            total_presence = 100 * round(float(self.total / total_registros), 2)
        except ZeroDivisionError:
            total_presence = 0
        return [
            self.imc,
            {
                "com_consulta": total_presence,
                "com_consulta_abs": self.total,
                "limite": self.label,
                "sem_consulta": round(100 - total_presence, 2),
                "sem_consulta_abs": total_registros - self.total,
            },
        ]

    def __repr__(self) -> str:
        return f"{self.imc}({self.label}): {self.total}"
