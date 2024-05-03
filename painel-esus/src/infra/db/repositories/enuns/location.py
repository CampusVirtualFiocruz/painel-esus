class Location:
    constants = {
        'rural': 3,
        'urbano': 2,
        'nao_informado': 1,
    }

    @staticmethod
    def get_(entry: str):
        location = Location()
        entry = entry.strip().lower()
        if entry in location.constants:
            return location.constants[entry]
        return None
