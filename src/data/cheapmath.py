import math

def calculate_size(x2,x1,y2,y1):
    distX = (x2-x1)**2
    distY = (y2-y1)**2
    dist = math.sqrt(distX+distY)
    return dist