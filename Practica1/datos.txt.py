with open("datos.txt","w") as f:
    f.write("Hola Mundo")

with open("datos.txt", "r") as f:
    contenido = f.read
    print(contenido)