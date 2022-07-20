n=int(input("Ingrese un número de filas del 1 al 9:"))
while n<1 or n>9: #Esto hará que te pida el número infinitas veces hasta que esté dentro del intervalo
     print("Error")
     n=int(input("Ingrese un número de filas nuevamente:"))

def Piramide (n): #Definimos la función Piramide

    k=n-1

    for i in range (0, n):

        for j in range (0, k):
            print(end=" ")#Agregará un espacio a la izquierda de cada fila

        k=k-1

        for j in range (0, i+1):

             print (j+1, end=" ")# El end=" " Agregará un espacio entre los números de las filas
        print ("\r") #Desplazará las filas de números a la izquierda
Piramide(n)
