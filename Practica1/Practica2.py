print ("Hola Mundo")
nombre="Ana"
edad= 20
print ("Nombre:" , nombre)
print ("Edad:" , edad)

# input muestra el texto que pongas entre comillas y espera que el usuario escriba algo
usuario= input ("Escribe su Nombre")
print ("Hola:" , usuario)

# operaciones aritméticas
a,b= 10,3
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)

# operaciones Logicos == != ><  >=  <=
print(a>b, a==10, b!=5)

#Comodines
print("Hola %s" % "Ana")
print("Tengo %d años" %25)  
print("PI= %f" %3.1416)  # número completo
print("PI= %.2f" %3.1416)  # 2 decimales
nombre="Ana"
edad= 30
print("Hola me llamo %s y tengo %d" %(nombre, edad))

# While
i= 1
while i<5:
     print(i)
     i += 1  # incrementa i en 1

# For
for j in range(5):
     print(j)

# if
x=10
if x >0:
     print("El valor es positivo")
elif x==0:
     print("El numero es 0")
else:
     print("El valor es negativo")

#Diccionarios | mapas
estudiante={
     "nombre": "Ana",
     "edad": 20,
     "carrera": "Ingenieria"
}
print(estudiante["nombre"])
estudiante["edad"]=30
estudiante["nota"]=4.5
print(estudiante["nombre"],estudiante["nota"], estudiante["carrera"])

# listas
numeros=[0,1,2,3]
print(numeros[0])  # Imprime el primer elemento (0)
numeros.append(9) # Agrega el número 9 a la lista
numeros.remove(3)  # Elimina el valor 3 de la lista
print (len(numeros))  # Imprime la longitud de la lista
datos=["texto",30, True] # Lista con distintos tipos de datos
numeros[1]=5  # Cambia el valor en la posición 1 por 5
print(numeros) 

#Funciones
def mutliplicar (primero, segundo):
    return primero*segundo
print (mutliplicar(3,2))

