from stealth import GetX, GetY, Dead, Self, Mana, GetMaxMana, GetQuantity, FindType, Backpack, UOSay

from pythonModules.aguardar import *
from pythonModules.medit import *
from pythonModules.callHelpRoom import callHelpRoom

def checkRecallReags():
    recallReagsTypes = [0x0F7A, 0x0F7B, 0x0F86]
    for reagType in recallReagsTypes:
        aguardar(100)
        if GetQuantity( FindType(reagType, Backpack()) ) == 0:
            print('[check-reags] -> sem reags de recall na bag...')
            return True


def recall(_list):    

    xDest = _list[0]
    yDest = _list[1]
    runePag = _list[2]
    runeNum = _list[3]
    dest = _list[4]
    
    if ( xDest == GetX(Self()) and yDest == GetY(Self()) ):
        print('[recall] -> o char ja está no local da runa...')
        return True

    while ( xDest != GetX(Self()) and yDest != GetY(Self()) ):
       
        aguardar(100)

        if Dead():
            return False

        if checkRecallReags():
            callHelpRoom()
            return False

        if Mana() < 20:
            medit( GetMaxMana(Self()) )

        print('[recall] -> recalando ' + dest + ' ...')
        UOSay( '.recall ' + str(runePag) + ',' + str(runeNum) )

        aguardar(10000)

    return True




