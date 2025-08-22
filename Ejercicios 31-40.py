#31. Gestión de una red social con **kwargs y arrays:
#Consigna: Escribe una función que administre publicaciones de una red social.
#La función debe recibir el nombre del usuario, el texto de la publicación y
#un número variable de etiquetas usando **kwargs y arrays.
#Además, debe manejar opciones adicionales como visibilidad pública o privada.
#La función debe devolver un diccionario con todos los detalles de la publicación.

def publicar(usuario, texto, **kwargs):
    # Creamos el diccionario base de la publicación
    publicacion = {
        "usuario": usuario,
        "texto": texto,
        "etiquetas": kwargs.pop("etiquetas", [])  # si no se pasan, queda lista vacía
    }

    # Agregamos el resto de parámetros (visibilidad, likes, etc.)
    publicacion.update(kwargs)
    return publicacion


post = publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100)

print(post)

#32. Consigna: Una empresa quiere simular las ventas de diferentes productos.
#Escribe una función que reciba un número variable de ventas (tuplas) donde cada tupla contiene el producto,
#la cantidad vendida, y el precio por unidad. La función debe devolver el total de ingresos generados por las ventas.

def simular_ventas(*args):
    total_ingresos = 0
    for producto, cantidad, precio in args:
        total_ingresos += cantidad * precio
    return total_ingresos

total = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))

print(f"Ingresos totales: ${total:.2f}")

#33. Sistema de reservas con tuplas y diccionarios:
#Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha
#y el valor es una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio.
#Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible
#en la fecha seleccionada.

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def habitacion_disponible(reservas, fecha, habitacion):
    if fecha not in reservas:
        return True

    for _, hab, _ in reservas[fecha]:
        if hab == habitacion:
            return False
    return True

def hacer_reserva(reservas, fecha, huesped, habitacion, precio):
    if not habitacion_disponible(reservas, fecha, habitacion):
        return False

    if fecha not in reservas:
        reservas[fecha] = []

    reservas[fecha].append((huesped, habitacion, precio))
    return True

ok = hacer_reserva(reservas, "2024-08-15", "María", 101, 150)
print("Reserva 1 OK?", ok)

ok = hacer_reserva(reservas, "2024-08-15", "María", 103, 160)
print("Reserva 2 OK?", ok)

print(reservas["2024-08-15"])

#34. Análisis de resultados de encuestas con diccionarios y arrays:
#Consigna: Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde
#la clave es la pregunta y el valor es un array con las respuestas recibidas.
#Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y
#devuelva un diccionario con estos resultados.

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def analizar_encuestas(encuestas):
    resultados = {}
    for pregunta, respuestas in encuestas.items():
        frecuencia = {}
        for r in respuestas:
            frecuencia[r] = frecuencia.get(r, 0) + 1
        resultados[pregunta] = frecuencia
    return resultados

resultado = analizar_encuestas(encuestas)

print("Resultados de encuestas:")
for pregunta, frec in resultado.items():
    print(f"\n{pregunta}")
    for respuesta, cantidad in frec.items():
        print(f"  {respuesta}: {cantidad}")

#35. Optimización de rutas con arrays y tuplas:
#Consigna: Una empresa de logística necesita optimizar sus rutas de entrega.
#Cada ruta se representa como una tupla (origen, destino, distancia).
#Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta.
#La función debe devolver las rutas que cumplen con las restricciones.

def filtrar_rutas(rutas, distancias_max):
    if len(rutas) != len(distancias_max):
        raise ValueError("La cantidad de rutas y de distancias máximas debe coincidir.")

    rutas_validas = []
    for (origen, destino, distancia), max_perm in zip(rutas, distancias_max):
        if distancia <= max_perm:
            rutas_validas.append((origen, destino, distancia))
    return rutas_validas

rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

validas = filtrar_rutas(rutas, distancias_max)
print(validas)

#36. Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs:
#Consigna: Escribe una función que gestione el inventario de una cadena de tiendas.
#La función debe recibir el nombre de la tienda, el producto y la cantidad a actualizar usando **kwargs.
#Debe manejar un diccionario donde la clave es el nombre de la tienda y
#el valor es otro diccionario con los productos y sus cantidades.
#La función debe actualizar el inventario y devolver el estado actual.

inventario = {

    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(tienda, **kwargs):
    if tienda not in inventario:
        inventario[tienda] = {}

    for producto, cambio in kwargs.items():
        # Si el producto no existe en esa tienda, empieza en 0
        inventario[tienda][producto] = inventario[tienda].get(producto, 0) + cambio

    return inventario

estado = actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)

print("Estado actualizado:", estado)

#37. Análisis de tendencias en redes sociales con arrays y tuplas:
#Consigna: Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales.
#Escribe una función que reciba un array de hashtags y una lista de tuplas donde
#cada tupla contiene un hashtag y su frecuencia de uso.
#La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad de veces.

hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizar_tendencias(hashtags, tendencias, umbral):
    resultados = []
    for tag, frecuencia in tendencias:
        if frecuencia > umbral:
            resultados.append(tag)
    return resultados

destacados = analizar_tendencias(hashtags, tendencias, 100)

print("Hashtags en tendencia (más de 100 menciones):")
for h in destacados:
    print(h)

#38. Administración de suscripciones con diccionarios, arrays, y **kwargs:
#Consigna: Escribe una función que gestione las suscripciones a un servicio en línea.
#La función debe recibir el nombre del usuario, el tipo de suscripción (mensual, anual),
#y cualquier otra opción adicional usando **kwargs.
#La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios
#y devolver el estado actualizado.

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}


def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    if usuario not in suscripciones:
        suscripciones[usuario] = []

    suscripciones[usuario].append(suscripcion)

    if kwargs:
        suscripciones[usuario + "_opciones"] = kwargs

    return suscripciones

estado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)

print("Estado actualizado de suscripciones:")
for usuario, datos in estado.items():
    print(usuario, ":", datos)

#39. Simulación de mercado bursátil con arrays y tuplas:
#Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil.
#La función debe recibir un array con los precios diarios de una acción y
#una lista de tuplas donde cada tupla contiene un día y un precio de compra o venta.
#La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado y
#vendido en los días especificados.

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]


def simular_mercado(precios, operaciones):
    beneficio = 0
    accion_en_mano = None

    for operacion, dia in operaciones:
        precio = precios[dia]

        if operacion == "compra":
            if accion_en_mano is None:
                accion_en_mano = precio
        elif operacion == "venta":
            if accion_en_mano is not None:
                beneficio += precio - accion_en_mano
                accion_en_mano = None

    return beneficio

resultado = simular_mercado(precios_diarios, operaciones)
print(f"Beneficio/Pérdida total: {resultado}")

#40. Análisis de rendimiento académico con diccionarios y arrays:
#Consigna: Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias.
#Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID
#y el valor es otro diccionario con las materias y sus respectivas calificaciones (arrays).
#Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.

estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}


def ranking_estudiantes(estudiantes):
    promedios = {}

    for id_est, materias in estudiantes.items():
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas)

        promedio = sum(todas_notas) / len(todas_notas)
        promedios[id_est] = promedio

    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    return ranking

resultado = ranking_estudiantes(estudiantes)

print("Ranking de estudiantes:")
for pos, (id_est, prom) in enumerate(resultado, start=1):
    print(f"{pos}. Estudiante {id_est} - Promedio: {prom:.2f}")


