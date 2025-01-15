from Shape.shape import Shape

class Triangle(Shape):
    """Subclase de Shape, una figura de 3 lados"""
    is_regular = False  #atributo de regularidad falso

    def __init__(self, vertices : list, edges : list):
        # se define cada una de las listas
        super().__init__()
        self._vertices = vertices
        self._edges = edges

    def compute_perimeter(self):
        # se recorre la lista de aristas para poder calcular su longitud y asi sumarla a una variable perimetro
        perimeter = 0
        for i in range(0, len(self._edges)):
            perimeter += self._edges[i].compute_lenght()
        return perimeter
    
    def compute_area(self):
        # se utiliza la formula de heron que se apoya en el semiperimetro y las longitudes de los lados para determinar el area de cualquier triangulo
        semiperimeter = self.compute_perimeter() / 2
        return (semiperimeter * (semiperimeter - self._edges[0].compute_lenght()) * (semiperimeter - self._edges[1].compute_lenght()) * (semiperimeter - self._edges[2].compute_lenght())) ** 0.5
    
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

class Isosceles(Triangle, Shape):
    """Clase que hereda todos los metodos de Triangle, siendo un triangulo de 2 lados iguales y 1 diferente en su definicion"""
    is_regular = False  #atributo de regularidad falso

    def __init__(self, vertices : list, edges : list):
        super().__init__(vertices, edges)

class Equilateral(Triangle, Shape):
    """Clase que hereda todos los metodos de Triangle, siendo un triangulo de 3 lados iguales en su definicion"""
    is_regular = True   #atributo de regularidad verdadero

    def __init__(self, vertices : list, edges : list):
        super().__init__(vertices, edges)

class Scalene(Triangle, Shape):
    """Clase que hereda todos los metodos de Triangle, siendo un triangulo de 3 lados diferentes en su definicion"""
    is_regular = False  #atributo de regularidad falso

    def __init__(self, vertices : list, edges : list):
        super().__init__(vertices, edges)

class TriRectangle(Triangle, Shape):
    """Clase que hereda todos los metodos de Triangle, siendo un triangulo en que uno de sus angulos internos es de 90 grados"""
    is_regular = False  #atributo de regularidad falso

    def __init__(self, vertices : list, edges : list):
        super().__init__(vertices, edges)