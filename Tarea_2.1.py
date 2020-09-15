#1. Ingrese un tiempo X que estará representado en segundos, luego ingrese el tiempo que tomará
#en realizarse una tarea Z representado en segundos, minutos y horas. Se pide verificar si con el
#tiempo X se puede finalizar la tarea Z
#NIKI WARA MAMANI QUISPE   C.I.:7618515
segundos=int(input("Ingrese el tiempo en segundos\n"))
segundos2=int(input("Ingrese la tarea a realizarse en segundos\n"))
print("seleccione una opcion\n")
print("1.- Convertir los segundos en hora, minutos y segundos(X)")
print("2.- Convertir el tiempo de trabajo de segundos en hora, minutos y segundos(Z)")
print("3.- Verificar si con el tiempo X se puede finalizar la tarea Z")
o=int(input())
if(o==1):
    dias = segundos // (24*60*60)
    segundos = segundos % (24*60*60)
    horas = segundos // (60*60)
    segundos = segundos % (60*60)
    minutos = segundos // 60
    segundos = segundos // 60
    print(format(dias, '02'),":",format(horas, '02'),":",format(minutos, '02'),":",format(segundos, '02'))
elif(o==2):
    dias2 = segundos2 // (24*60*60)
    segundos2 = segundos2 % (24*60*60)
    horas2 = segundos2 // (60*60)
    segundos2 = segundos2 % (60*60)
    minutos2 = segundos2 // 60
    segundos2 = segundos2 // 60
    print(format(dias2, '02'),":",format(horas2, '02'),":",format(minutos2, '02'),":",format(segundos2, '02'))
elif(o==3):
    if(segundos==segundos2):
        print("Los tiempos son iguales")
    else:
        print("Los tiempos no son iguales")
else:
    print("operacion invalida")