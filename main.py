# This is the entry point of the BB-Inv software.
# The BB-Inv software is an inventory and a warehouse management system
# The BB-Inv was created by Levente Bajnoczi, who is the CEO of BB Co.
# This project was inspired by the project kh-raktar
import core.bbinv



def startup() -> None:
    global inv
    inv = core.bbinv.BBinv()

startup()
inv.mainloop()