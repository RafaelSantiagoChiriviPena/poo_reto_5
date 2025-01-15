# poo_reto_5
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto
1. Create a package with all code of class Shape, this exersice should be conducted in two ways:
- A unique module inside of package Shape
El paquete sigue la siguiente estructura
```bash
├───reto_5_punto_1
│   │   main.py
│   │
│   └───Shape
│       │   shape.py
│       │   __init__.py
│       │
│       └───__pycache__
│               shape.cpython-312.pyc
│               __init__.cpython-312.pyc
```
- Individual modules that import Shape in inheritates from it.
El paquete sigue la siguiente estructura
```bash
└───reto_5_punto_2
    │   main.py
    │
    └───Shape
        │   line.py
        │   point.py
        │   rectangle.py
        │   shape.py
        │   triangle.py
        │   __init__.py
        │
        └───__pycache__
                line.cpython-312.pyc
                point.cpython-312.pyc
                rectangle.cpython-312.pyc
                shape.cpython-312.pyc
                triangle.cpython-312.pyc
                __init__.cpython-312.pyc
```
el resultado obtenido por ambos main es el siguiente:
```
[(0, 0), (3, 2), (0, 2), (3, 0)]
['(0,0) - (0,2)', '(0,2) - (3,2)', '(3,2) - (3,0)', '(0,0) - (3,0)']
(90, 90, 90, 90)
El perimetro del rectangulo es de 10 unidades
El area del rectangulo es de 6 unidades cuadradas

[(0, 0), (3, 3), (0, 3), (3, 0)]
['(0,0) - (0,3)', '(0,3) - (3,3)', '(3,3) - (3,0)', '(0,0) - (3,0)']
[90, 90, 90, 90]
El perimetro del cuadrado es de 12 unidades
El area del cuadrado es de 9 unidades cuadradas

[(0, 0), (4, 0), (2, 4.58257569495584)]
['(0,0) - (4,0)', '(4,0) - (2,4.58257569495584)', '(2,4.58257569495584) - (0,0)']
El perimetro del triangulo es de 14.0 unidades
El area del triangulo es de 9.16515138991168 unidades cuadradas

[(0, 0), (4, 0), (2, 3.4641016151377544)]
['(0,0) - (4,0)', '(4,0) - (2,3.4641016151377544)', '(2,3.4641016151377544) - (0,0)']
El perimetro del triangulo es de 12.0 unidades
El area del triangulo es de 6.928203230275509 unidades cuadradas

[(0, 0), (3, 0), (1, 4.0)]
['(0,0) - (3,0)', '(3,0) - (1,4.0)', '(1,4.0) - (0,0)']
El perimetro del triangulo es de 11.595241580617241 unidades
El area del triangulo es de 6.000000000000003 unidades cuadradas

[(0, 0), (3, 0), (3, 4)]
['(0,0) - (3,0)', '(3,0) - (3,4)', '(3,4) - (0,0)']
El perimetro del triangulo es de 12.0 unidades
El area del triangulo es de 6.0 unidades cuadradas
```
