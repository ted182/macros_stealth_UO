from stealth import FindType, FindQuantity, FindFullQuantity, GetQuantity, MoveItem, Backpack, Dead
from pythonModules.aguardar import *
from pythonModules.openBank import *
from pythonModules.openContainer import *


def restockMacroReags(_bagBankReags, _reagsDict):
    
    if Dead():
        return False
    
    openBank()
    openContainer(_bagBankReags)

    for item in _reagsDict:
        
        aguardar(100)

        if FindType(item['type'], _bagBankReags) > 0:
            
            item['bankAmount'] = FindFullQuantity()
            print( item['name'] + ' disponíveis: ' + str(FindFullQuantity()) )

            while GetQuantity( FindType(item['type'], Backpack()) ) < item['bagAmount']:
                qnt = item['bagAmount'] - FindQuantity()
                MoveItem( FindType(item['type'], _bagBankReags) , qnt, Backpack(), 0, 0, 0)
                aguardar(250)    

        else:
            print( item['name'] + ' acabou na bag de restock do banco...' )
            exit()
