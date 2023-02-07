

class BBtransaction:
    def __init__(self, id: int, torzs: str, cikkszam: str, trtype: str, quantity: float) -> None:
        self.id = id
        self.torzs = torzs
        self.cikkszam = cikkszam
        self.type = trtype
        self.quantity = quantity