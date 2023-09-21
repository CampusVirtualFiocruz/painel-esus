class IndividualCare:
    constants = {
        'rural': 3,
        'urbano': 2,
        'masculino': 1,
        'feminino': 2
    }

    @staticmethod
    def get_(entry: str):
        individual_care = IndividualCare()
        entry = entry.strip().lower()
        if entry in individual_care.constants:
            return individual_care.constants[entry]
        return None
