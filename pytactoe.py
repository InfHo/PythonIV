# Version 0.3
import random as rd

#tictactoefeld = ["_"] * 9
#                 0   1   2   3   4   5   6   7 
# tictactoefeld = ["x","_","_","_","x","_","_","_","x"]
tictactoefeld = ["_","_","_","_","_","_","_","_","_"]
# 0|1|2
# 3|4|5
# 6|7|8 

# nimm an, dass das ttt-Feld 9 Felder hat.
assert len(tictactoefeld) == 9


def print_feld(feld):
    #for y in range(0,9,3):
    #    print(' '.join(feld[y : y + 3]))

    print(feld[0],feld[1],feld[2])
    print(feld[3],feld[4],feld[5])
    print(feld[6],feld[7],feld[8])


# Beispielfelder für gewonnenes Spiel 
#                            0   1   2   3   4   5   6   7   8
beispiel_1_gewonnen_feld = ["x","_","_","_","x","_","_","_","x"]
beispiel_2_gewonnen_feld = ["x","x","x","_","_","_","_","_","_"]






# überprüft ob Spieler gewonnen hat
def check_ob_spieler_gewinnt(feld, spieler):
    z = False
    # Prüfe Zeile No° 1
    if feld[0] == feld[1] and feld[1] == feld[2] and feld[1] == spieler:
        z=True
    # Prüfe Zeile No° 2
    if feld[3] == feld[4] and feld[4] == feld[5] and feld[3] == spieler:
        z=True
    # Prüfe Zeile No° 3
    if feld[6] == feld[7] and feld[7] == feld[8] and feld[6] == spieler:
        z=True
    # Prüfe Spalte No° 1
    if feld[0] == feld[3] and feld[3] == feld[6] and feld[0] == spieler:
        z=True
    # Prüfe Spalte No° 2
    if feld[1] == feld[4] and feld[4] == feld[7] and feld[1] == spieler:
        z=True  
    # Prüfe Spalte No° 3
    if feld[2] == feld[5] and feld[5] == feld[8] and feld[2] == spieler:
        z=True
    # Prüfe Diagonale von links-oben -> rechts-unten
    if feld[0] == feld[4] and feld[4] == feld[8] and feld[0] == spieler:
        z=True
    # Prüfe Diagonale von links-unten -> rechts-oben
    if feld[2] == feld[4] and feld[4] == feld[6] and feld[2] == spieler:
        z=True
  
    if z:
        print(f"Spieler {spieler} gewinnt!")
        return True
    return z


def Zug(Spieler,Spielfeld):
    ZugErfolgreich=0
    while ZugErfolgreich==0:
        try:
            Feld=int(input("Welches Feld möchtest du belegen: "))
            ZugErfolgreich=1
        except:
            print("Es muss eine Zahl sein")
    if Spielfeld[Feld-1]=="_":
        Spielfeld[Feld-1]=Spieler

def Zug_KI(Spieler,feld):
    while "_" in feld:
        zufallszahl=rd.randint(0,8)
        if feld[zufallszahl] == "_":
            feld[zufallszahl] = Spieler
            break
    print("AI hat gezogen!")




# Wohin soll unser Dings?
# -> 9 Dingse oder jemand gewinnt
# --> for-Schleife!
# --> Feld ausgeben!
# --> irgendwas mit input (wer, wohin?)
# --> tictactoefeld anpassen
# --> hat wer gewonnen?


        
        
    
# #print_feld(tictactoefeld)
# print_feld(beispiel_1_gewonnen_feld)
# print_feld(beispiel_2_gewonnen_feld)

# print(check_ob_spieler_gewinnt(beispiel_2_gewonnen_feld, "x"))
# print(check_ob_spieler_gewinnt(beispiel_1_gewonnen_feld, "x"))

# print_feld(tictactoefeld)

# funktionX()
# print_feld(tictactoefeld)
    
#=================Hauptschleife================================================
print("\nFeldnummern:")
print("1|2|3")
print("4|5|6")
print("7|8|9")
print("")

while True:
    #Zug von x
    if not "_" in tictactoefeld:
        break
    Zug("x",tictactoefeld)
    print("________________")
    print_feld(tictactoefeld)
    if check_ob_spieler_gewinnt(tictactoefeld,"x"):
        break
    if not "_" in tictactoefeld:
        break
    
    # Zug("o",tictactoefeld) # <- 
    Zug_KI("o",tictactoefeld) # <- AI zieht
    print("________________")
    print_feld(tictactoefeld)
    if check_ob_spieler_gewinnt(tictactoefeld,"o"):
        break
    if not "_" in tictactoefeld:
        break
        
    


