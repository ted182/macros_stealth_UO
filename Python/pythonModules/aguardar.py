from stealth import Wait, Connected, CheckLag, InJournalBetweenTimes
from datetime import datetime, timedelta

def aguardar(_tempoMs: int):
    
    start = datetime.now()
    end = start + timedelta(seconds=-10)
    
    Wait(_tempoMs)    

    while ( not Connected() or not CheckLag(timeoutMS=1000) ):
        print('[aguardar] -> esperando 10 segundos para retomar...')
        Wait(10000)

    if InJournalBetweenTimes('World save in 10 seconds', start, end) > 0:
        print( '[worldSave] -> aguardando...' )
        Wait(25000)
        print( '[worldSave] -> liberado!' )
    
    