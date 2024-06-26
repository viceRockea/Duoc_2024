import prueba_funciones

def landing():
        while True:
            print("**************************************")
            print("************ Mundo Libro **************")
            print("**************************************")
            print("")
            print("[1] - Menu Mantenedor")
            print("[2] - Reportes")
            print("[0] - Salir")
            print("")
            opcionesv1 = int(input("Elige una opcion por favor"))

            if opcionesv1 == 1:
                    menu()
            elif opcionesv1 == 0:
                break

def menu():
    while True:
        print("[1] - Agregar Categoria")
        print("[2] - Editar Categoria")
        print("[3] - Eliminar Categoria")
        print("[4] - Listar Categoria")
        print("[0] - Volver")

        opcionesv2 = int(input("Elige una opcion"))
        if opcionesv2 == 1:
            agregarElemento()
        elif opcionesv2 == 2:
            agregar_nombre = input("Ingresa el nombre porfavor")
            agregar_nacionalidad = input("Ingresa la nacionalidad")
            prueba_funciones.agregarAutor(agregar_nombre, agregar_nacionalidad)
        elif opcionesv2 == 3:
            eliminarElementos()#Listar falta dejarlo mas bonito
        elif opcionesv2 == 4:
            mostrarElementos()#Listar falta dejarlo mas bonito
        elif opcionesv2 == 0:
            break

def agregarElemento():
    print("[1] - Agregar Autor")
    print("[2] - Agregar Libro")
    print("[3] - Agregar Categoria de libros")
    print("[4] - Agregar Usuarios")
    print("[0] - Volver")
    print("")

    while True:
        opcionesv3 = int(input("Elige que quieres agregar"))
        if opcionesv3 == 1:
            agregar_nombre = input("Ingresa el nombre porfavor")
            agregar_nacionalidad = input("Ingresa la nacionalidad")
            prueba_funciones.agregarAutor(agregar_nombre, agregar_nacionalidad)
        if opcionesv3 == 2:
            agregar_nombre = input("Ingresa el nombre porfavor")
            agregar_nacionalidad = input("Ingresa la nacionalidad")
            agregar_nacionalidad = input("Ingresa la nacionalidad")
            agregar_nacionalidad = input("Ingresa la nacionalidad")            
            agregar_nacionalidad = input("Ingresa la nacionalidad")
            prueba_funciones.agregarLibro(agregar_nombre, agregar_nacionalidad)
            opciones = int(input("deseas hacer una accion"))
        elif opciones == 0:
            break

def mostrarElementos():
    prueba_funciones.mostrarCosas()

def eliminarElementos():
    eliminar_id = int(input("Ingresa el id que quieres eliminar"))
    prueba_funciones.eliminarAutor(eliminar_id)
landing()