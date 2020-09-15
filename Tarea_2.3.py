#Dados 3 valores (horas, minutos y segundos) se pide sumar un segundo. 
#NIKI WARA MAMANI QUISPE   C.I.:7618515
h=int(input("Ingrese la hora\n"))
m=int(input("Ingrese los minutos\n"))
s=int(input("Ingrese los segundos\n"))
s=s+1
if(s>59):
    p=s//60
    s=s%60
    m=m+p
    if(m>59):
        q=m//60
        m=m%60
        h=h+p
        if(h>23):
            t=h//24
            h=h%24
print(format(h, '02'),":",format(m, '02'),":",format(s, '02'))