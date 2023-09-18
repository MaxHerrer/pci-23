# Calculos de Perimetros

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
  lado = float(input("Dame el valor del lado "))
  return lado + lado + lado

def perimetro_cuadrado():
  lado = float(input("Dame el valor del lado "))
  return lado * 4

def perimetro_rectangulo():
  lado_a = float(input("Dame el valor del lado_a "))
  lado_b = float(input("Dame el valor del lado_b "))
  return (lado_a * 2) + (lado_b * 2)

def perimetro_circulo():
  diametro = float(input("Dame el valor del diametro "))
  PI = 3.1416
  return diametro * PI

def perimetro_rombo():
  lado = float(input("Dame el valor del lado "))
  return lado * 4

def perimetro_pentagono():
  lado = float(input("Dame el valor del lado "))
  return lado * 5

def perimetro_hexagono():
  lado = float(input("Dame el valor del lado "))
  return lado * 6

def perimetro_trapecio():
  lado = float(input("Dame el valor del lado "))
  base_mayor = float(input("Dame el valor de la base_mayor "))
  base_menor = float(input("Dame el valor de la base_menor "))
  return lado + lado + base_mayor + base_menor

def perimetro_paralelogramo():
  lado_a = float(input("Dame el valor del lado_a "))
  lado_b = float(input("Dame el valor del lado_b "))
  return (lado_a * 2) + (lado_b * 2)

def area_triangulo():
  base = float(input("Dame el valor de la base "))
  altura = float(input("Dame el valor de la altura "))
  return (base * altura) / 2

def area_cuadrado():
  lado = float(input("Dame el valor del lado "))
  return lado * lado

def area_rectangulo():
  base = float(input("Dame el valor del base "))
  altura = float(input("Dame el valor de la altura "))
  return base * altura

def area_circulo():
  radio = float(input("Dame el valor del radio "))
  PI = 3.1416
  return PI * (radio ** 2)
  
def area_rombo():
  diametro_mayor = float(input("Dame el valor del diametro_mayor "))
  diametro_menor = float(input("Dame el valor del diametro_menor "))
  return (diametro_mayor * diametro_menor) / 2

def area_pentagono():
  lado = float(input("Dame el valor del lado "))
  altura = float(input("Dame el valor de la altura "))
  perimetro = lado * 5
  return (perimetro * altura) / 2

def area_hexagono():
  lado = float(input("Dame el valor del lado "))
  altura = float(input("Dame el valor de la altura "))
  perimetro = lado * 6
  return (perimetro * altura) / 2

def area_trapecio():
  altura = float(input("Dame el valor de la altura "))
  base_mayor = float(input("Dame el valor de la base_mayor "))
  base_menor = float(input("Dame el valor de la base_menor "))
  return (base_mayor * base_menor) * altura / 2

def area_pararelogramo():
  base = float(input("Dame el valor de la base "))
  altura = float(input("Dame el valor de la altura "))
  return base * altura

# Condicional IF

opcion = input("Para obtener el area tienes que poner 1, para del perimetro 2 y para ambos 3")
figura = input("Escribe que figura quieres obtener en minusculas")
if opcion == 1:
    if figura == "triangulo":
        area_triangulo()
    elif figura == "cuadrado":
        area_cuadrado()
    elif figura == "rectangulo":
        area_rectangulo()
    elif figura == "circulo":
        area_circulo()
    elif figura == "rombo":
        area_rombo()
    elif figura == "pentagono":
        area_pentagono()
    elif figura == "trapecio":
        area_trapecio()
    elif figura == "paralelogramo":
        area_pararelogramo()
elif opcion == 2:
    if figura == "triangulo":
        perimetro_triangulo()
    elif figura == "cuadrado":
        perimetro_cuadrado()
    elif figura == "rectangulo":
        perimetro_rectangulo()
    elif figura == "circulo":
        perimetro_circulo()
    elif figura == "rombo":
        perimetro_rombo()
    elif figura == "pentagono":
        perimetro_pentagono()
    elif figura == "trapecio":
        perimetro_trapecio()
    elif figura == "paralelogramo":
        perimetro_paralelogramo()
elif opcion == 3:
    if figura == "triangulo":
        area_triangulo()
        perimetro_triangulo()
    elif figura == "cuadrado":
        area_cuadrado()
        perimetro_cuadrado()
    elif figura == "rectangulo":
        area_rectangulo()
        perimetro_rectangulo()
    elif figura == "circulo":
        area_circulo()
        perimetro_circulo()
    elif figura == "rombo":
        area_rombo()
        perimetro_rombo()
    elif figura == "pentagono":
        area_pentagono()
        perimetro_pentagono()
    elif figura == "trapecio":
        area_trapecio()
        perimetro_trapecio()
    elif figura == "paralelogramo":
        area_pararelogramo()
        perimetro_paralelogramo()
else:
    print("No existe la opcion")
