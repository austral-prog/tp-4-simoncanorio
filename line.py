import math 
def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print(f"""El coeficiente A de su ecuación de la recta es: {A}
El coeficiente B de su ecuación de la recta es: {B}
El coeficiente X1 de su ecuación de la recta es: {X1}
El coeficiente X2 de su ecuación de la recta es: {X2}""")

    Y1 = A * X1 + B
    Y2 = A * X2 + B
    print(f"""
Para la siguiente ecuación:
\tY = {A}X + {B}""")
    print(f"""
Dados los siguientes puntos:
\tP1 ({X1}, {Y1})
\tP2 ({X2}, {Y2})""")
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    print(f"""
La distancia entre ellos es: {distancia}""")
