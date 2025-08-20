#11. Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
num = 10.676767
numRound = round(num)
print(numRound)

#12. Gestión de inventario con tuplas:
#Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible.
#Representa cada producto como una tupla (nombre, precio, cantidad).
#Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
#productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

productos = [
    ("laptop", 1200, 5),
    ("mouse", 25, 50),
    ("teclado", 100, 30)
]

def producto_mas_caro(lista_productos):
    return max(lista_productos, key=lambda p: p[1])

mas_caro = producto_mas_caro(productos)

print("El producto más caro es:", mas_caro[0], "con un precio de $", mas_caro[1])

#13. Registro de estudiantes con diccionarios:
#Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario
#con nombre, edad y calificaciones en distintas materias.
#Escribe una función que reciba el registro de estudiantes y devuelva el promedio de calificaciones de un estudiante
#dado su número de matrícula.

estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedio_estudiante(registro, matricula):
    if matricula in registro:
        calificaciones = registro[matricula]["calificaciones"]
        if not calificaciones:
            return None
        return sum(calificaciones.values()) / len(calificaciones)
    else:
        return None

mat = int(input("Ingrese el numero de matricula: "))
prom = promedio_estudiante(estudiantes, mat)

if prom is not None:
    print(f"Promedio de {estudiantes[mat]['nombre']}: {prom:.2f}")
else:
    print("Matrícula no encontrada o sin calificaciones.")

#14. Análisis de datos meteorológicos con arrays:
#Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array.
#Escribe una función que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.

def analizar_temperaturas(temperaturas_array):
    if not temperaturas_array:
        return None, None, None

    media = sum(temperaturas_array) / len(temperaturas_array)
    maxima = max(temperaturas_array)
    minima = min(temperaturas_array)

    return media, maxima, minima

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]
media, maxima, minima = analizar_temperaturas(temperaturas)

print(f"Temperatura media del mes: {media:.2f}°C")
print(f"Temperatura máxima del mes: {maxima}°C")
print(f"Temperatura mínima del mes: {minima}°C")

#15. Manejo de parámetros variables con *args:
#Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio.
#Utiliza *args para recibir las notas.
#calcular_promedio(85, 90, 78, 92)

def calcular_promedio(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print("El promedio de las notas ingresadas es: ")
print(calcular_promedio(85, 90, 78, 92))

#16. Creación de un perfil de usuario con **kwargs:
#Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico,
#y cualquier otro dato adicional usando **kwargs. La función debe devolver un diccionario con toda la información del usuario.
#crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

def crear_perfil(**kwargs):
    perfil = {}
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil

perfil = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza", telefono="123456789")

print("Perfil creado:")
for k, v in perfil.items():
    print(f"{k}: {v}")

#17. Administración de empleados con tuplas y diccionarios:
#Consigna: Una empresa quiere administrar la información de sus empleados,
#donde cada empleado se representa como una tupla (nombre, edad, salario).
#Escribe una función que reciba un diccionario donde la clave es el ID del empleado
#y el valor es la tupla con su información.
#La función debe devolver un diccionario con los empleados que ganan más de un salario dado.

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def empleados_con_salario_mayor(dic_empleados, salario_minimo):
    resultado = {}
    for id_empleado, datos in dic_empleados.items():
        nombre, edad, salario = datos  # desempaquetar la tupla
        if salario > salario_minimo:
            resultado[id_empleado] = datos
    return resultado

filtrados = empleados_con_salario_mayor(empleados, 2500)

print("Empleados con salario mayor a 2500:")
for id_emp, datos in filtrados.items():
    print(f"ID {id_emp}: Nombre={datos[0]}, Edad={datos[1]}, Salario={datos[2]}")

#18. Procesamiento de ventas con arrays:
#Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array.
#Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]


def procesar_ventas(ventas):
    if not ventas:
        return 0, 0

    total = sum(ventas)
    promedio = total / len(ventas)
    return total, promedio

total, promedio = procesar_ventas(ventas_diarias)

print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio:.2f}")

#19. Análisis de resultados deportivos con diccionarios:
#Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde
#la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos.
#Escribe una función que calcule el total de goles anotados y recibidos en la temporada.

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcular_goles(resultados):
    goles_anotados = 0
    goles_recibidos = 0

    for equipo, (a_favor, en_contra) in resultados.items():
        goles_anotados += a_favor
        goles_recibidos += en_contra

    return goles_anotados, goles_recibidos

a_favor, en_contra = calcular_goles(resultados)

print(f"Total de goles anotados: {a_favor}")
print(f"Total de goles recibidos: {en_contra}")

#20. Configuración de una aplicación con **kwargs:
#Consigna: Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro,
#idioma, notificaciones, etc., usando **kwargs. La función debe devolver un diccionario con las configuraciones aplicadas.
#configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

def configurar_app(**kwargs):
    app = {}
    for clave, valor in kwargs.items():
        app[clave] = valor
    return app

app = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print("Configuraciones de la app:")
for k, v in app.items():
    print(f"{k}: {v}")
