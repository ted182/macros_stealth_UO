from stealth import UOSay, WaitJournalLine, Dead
from datetime import datetime
from pythonModules.aguardar import *

def openBank():
    
    start = datetime.now()

    aguardar(250)

    if Dead():
        return False
    
    UOSay('banker bank')
    UOSay('banco')

    if ( not WaitJournalLine(start, 'stones in your Bank Box', 2000) ):
        openBank()

    return True

