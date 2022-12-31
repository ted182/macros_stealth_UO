from stealth import FindType, FindQuantity, FindFullQuantity, GetQuantity, MoveItem, Backpack, Dead
from datetime import datetime, timedelta

from pythonModules.aguardar import *
from pythonModules.openBank import *
from pythonModules.openContainer import *


def reagBagAmount(_type):
    return GetQuantity( FindType(_type, Backpack()) )

def checkBankResources(_bagBankReags, _reagsDict):

    checkTimes = 3  #roda a rotina x vezes para garantir que não deu erro
    attempts = 0
    err = 0

    while attempts <= checkTimes - 1 :

        openBank()
        openContainer(_bagBankReags)

        for item in _reagsDict:
            aguardar(100)
            if FindType(item['type'], _bagBankReags) > 0:                    
                item['bankAmount'] = FindFullQuantity()
            else:
                #print('erro-01')
                err += 1
        
        attempts += 1

    if err >= checkTimes:
        return False
    
    return True

def printBankResources(_reagsDict):
    for item in _reagsDict:
        print( item['name'] + ' disponíveis: ' + str( item['bankAmount'] ) )


def restockMacroReags(_bagBankReags, _reagsDict):   

    if Dead():
        return False
    
    if not checkBankResources(_bagBankReags, _reagsDict):
        print( '[restock-reags] -> sem reags na bag de restock do banco...' )
        exit()
    
    timeout = datetime.now() + timedelta(seconds=300)
    
    for item in _reagsDict:
            
        aguardar(250)

        while reagBagAmount(item['type']) < item['bagAmount']:
            if (datetime.now() > timeout):
                break
            openBank()
            openContainer(_bagBankReags)
            qnt = item['bagAmount'] - FindQuantity()
            MoveItem( FindType(item['type'], _bagBankReags) , qnt, Backpack(), 0, 0, 0)
            aguardar(250) 
    
    printBankResources(_reagsDict)
