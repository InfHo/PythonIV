
def taschenrechner():
    rechenoperation = input("Bitte gib die rechenoperation an:")
    if rechenoperation == "+":
        ErsteZahl=int(input("Bitte gib die erste Zahl an, die addiert werden soll"))
        ZweiteZahl=int(input("Bitte gib die zweite Zahl an, die addiert werden soll"))
        print(ErsteZahl+ZweiteZahl)
    if rechenoperation == "/":
        try:
            ErsteZahl=int(input("Bitte gib die erste Zahl an, die dividiert werden soll"))
            ZweiteZahl=int(input("Bitte gib die zweite Zahl an, die dividiert werden soll"))
            print(ErsteZahl/ZweiteZahl)
        except ZeroDivisionError as e:
            print("Du sollst nicht durch Null teilen")
    if not rechenoperation =="+" or rechenoperation =="/":
        print("Diese Rechenoperation gibt es nicht, bitte gib ein gültiges Mathematisches Zeichen an.")
      
      
taschenrechner()
