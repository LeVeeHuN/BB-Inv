# This class implements the bbitem type that is used in the BB-Inv system.

class BBitem:
    def __init__(self, name: str, torzs: str, cikkszam: str, mertek: str) -> None:
        self.name = name
        self.torzs = torzs
        self.cikkszam = cikkszam
        self.mertek = mertek
        self.quantity = float(0)

    def add(self, quantity):
        self.quantity += quantity

    def remove(self, quantity):
        if self.quantity < quantity:
            print("Nem all rendelkezesre elegendo anyag.")
            input("Nyomj entert a folytatashoz")
        else:
            self.quantity -= quantity

    def unsafeRemove(self, quantity):
        self.quantity -= quantity
