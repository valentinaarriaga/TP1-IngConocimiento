#1. Crea un código que imprima en pantalla la expresión “Mi Primer Código En Python.”
print("Mi primer Codigo en Python")

#2. Crea un código que imprima en pantalla la siguiente expresión.
print("1| A  B    C")
print("2| D  E    F")
print("3| G  H    I")

#3. Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
#¿Qué estás estudiando?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).
estudiando = input("¿Que estas estudiando? ")
print(estudiando)

#4. Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
#¿En qué país vives?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).
pais = input("¿En que pais vives? ")
print(pais)

#5. Declara dos variables, llamadas nombre y edad.
#Asigna a la variable nombre el valor "David Bowman", y a la edad, el valor 51
nombre = "David Bowman"
edad = 51

#6. Crea tres variables: nombre, apellido y nombrecompleto
#A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts".
#Finalmente, construye la variable nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio).
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print(nombrecompleto)

#7. Declara la variable materia, asígnale el valor "Ingeniería del conocimiento", y muestra en pantalla la frase:
#Estás estudiando “materia”
#Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable.
#Recuerda agregar un espacio antes de concatenar la variable al resto del texto.
materia = "Ingenieria del conocimiento"
print("Estas estudiando " +materia)

#8. Convierte el valor de num1 (num1=35) en un int e imprime el tipo de dato que resulta
num1 = 35
num1Int = int(num1)
print(type(num1Int))

#9. Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
#“Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)”

nombre_asociado = input("¿Como es su nombre de asociado? ")
numero_asociado = input("¿Como es su numero de asociado? ")
print("Estimado/a " +nombre_asociado+ ", su número de asociado es: " +numero_asociado+ ".")

#10. Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.
division = 874/27
print(division)




