# Calculos de Perimetros
import math

# El Triangulo

lado = float(input("Dame el valor del lado "))
perimetro = lado + lado + lado
print("El perimetro del triangulo es",perimetro)

# El Cuadrado

lado = float(input("Dame el valor del lado "))
perimetro = lado * 4
print("El perimetro del cuadrado es de",perimetro)

# El Rectangulo

lado_a = float(input("Dame el valor del lado_a "))
lado_b = float(input("Dame el valor del lado_b "))
perimetro = (lado_a * 2) + (lado_b * 2)
print("El perimetro del rectangulo es de",perimetro)

# El Circulo

diametro = float(input("Dame el valor del diametro "))
PI = 3.1416
perimetro = diametro * PI
print("El perimetro del circulo es de",perimetro)

# El Rombo

lado = float(input("Dame el valor del lado "))
perimetro = lado * 4
print("El perimetro del rombo es de",perimetro)

# El Pentagono

lado = float(input("Dame el valor del lado "))
perimetro = lado * 5
print("El perimetro del rpentagono es de",perimetro)

# El Hexagono

lado = float(input("Dame el valor del lado "))
perimetro = lado * 6
print("El perimetro del hexagono es de",perimetro)

# El Trapecio

lado = float(input("Dame el valor del lado "))
base_mayor = float(input("Dame el valor de la base_mayor "))
base_menor = float(input("Dame el valor de la base_menor "))
perimetro = lado + lado + base_mayor + base_menor
print("El perimetro del trapecio es de",perimetro)

# El Pararelogramo

lado_a = float(input("Dame el valor del lado_a "))
lado_b = float(input("Dame el valor del lado_b "))
perimetro = (lado_a * 2) + (lado_b * 2)
print("El perimetro del paralelogramo es de",perimetro)

# Calculos de Areas

# El Triangulo

base = float(input("Dame el valor de la base "))
altura = float(input("Dame el valor de la altura "))
area= (base * altura) / 2
print("El area del triangulo es de",area)

# El Cuadrado

lado = float(input("Dame el valor del lado "))
area= lado * lado
print("El area del cuadrado es de",area)

# El Rectangulo

base = float(input("Dame el valor del base "))
altura = float(input("Dame el valor de la altura "))
area= base * altura
print("El area del rectangulo es de",area)

# El Circulo

radio = float(input("Dame el valor del radio "))
PI = 3.1416
perimetro = PI * (radio ** 2)
print("El perimetro del circulo es de",perimetro)

# El Rombo

diametro_mayor = float(input("Dame el valor del diametro_mayor "))
diametro_menor = float(input("Dame el valor del diametro_menor "))
area= (base * altura) / 2
print("El area del rombo es de",area)

# El Pentagono

lado = float(input("Dame el valor del lado "))
altura = float(input("Dame el valor de la altura "))
perimetro = lado * 5
area= (perimetro * altura) / 2
print("El area del pentagono es de",area)

# El Hexagono

lado = float(input("Dame el valor del lado "))
altura = float(input("Dame el valor de la altura "))
perimetro = lado * 6
area= (perimetro * altura) / 2
print("El area del pentagono es de",area)

# El Trapecio

altura = float(input("Dame el valor de la altura "))
base_mayor = float(input("Dame el valor de la base_mayor "))
base_menor = float(input("Dame el valor de la base_menor "))
area = (base_mayor * base_menor) * altura / 2
print("El are del trapecio es de",area)

# El Pararelogramo

base = float(input("Dame el valor del base "))
altura = float(input("Dame el valor de la altura "))
area= base * altura
print("El area del paralelogramo es de",area)

# Funciones

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

# Condicional IF

opcion = int(input("Para obtener el área, pon 1, para el perímetro, pon 2 y para ambos, pon 3: "))
figura = int(input("Para triángulo pon 1, para cuadrado pon 2, para rectángulo pon 3, para círculo pon 4, para rombo pon 5, para pentágono pon 6, para trapecio pon 7 y para paralelogramo pon 8: ")) 
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

# Ciclos

repetir = int(input("Si quieres volver a realizar la operación, pon 1, sino pon 0: "))
while repetir == 1:
    opcion = int(input("Para obtener el área, pon 1, para el perímetro, pon 2 y para ambos, pon 3: "))
    figura = int(input("Para triángulo pon 1, para cuadrado pon 2, para rectángulo pon 3, para círculo pon 4, para rombo pon 5, para pentágono pon 6, para trapecio pon 7 y para paralelogramo pon 8: ")) 
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
        
    repetir = int(input("Si quieres volver a realizar la operación, pon 1, sino pon 0: "))
