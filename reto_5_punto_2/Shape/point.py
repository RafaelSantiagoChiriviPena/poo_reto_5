class Point:
    """Se define un punto del espacio"""

    def __init__(self,x,y):
        # se establecen coordenadas x,y para el punto
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point")-> float:
        # determina la diferencia entre cada eje de coordenadas entre los puntos, y obteniendo su distancia por medio de pitagoras
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance
