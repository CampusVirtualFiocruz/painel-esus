class InfantilAdapter:

    def total_count_infantil(self, response):
        total = response[0][0] if response else 0
        return {"data": total}
