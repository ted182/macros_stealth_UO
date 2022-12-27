from stealth import Mana, Dead, WarMode, SetWarMode, UseSkill
from datetime import datetime, timedelta

from pythonModules.aguardar import *

def medit(_val):
    
    while ( Mana() < _val ):
        
        if Dead():
            return False
        
        start = datetime.now()
        end = start + timedelta(seconds=10)
        
        print( '[medit] -> meditando...' )
        
        if WarMode():
            SetWarMode(False)
            aguardar(200)
        
        UseSkill('Meditation')
        aguardar(2000)

        if InJournalBetweenTimes('You are at peace.', start, end) > 0:
            break
    
    return True