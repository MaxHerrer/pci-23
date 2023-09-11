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
  perimetro = lado + lado + lado
  print("El perimetro del triangulo es",perimetro)
perimetro_triangulo()

def perimetro_cuadrado():
  lado = float(input("Dame el valor del lado "))
  perimetro = lado * 4
  print("El perimetro del cuadrado es de",perimetro)

def perimetro_rectangulo():
  lado_a = float(input("Dame el valor del lado_a "))
  lado_b = float(input("Dame el valor del lado_b "))
  perimetro = (lado_a * 2) + (lado_b * 2)
  print("El perimetro del rectangulo es de",perimetro)
perimetro_rectangulo()

def perimetro_circulo():
  diametro = float(input("Dame el valor del diametro "))
  PI = 3.1416
  perimetro = diametro * PI
  print("El perimetro del circulo es de",perimetro)
perimetro_circulo()

def perimetro_rombo():
  lado = float(input("Dame el valor del lado "))
  perimetro = lado * 4
  print("El perimetro del rombo es de",perimetro)
perimetro_rombo()

def perimetro_pentagono():
  lado = float(input("Dame el valor del lado "))
  perimetro = lado * 5
  print("El perimetro del pentagono es de",perimetro)
perimetro_pentagono()

def perimetro_hexagono():
  lado = float(input("Dame el valor del lado "))
  perimetro = lado * 6
  print("El perimetro del hexagono es de",perimetro)
perimetro_hexagono()

def perimetro_trapecio():
  lado = float(input("Dame el valor del lado "))
  base_mayor = float(input("Dame el valor de la base_mayor "))
  base_menor = float(input("Dame el valor de la base_menor "))
  perimetro = lado + lado + base_mayor + base_menor
  print("El perimetro del trapecio es de",perimetro)
perimetro_trapecio()

def perimetro_paralelogramo():
  lado_a = float(input("Dame el valor del lado_a "))
  lado_b = float(input("Dame el valor del lado_b "))
  perimetro = (lado_a * 2) + (lado_b * 2)
  print("El perimetro del paralelogramo es de",perimetro)
perimetro_paralelogramo()

def area_triangulo():
  base = float(input("Dame el valor de la base "))
  altura = float(input("Dame el valor de la altura "))
  area= (base * altura) / 2
  print("El area del triangulo es de",area)
area_triangulo()

def area_cuadrado():
  lado = float(input("Dame el valor del lado "))
  area= lado * lado
  print("El area del cuadrado es de",area)
area_cuadrado()

def area_rectangulo():
  base = float(input("Dame el valor del base "))
  altura = float(input("Dame el valor de la altura "))
  area= base * altura
  print("El area del rectangulo es de",area)
area_rectangulo()

def area_circulo():
  radio = float(input("Dame el valor del radio "))
  PI = 3.1416
  perimetro = PI * (radio ** 2)
  print("El perimetro del circulo es de",perimetro)
area_circulo()

def area_rombo():
  diametro_mayor = float(input("Dame el valor del diametro_mayor "))
  diametro_menor = float(input("Dame el valor del diametro_menor "))
  area= (base * altura) / 2
  print("El area del rombo es de",area)
area_rombo()

def area_pentagono():
  lado = float(input("Dame el valor del lado "))
  altura = float(input("Dame el valor de la altura "))
  perimetro = lado * 5
  area= (perimetro * altura) / 2
  print("El area del pentagono es de",area)
area_pentagono()

def area_pentagono():
  lado = float(input("Dame el valor del lado "))
  altura = float(input("Dame el valor de la altura "))
  perimetro = lado * 6
  area= (perimetro * altura) / 2
  print("El area del pentagono es de",area)
area_pentagono()

def area_trapecio():
  altura = float(input("Dame el valor de la altura "))
  base_mayor = float(input("Dame el valor de la base_mayor "))
  base_menor = float(input("Dame el valor de la base_menor "))
  area = (base_mayor * base_menor) * altura / 2
  print("El are del trapecio es de",area)
area_trapecio()
