from Shape.shape import Shape

class Rectangle(Shape):
    """Reinvencion de la clase Rectangle, añadiendo vertices, aristas y angulos internos a su definicion"""
    is_regular = False  # atributo de regularidad falso

    def __init__(self, vertices : list, edges : list, inner_angles : list):
        # se define cada una de las listas
        super().__init__()
        self._vertices = vertices
        self._edges = edges #orden: height1, width1, height2, width2
        self._inner_angles = inner_angles

    def compute_area(self):
        # toma coordenadas de los puntos de las lineas para determinar altura y anchura del rectangulo para asi calcular el area
        return ((self._edges[0].end.y-self._edges[0].start.y) * (self._edges[3].end.x - self._edges[3].start.x))
        
    def compute_perimeter(self):
        # toma coordenadas de los puntos de las lineas para determinar altura y anchura del rectangulo para asi calcular el perimetro
        return 2 * ((self._edges[0].end.y-self._edges[0].start.y) + (self._edges[3].end.x - self._edges[3].start.x))
    
    def get_vertices(self):
        # obtiene los compnentes x y y de cada punto definido para el objeto, ubicandolo en tuplas que seran puestas en una lista que es el retorno de la funcion
        vertices_get = []
        for i in range(0, len(self._vertices)):
            point_get = (self._vertices[i].x , self._vertices[i].y)
            vertices_get.append(point_get)
        return vertices_get
    
    def get_edges(self):
        # obtiene los puntos de inicio y final de cada linea, escribiendola como una cadena de la forma "(x1,y1) - (x2,y2)" para luego poner cada cadena en una lista que es el retorno de la funcion
        edges_get = []
        for i in range(0, len(self._edges)):
            line_get = f"({self._edges[i].start.x},{self._edges[i].start.y}) - ({self._edges[i].end.x},{self._edges[i].end.y})"
            edges_get.append(line_get)
        return edges_get
        
    def get_inner_angles(self):
        # retorna la lista definida de angulos internos
        return self._inner_angles
    
class Square(Rectangle, Shape):
    """Clase que hereda todos los metodos de rectangle, con una unica diferencia en su definicion, las lineas deben tener la misma longitud"""
    is_regular = True   #atributo de regularidad verdadero

    def __init__(self, vertices : list, edges : list, inner_angles : list):
        super().__init__(vertices, edges, inner_angles)