from stealth import FindTypeEx, FindQuantity, FindItem, MoveItem, Backpack, Dead
from pythonModules.aguardar import *
from pythonModules.openBank import *
from pythonModules.openContainer import *


def unloadToBank(_destBag, _listDict):

    if Dead():
        return False

    foundedItems = {}
    found = False
    openBank()
    openContainer(_destBag)
    
    for item in _listDict:
        
        for type in item['type']:
            
            while FindTypeEx(type, item['color'], Backpack(), False) > 0:                
                found = True
                qnt = FindQuantity()
                MoveItem(FindItem(), qnt, _destBag, 0, 0, 0)
                aguardar(250)

            if found:
                found = False
                item['amount'] += qnt    
            
            if item['amount'] > 0:
                foundedItems[ item['name'] ] = item['amount']

    print(foundedItems)
    return _listDict