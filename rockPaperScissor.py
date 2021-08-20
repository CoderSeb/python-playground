# Gör ett spel där du spelar sten, sax, påse mot datorn.
# I programmering är det viktigt att kunna söka information på nätet så gör ett försök!
# Dela upp problemet i mindre delar.
# Förslagsvis, börja med att skapa en input där användaren skriver in en siffra eller text för att välja sten, sax eller påse.

# Ett paket som förenklar utvecklingen är random. Som hjälp är det paketet redan importerat. Läs dock på om hur det används.
import random

userAction = int(input("Välj ett alternativ: (1)-Sten, (2)-Sax eller (3)-Påse: "))
possibleActions = [1, 2, 3]
computerAction = random.choice(possibleActions)


def convertAction(action):
    if action == 1:
        action = "Sten"
    elif action == 2:
        action = "Sax"
    else:
        action = "Påse"
    return action


print(f"\nDu valde {convertAction(userAction)}, datorn valde {convertAction(computerAction)}.\n")


def checkWinner(usrAct, cprAct):
    if usrAct == cprAct:
        print("Det blev lika!")
    elif usrAct == 1:
        if cprAct == 2:
            print("Grattis! Du vann!")
        else:
            print("Påse slår sten, du förlorade...")
    elif usrAct == 2:
        if cprAct == 3:
            print("Grattis! Du vann!")
        else:
            print("Tyvärr... Sten slår sax!")
    elif usrAct == 3:
        if cprAct == 1:
            print("Grattis! Du vann!")
        else:
            print("Aj aj! Sax klipper sönder påsen!")


checkWinner(userAction, computerAction)
