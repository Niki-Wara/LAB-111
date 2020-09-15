# 2. Utilizando los coeficientes (a, b, c) de una ecuación de 
# segundo grado se pide mostrar la naturaleza de sus raíces
#NOMBRE:NIKI WARA MAMANI QUISPE   C.I.:7618515
from math import sqrt

a = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
b = int(input("Ingrese el coeficiente de la variable lineal\n"))
c = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0

if ((b**2)-4*a*c) < 0:
  print("La ecuacion no tiene soluciones reales")
else:
  x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
  x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
  print("Las dos soluciones reales son:")
  print(x1)
  print(x2)
print("Finalizo el programa")