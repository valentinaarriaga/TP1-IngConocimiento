#21. Ordenamiento de datos con tuplas:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación.
#La función debe devolver la lista ordenada por puntuación de mayor a menor.
#puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar_puntuaciones(lista):
    return sorted(lista, key=lambda p: p[1], reverse=True)

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

ordenadas = ordenar_puntuaciones(puntuaciones)

print("Puntuaciones ordenadas:")
for nombre, puntaje in ordenadas:
    print(f"{nombre}: {puntaje}")

#22. Planificación de viajes con tuplas y diccionarios:
#Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla
#(destino, precio, duración en días).
#Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves
#y el precio total (precio por día * duración) como valor.

def calcular_precios(paquetes):
    resultado = {}
    for destino, precio, dias in paquetes:
        total = precio * dias
        resultado[destino] = total
    return resultado

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

precios_totales = calcular_precios(paquetes)

print("Precios totales por destino:")
for destino, precio in precios_totales.items():
    print(f"{destino}: ${precio}")

#23. Gestión de inventario con arrays:
#Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico
#y su valor es la cantidad disponible. Escribe una función que reciba el array de inventario
#y un número de productos vendidos (otro array) y devuelva el inventario actualizado.

def actualizar_inventario(inventario, ventas):
    inventario_actualizado = []
    for stock, vendidos in zip(inventario, ventas):
        inventario_actualizado.append(stock - vendidos)
    return inventario_actualizado

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

nuevo_inventario = actualizar_inventario(inventario, ventas)

print("Inventario actualizado:", nuevo_inventario)

#24. Organización de eventos con *args:
#Consigna: Escribe una función que reciba un número variable de nombres de eventos
#y los imprima en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.
def organizar_eventos(*args):
    print("Lista de eventos:")
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

#25. Análisis financiero con **kwargs:
#Consigna: Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs
#y calcule el balance final. La función debe manejar ingresos como positivos y gastos como negativos.

def analizar_finanzas(**kwargs):
    balance = sum(kwargs.values())
    return balance

resultado = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)

print(f"Balance final: {resultado}")

#26. Registro de empleados con tuplas y **kwargs:
#Consigna: Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios,
#y otros datos como dirección, número de teléfono, etc., como **kwargs.
#La función debe devolver un diccionario con toda la información del empleado.

def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario
    }
    empleado.update(kwargs)
    return empleado

empleado1 = registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")
empleado2 = registro_empleado("Martin", 26, 8000, direccion="Palmares 123", telefono="234567890")

print(empleado1)
print(empleado2)

#27. Estadísticas de ventas con arrays:
#Consigna: Escribe una función que reciba un array con las ventas de cada mes y
#devuelva un diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def estadisticas_ventas(ventas):
    if not ventas:
        return {"total": 0, "promedio": 0, "mes_max": None}

    total = sum(ventas)
    promedio = total / len(ventas)
    indice_max = ventas.index(max(ventas))

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    return {
        "total": total,
        "promedio": promedio,
        "mes_max": meses[indice_max]
    }

resultado = estadisticas_ventas(ventas_mensuales)

print("Estadísticas de ventas:")
print(f"Total anual: {resultado['total']}")
print(f"Promedio mensual: {resultado['promedio']:.2f}")
print(f"Mes con mayores ventas: {resultado['mes_max']}")

#28. Organización de una biblioteca con diccionarios:
#Consigna: Una biblioteca registra sus libros en un diccionario donde la clave es el título del libro
#y el valor es otro diccionario con la información del autor, año de publicación, y género.
#Escribe una función que reciba este diccionario y devuelva una lista de todos los libros publicados después del año 2000.

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libros_post_2000(biblioteca):
    libros = []
    for titulo, info in biblioteca.items():
        if info["año"] > 2000:
            libros.append(titulo)
    return libros

resultado = libros_post_2000(biblioteca)

print("Libros publicados después del 2000:")
for libro in resultado:
    print(libro)

#29. Registro de notas con tuplas y arrays:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante
#y sus calificaciones en un array. La función debe devolver un diccionario con el nombre del estudiante como clave
#y su promedio de calificaciones como valor.

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedios_estudiantes(notas_estudiantes):
    resultado = {}
    for nombre, calificaciones in notas_estudiantes:
        promedio = sum(calificaciones) / len(calificaciones)
        resultado[nombre] = promedio
    return resultado

promedios = promedios_estudiantes(notas_estudiantes)

print("Promedio de calificaciones por estudiante:")
for estudiante, promedio in promedios.items():
    print(f"{estudiante}: {promedio:.2f}")

#30. Configuración de perfiles de usuario con **kwargs y arrays:
#Consigna: Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs.
#La función debe devolver un diccionario donde la clave es el nombre del usuario
#y el valor es un array con las configuraciones aplicadas.

def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        # Guardamos las configuraciones como lista de pares clave=valor
        perfiles[usuario] = [f"{clave}={valor}" for clave, valor in kwargs.items()]
    return perfiles

usuarios = ["Ana", "Luis", "María"]

perfiles_config = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

print("Perfiles de usuario configurados:")
for usuario, configuraciones in perfiles_config.items():
    print(f"{usuario}: {configuraciones}")








