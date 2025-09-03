
catalogo={
    "001":{"titulo":"cien Años de soledad","autor":"Gabriel Garcia Marquez","estado":"disponible"},
    "002":{"titulo":"El Amor en los tiempos del Colera","autor":"Gabriel Garcia Marquez","estado":"disponible"},
    "003":{"titulo": "La Vorágine", "autor": "José Eustasio Rivera", "estado": "disponible"},
    "004":{"titulo": "María", "autor": "Jorge Isaacs", "estado": "prestado"},
    "005":{"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "estado": "disponible"},
}

def mostrar_catalogo():
    """Muestra todos los libros del catálogo con su información y estado"""
    print("\n--- Catálogo de Libros ---")
    for codigo, datos in catalogo.items():  # recorremos cada libro
        estado = "Disponible" if datos["estado"] == "disponible" else "Prestado"
        print(f"{codigo}: {datos['titulo']} - {datos['autor']} [{estado}]")

def buscar_libro():
    """Busca un libro por código"""
    codigo = input("Ingrese el código del libro a buscar: ")
    if codigo in catalogo:  # Verificamos si existe
        datos = catalogo[codigo]
        estado = "Disponible" if datos["estado"] == "disponible" else "Prestado"
        print(f"{codigo}: {datos['titulo']} - {datos['autor']} [{estado}]")
    else:
        print("Error: El código ingresado no existe.")

def prestar_libro():
    """Permite prestar un libro, si está disponible"""
    codigo = input("Ingrese el código del libro a prestar: ")
    if codigo in catalogo:
        if catalogo[codigo]["estado"] == "disponible":
            catalogo[codigo]["estado"] = "prestado"
            print(f"Has prestado: {catalogo[codigo]['titulo']} ({catalogo[codigo]['autor']})")
        else:
            print("Este libro ya está prestado.")
    else:
        print("Error: El código ingresado no existe.")

def devolver_libro():
    """Permite devolver un libro, si está prestado"""
    codigo = input("Ingrese el código del libro a devolver: ")
    if codigo in catalogo:
        if catalogo[codigo]["estado"] == "prestado":
            catalogo[codigo]["estado"] = "disponible"
            print(f"Has devuelto: {catalogo[codigo]['titulo']} ({catalogo[codigo]['autor']})")
        else:
            print("Este libro ya está disponible.")
    else:
        print("Error: El código ingresado no existe.")

def agregar_libro():
    """Agrega un nuevo libro al catálogo"""
    codigo = input("Ingrese el código único del libro: ")
    if codigo in catalogo:  # Validamos que no se repita el código
        print("Error: Ese código ya existe en el catálogo.")
    else:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        catalogo[codigo] = {"titulo": titulo, "autor": autor, "estado": "disponible"}
        print(f"Libro agregado exitosamente: {codigo} - {titulo} ({autor})")

# ------------------ MENÚ PRINCIPAL ------------------

def menu():
    while True:  # bucle infinito hasta que el usuario elija salir
        print("\n--- Menú Biblioteca ---")
        print("1: Ver catálogo de libros")
        print("2: Buscar libro por código")
        print("3: Prestar libro")
        print("4: Devolver libro")
        print("5: Agregar libro nuevo")
        print("0: Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            agregar_libro()
        elif opcion == "0":
            print("Gracias por usar la Biblioteca Digital.")
            break  # Salimos del bucle y del programa
        else:
            print("Opción inválida, por favor intente de nuevo.")

# ------------------ EJECUCIÓN ------------------
menu()