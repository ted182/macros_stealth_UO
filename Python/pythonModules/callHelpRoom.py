from stealth import HelpRequest, GetGumpsCount, GetGumpInfo, NumGumpButton, GetX, GetY, Self
from datetime import datetime, timedelta

from pythonModules.aguardar import *
from pythonModules.mover import *


gumpHelp1 = 0x0000049B  #id do gump 'pedir help room'
gumpHelp2 = 0x0000049C  #id do gump 'sim!'
startCoordHelpRoom = [5451,1196]
startCoordComerceRoom = [2341,532] 
startCoordMinoc = [2466,544]  
endCoordMinoc = [2513, 548]  
gateCoordComerceRoom = [5448,1192]
gateCoordMinoc = [2330,536]



def clickGumpButton(gumpID , buttonID):
    for i in range( GetGumpsCount() ):  # go for each gump 
        g = GetGumpInfo(i)  # get gump
        if g['GumpID'] == gumpID:  # check if gump id is that what you need 
            NumGumpButton(i, buttonID)

def checkCoords(_x, _y):
    if GetX(Self()) == _x and GetY(Self()) == _y:
        return True
    return False

def checkHelpRoomStartPoint():
    global startCoordHelpRoom
    return checkCoords( startCoordHelpRoom[0], startCoordHelpRoom[1] )
    
def checkComerceRoomStartPoint():
    global startCoordComerceRoom
    return checkCoords( startCoordComerceRoom[0], startCoordComerceRoom[1] )

def checkMinocStartPoint():
    global startCoordMinoc
    return checkCoords( startCoordMinoc[0], startCoordMinoc[1] )

def callHelpRoom():   

    global gateCoordComerceRoom, gateCoordMinoc, endCoordMinoc

    timeout = datetime.now() + timedelta(seconds=180)    

    if not checkMinocStartPoint():
    
        if not checkComerceRoomStartPoint():
        
            if not checkHelpRoomStartPoint():
                aguardar(250)
                HelpRequest()
                aguardar(250)
                clickGumpButton(gumpHelp1,7)
                aguardar(250)
                clickGumpButton(gumpHelp2,8)

            while not checkHelpRoomStartPoint():
                print('[call-HP] - > aguardando help room...')                
                if (datetime.now() > timeout):
                    callHelpRoom()
                aguardar(10000)

            aguardar(250)
            mover( gateCoordComerceRoom[0], gateCoordComerceRoom[1], 0 )  

        aguardar(250)
        mover( gateCoordMinoc[0], gateCoordMinoc[1], 0 )

    aguardar(250)
    mover( endCoordMinoc[0], endCoordMinoc[1], 2 )