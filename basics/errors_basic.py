
try:
    zahl1 = int(input("Gib  zahl1 ein:"))
    zahl2 = int(input("Gib  zahl2 ein:"))
    ergebnis = zahl1/zahl2
    print(ergebnis)

except ZeroDivisionError as e:
    print("Du sollst nicht durch 0 teilen!")

except ValueError as dings:
    print("Du sollst nicht durch buchstebaen teilen!", dings)

