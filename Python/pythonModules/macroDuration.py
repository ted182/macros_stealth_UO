from datetime import datetime

def macroDuration(_startTime):
    delta = datetime.now() - _startTime
    print( 'tempo de macro decorrido: ' + str(delta) )    
    return True
