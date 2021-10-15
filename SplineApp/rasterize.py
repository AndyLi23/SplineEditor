def plotLineLow(x0, y0, x1, y1):
    l = []
    
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    
    if(dy < 0):
        yi = -1
        dy = -dy
        
    D = (2*dy)-dx
    y = y0
    
    for x in range(x0, x1+1):
        l.append((x, y))
        if D > 0:
            y += yi
            D += 2*(dy-dx)
        else:
            D += 2*dy
            
    return l


def plotLineHigh(x0, y0, x1, y1):
    l = []
    
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    
    if(dx < 0):
        xi = -1
        dx = -dx
        
    D = (2*dx)-dy
    x = x0
    
    for y in range(y0, y1+1):
        l.append((x, y))
        if D > 0:
            x += xi
            D += 2*(dx-dy)
        else:
            D = D + 2*dx
            
    return l

def plotLine(x0, y0, x1, y1):
    l = []
    if abs(y1-y0) < abs(x1-x0):
        if x0>x1:
            l = plotLineLow(x1, y1, x0, y0)
        else:
            l = plotLineLow(x0, y0, x1, y1)
    else:
        if y0>y1:
            l = plotLineHigh(x1, y1, x0, y0)
        else:
            l = plotLineHigh(x0, y0, x1, y1)
    return l
        