import time
from pythonModules.aguardar import *
from stealth import Dead, SetEventProc, SetGlobal, GetGlobal, UseObject


def openContainer(_serial):
    
    def waitOpenContainer(_serial, _modelGump):    
        SetGlobal('char', 'Container', 'Open')
    
    def emptyEventFunction(_serial, _modelGump):
        aguardar(100)

    if Dead():
        return False    
    
    startTime = time.time()
    waitTime = 1

    SetGlobal('char', 'Container', 'Closed')
    SetEventProc('evDrawContainer', waitOpenContainer)
    aguardar(100)        
    UseObject(_serial)  

    while ( (GetGlobal('char', 'Container') == 'Closed') and (time.time() < startTime + waitTime) ):
        aguardar(100)

    SetEventProc('evDrawContainer', emptyEventFunction) #limpar o evento de abrir container
    return True