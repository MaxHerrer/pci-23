import math

def perimetro_triangulo():
    lado = float(input("Dame el valor del lado: "))
    return lado + lado + lado

def perimetro_cuadrado():
    lado = float(input("Dame el valor del lado: "))
    return lado * 4

def perimetro_rectangulo():
    lado_a = float(input("Dame el valor del lado_a: "))
    lado_b = float(input("Dame el valor del lado_b: "))
    return (lado_a * 2) + (lado_b * 2)

def perimetro_circulo():
    radio = float(input("Dame el valor del radio: "))
    PI = math.pi
    return 2 * PI * radio

def perimetro_rombo():
    lado = float(input("Dame el valor del lado: "))
    return lado * 4

def perimetro_pentagono():
    lado = float(input("Dame el valor del lado: "))
    return lado * 5

def perimetro_hexagono():
    lado = float(input("Dame el valor del lado: "))
    return lado * 6

def perimetro_trapecio():
    lado = float(input("Dame el valor del lado: "))
    base_mayor = float(input("Dame el valor de la base mayor: "))
    base_menor = float(input("Dame el valor de la base menor: "))
    return lado + lado + base_mayor + base_menor

def perimetro_paralelogramo():
    lado_a = float(input("Dame el valor del lado_a: "))
    lado_b = float(input("Dame el valor del lado_b: "))
    return (lado_a * 2) + (lado_b * 2)

def area_triangulo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return (base * altura) / 2

def area_cuadrado():
    lado = float(input("Dame el valor del lado: "))
    return lado * lado

def area_rectangulo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return base * altura

def area_circulo():
    radio = float(input("Dame el valor del radio: "))
    PI = math.pi
    return PI * (radio ** 2)
  
def area_rombo():
    diagonal_mayor = float(input("Dame el valor de la diagonal mayor: "))
    diagonal_menor = float(input("Dame el valor de la diagonal menor: "))
    return (diagonal_mayor * diagonal_menor) / 2

def area_pentagono():
    lado = float(input("Dame el valor del lado: "))
    apotema = float(input("Dame el valor de la apotema: "))
    return (5 * lado * apotema) / 2

def area_hexagono():
    lado = float(input("Dame el valor del lado: "))
    apotema = float(input("Dame el valor de la apotema: "))
    return (6 * lado * apotema) / 2

def area_trapecio():
    base_mayor = float(input("Dame el valor de la base mayor: "))
    base_menor = float(input("Dame el valor de la base menor: "))
    altura = float(input("Dame el valor de la altura: "))
    return ((base_mayor + base_menor) * altura) / 2

def area_paralelogramo():
    base = float(input("Dame el valor de la base: "))
    altura = float(input("Dame el valor de la altura: "))
    return base * altura

def main():
    figuras = ["1) Triángulo", "2) Cuadrado", "3) Rectángulo", "4) Círculo", "5) Rombo", "6) Pentágono", "7) Trapecio", "8) Paralelogramo"]
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
    repetir = int(input("Si quieres volver a realizar la operación, pon 1, sino pon 0: "))
else:
    print("Hasta luego")
    main()
    repetir = int(input("Si quieres volver a realizar la operación, pon 1, sino pon 0: "))
else:
    print("Hasta luego")
