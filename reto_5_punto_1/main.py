from Shape.shape import *
if __name__ == "__main__":
    # definicion para cada tipo de figura, y aplicando sus metodos con la estructura: vertices, aristas, angulos, perimetro y area
    rectangle_test = Rectangle(
        vertices = (
            Point(0,0),
            Point(3,2),
            Point(0,2),
            Point(3,0)
        ),
        edges= (
            Line(
                start = Point(0,0),
                end = Point(0,2)
            ),
            Line(
                start = Point(0,2),
                end = Point(3,2)
            ),
            Line(
                start = Point(3,2),
                end = Point(3,0)
            ),
            Line(
                start = Point(0,0),
                end = Point(3,0)
            )
        ),
        inner_angles=(90, 90, 90, 90)
    )

    print(rectangle_test.get_vertices())
    print(rectangle_test.get_edges())
    print(rectangle_test.get_inner_angles())
    print(f"El perimetro del rectangulo es de {rectangle_test.compute_perimeter()} unidades")
    print(f"El area del rectangulo es de {rectangle_test.compute_area()} unidades cuadradas \n")

    square_test = Square(
        vertices= (
            Point(0,0),
            Point(3,3),
            Point(0,3),
            Point(3,0)
        ),
        edges= (
            Line(
                start = Point(0,0),
                end = Point(0,3)
            ),
            Line(
                start = Point(0,3),
                end = Point(3,3)
            ),
            Line(
                start = Point(3,3),
                end = Point(3,0)
            ),
            Line(
                start = Point(0,0),
                end = Point(3,0)
            )
        ),
        inner_angles= [90, 90, 90, 90]
    )

    print(square_test.get_vertices())
    print(square_test.get_edges())
    print(square_test.get_inner_angles())
    print(f"El perimetro del cuadrado es de {square_test.compute_perimeter()} unidades")
    print(f"El area del cuadrado es de {square_test.compute_area()} unidades cuadradas \n")

    IsosTriangle_test = Isosceles(
        vertices = (
            Point(0,0),
            Point(4,0),
            Point(2,21 ** 0.5)
        ),
        edges = (
            Line(
                start = Point(0,0),
                end = Point(4,0),
            ),
            Line(
                start = Point(4,0),
                end = Point(2, 21 ** 0.5)
            ),
            Line(
                start = Point(2, 21 ** 0.5),
                end = Point(0,0)
            )
        )
    )

    print(IsosTriangle_test.get_vertices())
    print(IsosTriangle_test.get_edges())
    print(f"El perimetro del triangulo es de {IsosTriangle_test.compute_perimeter()} unidades")
    print(f"El area del triangulo es de {IsosTriangle_test.compute_area()} unidades cuadradas \n")

    EquiTriangle_test = Equilateral(
        vertices = (
            Point(0,0),
            Point(4,0),
            Point(2,12 ** 0.5)
        ),
        edges = (
            Line(
                start = Point(0,0),
                end = Point(4,0),
            ),
            Line(
                start = Point(4,0),
                end = Point(2, 12 ** 0.5)
            ),
            Line(
                start = Point(2, 12 ** 0.5),
                end = Point(0,0)
            )
        )
    )

    print(EquiTriangle_test.get_vertices())
    print(EquiTriangle_test.get_edges())
    print(f"El perimetro del triangulo es de {EquiTriangle_test.compute_perimeter()} unidades")
    print(f"El area del triangulo es de {EquiTriangle_test.compute_area()} unidades cuadradas \n")

    ScalTriangle_test = Scalene(
        vertices = (
            Point(0,0),
            Point(3,0),
            Point(1,16 ** 0.5)
        ),
        edges = (
            Line(
                start = Point(0,0),
                end = Point(3,0),
            ),
            Line(
                start = Point(3,0),
                end = Point(1, 16 ** 0.5)
            ),
            Line(
                start = Point(1, 16 ** 0.5),
                end = Point(0,0)
            )
        )
    )

    print(ScalTriangle_test.get_vertices())
    print(ScalTriangle_test.get_edges())
    print(f"El perimetro del triangulo es de {ScalTriangle_test.compute_perimeter()} unidades")
    print(f"El area del triangulo es de {ScalTriangle_test.compute_area()} unidades cuadradas \n")

    TriRect_test = TriRectangle(
        vertices = (
            Point(0,0),
            Point(3,0),
            Point(3,4)
        ),
        edges = (
            Line(
                start = Point(0,0),
                end = Point(3,0),
            ),
            Line(
                start = Point(3,0),
                end = Point(3,4)
            ),
            Line(
                start = Point(3,4),
                end = Point(0,0)
            )
        )
    )

    print(TriRect_test.get_vertices())
    print(TriRect_test.get_edges())
    print(f"El perimetro del triangulo es de {TriRect_test.compute_perimeter()} unidades")
    print(f"El area del triangulo es de {TriRect_test.compute_area()} unidades cuadradas \n")