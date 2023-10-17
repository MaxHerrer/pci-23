"""Se importa la biblioteca math al programa"""
import math

"""Calcula el perimetro del triangulo con sus tres lados"""
def perimetro_triangulo():
    lado_a = float(input("Dame el valor del lado_a: "))
    lado_b = float(input("Dame el valor del lado_b: "))
    lado_c = float(input("Dame el valor del lado_c: "))
    return lado_a + lado_b + lado_c

"""Calcula el perimetro del cuadrado con uno de sus lados"""
def perimetro_cuadrado():
    lado = float(input("Dame el valor del lado: "))
    return lado * 4

"""Calcula el perimetro del rectangulo con dos de sus lados"""
def perimetro_rectangulo():
    lado_a = float(input("Dame el valor del lado_a: "))
    lado_b = float(input("Dame el valor del lado_b: "))
    return (lado_a * 2) + (lado_b * 2)

"""Calcula el perimetro del circulo con su radio y pi"""
"""Aqui se utiliza la biblioteca math"""
"""https://docs.python.org/es/3/library/math.html"""
def perimetro_circulo():
    radio = float(input("Dame el valor del radio: "))
    PI = math.pi
    return 2 * PI * radio

"""Calcula el perimetro del rombo con uno lados"""
def perimetro_rombo():
    lado = float(input("Dame el valor del lado: "))
    return lado * 4

"""Calcula el perimetro del pentagono con uno de sus lados"""
def perimetro_pentagono():
    lado = float(input("Dame el valor del lado: "))
    return lado * 5

"""Calcula el perimetro del hexagono con uno de sus lados"""
def perimetro_hexagono():
    lado = float(input("Dame el valor del lado: "))
    return lado * 6

"""Calcula el perimetro del trapecio con uno de sus lados,\
    con su base mayor y su base menor"""
def perimetro_trapecio():
    lado = float(input("Dame el valor del lado: "))
    base_mayor = float(input("Dame el valor de la base mayor: "))
    base_menor = float(input("Dame el valor de la base menor: "))
    return lado + lado + base_mayor + base_menor

"""Calcula el perimetro del paralelogramo con dos de sus lados"""
def perimetro_paralelogramo():
    lado_a = float(input("Dame el valor del lado_a: "))
    lado_b = float(input("Dame el valor del lado_b: "))
    return (lado_a * 2) + (lado_b * 2)

"""Calcula el area del triangulo con su base y su altura"""
def area_triangulo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return (base * altura) / 2

"""Calcula el area del cuadrado con uno de sus lados"""
def area_cuadrado():
    lado = float(input("Dame el valor del lado: "))
    return lado * lado

"""Calcula el area del rectangulo con su base y su altura"""
def area_rectangulo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return base * altura

"""Calcula el area del circulo con su radio y pi"""
"""Aqui se utiliza la biblioteca math"""
"""https://docs.python.org/es/3/library/math.html"""
def area_circulo():
    radio = float(input("Dame el valor del radio: "))
    PI = math.pi
    return PI * (radio ** 2)

"""Calcula el area del rombo con su diagonal mayor y menor"""
def area_rombo():
    diagonal_mayor = float(input("Dame el valor de la diagonal mayor: "))
    diagonal_menor = float(input("Dame el valor de la diagonal menor: "))
    return (diagonal_mayor * diagonal_menor) / 2

"""Calcula el area del pentagono con su lado y su apotema"""
def area_pentagono():
    lado = float(input("Dame el valor del lado: "))
    apotema = float(input("Dame el valor de la apotema: "))
    return (5 * lado * apotema) / 2

"""Calcula el area del hexagono con su lado y su apotema"""
def area_hexagono():
    lado = float(input("Dame el valor del lado: "))
    apotema = float(input("Dame el valor de la apotema: "))
    return (6 * lado * apotema) / 2

"""Calcula el area del trapecio con su base mayor y menor, y su altura"""
def area_trapecio():
    base_mayor = float(input("Dame el valor de la base mayor: "))
    base_menor = float(input("Dame el valor de la base menor: "))
    altura = float(input("Dame el valor de la altura: "))
    return ((base_mayor + base_menor) * altura) / 2

"""Calcula el area del paralelogramo con su base y su altura"""
def area_paralelogramo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return base * altura

"""Se agregan todas las funciones junto a los ciclos y operadores\ 
    de decision para crear el programa central"""
def main():
    figuras = ["1) Triángulo", "2) Cuadrado", "3) Rectángulo", "4) Círculo", 
               "5) Rombo", "6) Pentágono", "7) Trapecio", "8) Paralelogramo"]
    for figura in figuras:
        print(figura)
    figura = int(input("Elige una figura: "))

    opciones = ["1) Área", "2) Perímetro", "3) Ambos"]
    for opcion in opciones:
        print(opcion)
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        if figura == 1:
            print("Área del triángulo:", area_triangulo())
        elif figura == 2:
            print("Área del cuadrado:", area_cuadrado())
        elif figura == 3:
            print("Área del rectángulo:", area_rectangulo())
        elif figura == 4:
            print("Área del círculo:", area_circulo())
        elif figura == 5:
            print("Área del rombo:", area_rombo())
        elif figura == 6:
            print("Área del pentágono:", area_pentagono())
        elif figura == 7:
            print("Área del trapecio:", area_trapecio())
        elif figura == 8:
            print("Área del paralelogramo:", area_paralelogramo())
        else:
            print("Figura no válida.")

    elif opcion == 2:
        if figura == 1:
            print("Perímetro del triángulo:", perimetro_triangulo())
        elif figura == 2:
            print("Perímetro del cuadrado:", perimetro_cuadrado())
        elif figura == 3:
            print("Perímetro del rectángulo:", perimetro_rectangulo())
        elif figura == 4:
            print("Perímetro del círculo:", perimetro_circulo())
        elif figura == 5:
            print("Perímetro del rombo:", perimetro_rombo())
        elif figura == 6:
            print("Perímetro del pentágono:", perimetro_pentagono())
        elif figura == 7:
            print("Perímetro del trapecio:", perimetro_trapecio())
        elif figura == 8:
            print("Perímetro del paralelogramo:", perimetro_paralelogramo())
        else:
            print("Figura no válida.")

    elif opcion == 3:
        if figura == 1:
            print("Área del triángulo:", area_triangulo())
            print("Perímetro del triángulo:", perimetro_triangulo())
        elif figura == 2:
            print("Área del cuadrado:", area_cuadrado())
            print("Perímetro del cuadrado:", perimetro_cuadrado())
        elif figura == 3:
            print("Área del rectángulo:", area_rectangulo())
            print("Perímetro del rectángulo:", perimetro_rectangulo())
        elif figura == 4:
            print("Área del círculo:", area_circulo())
            print("Perímetro del círculo:", perimetro_circulo())
        elif figura == 5:
            print("Área del rombo:", area_rombo())
            print("Perímetro del rombo:", perimetro_rombo())
        elif figura == 6:
            print("Área del pentágono:", area_pentagono())
            print("Perímetro del pentágono:", perimetro_pentagono())
        elif figura == 7:
            print("Área del trapecio:", area_trapecio())
            print("Perímetro del trapecio:", perimetro_trapecio())
        elif figura == 8:
            print("Área del paralelogramo:", area_paralelogramo())
            print("Perímetro del paralelogramo:", perimetro_paralelogramo())
        else:
            print("Figura no válida.")
    else:
        print("Opción no válida.")

repetir = 1
while repetir == 1:
    main()
    repetir = int(input("Si quieres volver a realizar \
                        la operación, pon 1, sino pon 0: "))
else:
    print("Hasta luego")
