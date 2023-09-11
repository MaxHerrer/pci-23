# Proyecto
Repo almacenar ejercicios y ejemplos de clase "Pensamiento Computacional para Ingenieria" TC1028.411

# Avance 1: Selección de proyecto
El tema va a ser de un programa la cual te va a ayudar a calcular el area y perimetro de las principales figuras geometricas las cuales son:
- El Triangulo
- El Cuadrado
- El Rectangulo
- El Circulo
- El Rombo
- El Pentagono
- El Hexagono
- El Trapecio
- El Pararelogramo

Esto se hace con el objetivo de poder crear un programa el cual solamente decir que se busca obtener y con cual figura ya solamente te pida los datos para asi mismo esto ya solamente los tenga que terminar haciendo.

# Algoritmo
Su algoritmo va a ser de preguntarle al usuario de que es lo que quiere obtener si el area, el perimetro o ambos, y luego se preguntara cual sera la figura que se necesitara.

Pasos:
  1. Pedir al usuario si quiere calcular el area, el perimetro o ambos.
  2. Si elijes area solamente se calculara este.
  3. Se le preguntara cual de las figuras mostradas necesita calcular su area.
  4. Si elijes perimetro solamente se calculara este.
  5. Se le preguntara cual de las figuras mostradas necesita calcular su perimetro.
  6. Si elijes ambos solamente se calculara este.
  7. Se le preguntara cual de las figuras mostradas necesita calcular su area y su perimetro.

def area_paralelogramo()
  base = float(input("Dame el valor del base "))
  altura = float(input("Dame el valor de la altura "))
  area= base * altura
  print("El area del paralelogramo es de",area)
area_paralelogramo()
