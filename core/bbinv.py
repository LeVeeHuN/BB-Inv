# This is the main class of the application
# It handles everything

import os
import core.filehandler
import core.bbitem
import core.bbtransaction
import core.constants as c

class BBinv:
    def __init__(self) -> None:
        self.items = list()
        self.transactions = list()

        print("BB-Inv DEV 0.0.1")

        saves = os.listdir("./saves")
        print("0 - Uj raktar")
        for i, save in enumerate(saves):
            print(f"{i+1} - {save}")
        userCh = int(input("Valasz: ")) - 1
        if userCh == -1:
            self.new()
        else:
            fh = core.filehandler.Filehandler()
            fh.setTarget(f"./saves/{saves[userCh-1]}")
            savedata = fh.readData()
            self.initfromdata(savedata)


    def new(self):
        pass

    def initfromdata(self, savedata: tuple):
        items = savedata[0]
        transactions = savedata[1]

        for item in items:
            i = core.bbitem.BBitem(item[0], item[1], item[2], item[4])
            i.add(float(item[3]))
            self.items.append(i)

        for tr in transactions:
            self.transactions.append(core.bbtransaction.BBtransaction(tr[0], tr[1], tr[2], tr[3], tr[4]))


    def printdata(self) -> None:
        print("Elemek:")
        for item in self.items:
            print(item.name + " " + str(item.quantity) + " " + item.mertek)

    def datainit(self, data):
        pass

    def deleteItem(self, torzs: str, cikkszam: str) -> None:
        for i, item in enumerate(self.items):
            if item.torzs == torzs and item.cikkszam == cikkszam:
                self.items.pop(i)
                c.cls()
                input(f"A {torzs} cikktorzsben talalhato {cikkszam} cikkszamu cikk torlve lett a raktarbol.\nNyomj ENTER-t a folytatashoz!")
                return None

    def modifyItem(self, torzs: str, cikkszam: str):
        for item in self.items:
            if item.torzs == torzs and item.cikkszam == cikkszam:
                c.cls()
                print('0 - Vissza\n1 - Hozzaadas\n2 - Elvetel')
                try:
                    userCh = int(input("Valasz: "))
                except:
                    c.cls()
                    input("Nincs ilyen opcio...\nNyomj ENTER-t a folytatashoz!")
                    return None
                if userCh == 0:
                    return None
                elif userCh == 1:
                    quantity = int(input("Hozzaadando mennyiseg: "))
                    item.add(quantity)
                    return None
                elif userCh == 2:
                    quantity = int(input("Eltavolitando mennyiseg: "))
                    item.remove(quantity)
                    return None

    def mainloop(self) -> None:
        while True:
            c.cls()
            print("0 - Kilepes")
            print("Adja meg a cikk osszetett kodjat: ")

            userCh = str(input("Valasz: "))
            if userCh == '0':
                break
            else:
                for item in self.items:
                    if item.torzs + item.cikkszam == userCh:
                        c.cls()
                        print(f"{item.name}\n{item.torzs} {item.cikkszam}\n{item.quantity} {item.mertek}")
                        try:
                            userCh = int(input("0 - Vissza\n1 - Modositas\n2 - Torles"))
                        except:
                            c.cls()
                            input("Nincs ilyen opcio...\nNyomj ENTER-t a folytatashoz!")
                            break

                        if userCh == 0:
                            break
                        elif userCh == 1:
                            # Cikk modositasa
                            self.modifyItem(item.torzs, item.cikkszam)
                            break
                        elif userCh == 2:
                            # Cikk torlese
                            self.deleteItem(item.torzs, item.cikkszam)
                            break
                        else:
                            input("Nincs ilyen opcio...\nNyomj ENTER-t a folytatashotz!")
                            break
        print('EXITING APPLICATION...')
        return None
