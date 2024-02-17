# Version 0.1

#tictactoefeld = ["_"] * 9
#                 0   1   2   3   4   5   6   7 
tictactoefeld = ["x","_","_","_","x","_","_","_","x"]
# 0|1|2
# 3|4|5
# 6|7|8

assert len(tictactoefeld) == 9


def print_feld(feld):
    #for y in range(0,9,3):
    #    print(' '.join(feld[y : y + 3]))
    
    #print(feld[0:3])
    #print(feld[3:6])
    #print(feld[6:9])

    print(feld[0],feld[1],feld[2])
    print(feld[3],feld[4],feld[5])
    print(feld[6],feld[7],feld[8])


# Beispielfelder für gewonnenes Spiel 
beispiel_1_gewonnen_feld = ["x","_","_","_","x","_","_","_","x"]
beispiel_2_gewonnen_feld = ["x","x","x","_","_","_","_","_","_"]

# überprüft ob Spieler gewonnen hat
def check_ob_spieler_gewinnt(feld, spieler):
    z = False
    if feld[0] == feld[1] and feld[1] == feld[2] and feld[1] == spieler:
        z=True
    if feld[3] == feld[4] and feld[4] == feld[5] and feld[3] == spieler:
        z=True
    if feld[6] == feld[7] and feld[7] == feld[8] and feld[6] == spieler:
        z=True
    if feld[0] == feld[3] and feld[3] == feld[6] and feld[0] == spieler:
        z=True

    if z:
        print(f"Spieler {spieler} gewinnt!")
    return z



    
        
        
    
#print_feld(tictactoefeld)
print_feld(beispiel_1_gewonnen_feld)
print_feld(beispiel_2_gewonnen_feld)

print(check_ob_spieler_gewinnt(beispiel_2_gewonnen_feld, "x"))
print(check_ob_spieler_gewinnt(beispiel_1_gewonnen_feld, "x"))
