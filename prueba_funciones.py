import os
import json

def cargarDatos():
    with open("biblioteca.json", mode="r") as archivoJson:
        leerJson = json.load(archivoJson)
        return leerJson

def escribirDatos(datos):
    with open("biblioteca.json", mode="w") as escribirJson:
        json.dump(datos, escribirJson, indent=4)

def mostrarCosas():
    datos = cargarDatos()
    for i in datos["Autor"]:
        print(i["AutorID"], i["Nombre"], i["Nacionalidad"])
    for i in datos["Categoria"]:
        print(i["CategoriaID"], i["Nombre"])
    for i in datos["Libro"]:
        print(i["LibroID"],i["Titulo"], i["AutorID"], i["CategoriaID"], i["AnoPublicacion"], i["ISBN"])

def agregarAutor(nombre, nacionalidad):
    datos = cargarDatos()
    nuevoAutor = {
        "AutorID":len(datos["Autor"])+1,
        "Nombre": nombre,
        "Nacionalidad": nacionalidad
    }
    datos["Autor"].append(nuevoAutor)

    escribirDatos(datos)

def agregarLibro(titulo, autorID, categoriaID, anoPublicacion, iSBN):
    datos = cargarDatos()
    nuevoLibro = {
        "LibroID":len(datos["Libro"])+1,
        "Titulo": titulo,
        "AutorID": autorID,
        "CategoriaID": categoriaID,
        "AnoPublicacion": anoPublicacion,
        "ISBN": iSBN
    }
    datos["Libro"].append(nuevoLibro)

    escribirDatos(datos)

def editarAutor(id:int, autor:str, nacionalidad:str):
    datos = cargarDatos()
    contador = 0
    for i in datos["Autor"]:
        if i["AutorID"] == id:
            print("Lo encontre!")
        contador+1
    
    datos["Autor"][contador]["Nombre"] = autor
    datos["Autor"][contador]["Nacionalidad"] = nacionalidad

    escribirDatos(datos)

def eliminarAutor(id:int):
    datos = cargarDatos()
    contador = 0
    for i in datos["Autor"]:
        if i["AutorID"] == id:
            print("Lo encontre!")
        contador+1

    datos["Autor"][contador].pop

    escribirDatos(datos)


    

