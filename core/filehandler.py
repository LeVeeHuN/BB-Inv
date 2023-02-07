

class Filehandler:
    def __init__(self) -> None:
        self.savename = None
        self.data = None

    def setTarget(self, savename: str):
        self.savename = savename

    def readData(self) -> tuple:
        with open(self.savename, 'r') as f:
            data = f.read()
        
        data = data.split("||")

        ### Items
        tmp = data[0].split("\n")
        tmp.pop()

        items = []
        for item in tmp:
            items.append(item.split("|"))

        ### Transactions
        tmp = data[1].split("\n")
        tmp.pop(0)

        transactions = []
        for tr in tmp:
            transactions.append(tr.split("|"))

        ### Final
        data = (items, transactions)
        return data

    def save(self, data):
        pass

    def autosave(self, data):
        pass


###########################
fh = Filehandler()
fh.setTarget("./saves/tesztsave.levdb")
x = fh.readData()