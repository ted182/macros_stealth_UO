from stealth import NewMoveXY

def mover(_x, _y, _acc=1, _run=False):
    """
    function NewMoveXY(
        Xdst, Ydst : Word; 
        Optimized : Boolean; 
        Accuracy : Integer; 
        Running : Boolean
    ) : Boolean
    """
    opt = True
    #acc = 1
    #run = False    
    
    return NewMoveXY(_x, _y, opt, _acc, _run)