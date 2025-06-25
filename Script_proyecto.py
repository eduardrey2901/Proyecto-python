# %%
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def diccionario(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra.isalpha():
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

cadena = "cadena de caracteres de prueba"    
diccionario(cadena)

# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def multiplica_por_2(num):
    return num*2

lista1 = [2, 4, 5, 32, 54, 2, 5, 8]
lista_resultado = list(map(multiplica_por_2, lista1))
print (f"La lista con el doble de cada valor de la lisat inicial es: {lista_resultado}")

# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista
# con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabra(lista_palabras, palabra_objetivo):
    lista_resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            lista_resultado.append(palabra)
    print (f"Las palabras que contienen '{palabra_objetivo}' són: {lista_resultado}")

lista_1 = ['resolución', 'soledad', 'amigos', 'sociedad', 'casualidad', 'mesón', 'consolar']
buscar_palabra(lista_1, 'sol')

# %%
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia(lista_1, lista_2):
    resultado = map(lambda x, y: x - y, lista_1, lista_2)
    print (list(resultado))

lista_num1 = [85, 35, 22, 36, 28, 56, 99, 35, 65, 24, 8]
lista_num2 = [63, 24, 21, 26, 13, 12, 30, 26, 55, 3, 2]
diferencia(lista_num1, lista_num2)

# %%
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5.
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado",
# de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def estado(lista_1, nota_aprobado = 5):
    if sum(lista_1)/len(lista_1) >= nota_aprobado:
        result = 'aprobado'
    else:
        result = 'suspenso'
    resultado = (sum(lista_1)/len(lista_1), result)
    return resultado

lista = [6, 7, 4, 3, 7, 5, 7, 3, 9, 2]
nota_aprobado = 5.3
estado_clase = estado(lista, nota_aprobado)
print (estado_clase)


# %%
#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(num):
    if num < 0:
        return "El factoral no está definido para números negativos"
    elif num == 1 or num == 0:
        return 1
    return num * factorial(num-1)

print (factorial(6))

# %%
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

datos = [(1, 2), (3, 4), (5, 6)]
resultado = list(map(lambda t: str(t), datos))
print (resultado, type(resultado))

# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

print("Por favor, ingrese dos numeros para divirlos (recuerda que el divisor no puede ser 0):")
while True:
    try:
        dividendo = float(input("Dividendo: "))
        divisor = float(input("Divisor: "))
        if (divisor == 0):
            print("La división no fue exitosa, recuerda que el divisor debe ser distinto de 0")
            continue
        break
    except ValueError:
        print ("Debes introducir numeros, no cadenas de caracteres")
resultado = dividendo/divisor
print (f'La división fue exitosa {resultado}')

# %%
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def excluir(lista):
    lista_prohib = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda t: t not in lista_prohib, lista))

lista_1 = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Canguro", "calamar", "Perro", "Gato"]
resultado = excluir(lista_1)
print (resultado)


# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

def promedio(lista):
    try:
        resultado = sum(lista)/len(lista)
        print (f"El promedio es {resultado}")
    except TypeError:
        print("Ha habido un problema, la lista contiene algo que no son numeros, revise de nuevo la lista")
    except ZeroDivisionError:
        print("Ha habido un problema, la lista esta vacia, revise de nuevo la lista")

lista = []
promedio(lista)


# %%
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

print("Por favor, ingrese su edad")
while True:
    try:
        edad = int(input("Edad: "))
        if (edad <= 0 or edad >= 120):
            print("Su edad es incorrecta, sale del rango esperado (mayor que 0 y menor que 120), introduzca de nuevo su edad")
            continue
        break
    except ValueError:
        print ("Debes introducir numeros, no cadenas de caracteres")
print (f'El usuario tiene: {edad} años')

# %%
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def contar(cadena):
    suma = 0
    for c in cadena:
        suma += 1
    return suma

cadena = "hola me llamo edu"
palabras = cadena.split()
resultado = list(map(lambda x: contar(x), palabras))
print (resultado)

# %%
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def tuplas_letras(cadena):
    letras = []
    for l in cadena:
        if l.lower() not in [x.lower() for x in letras]:
            letras.append(l)
    return list(map(lambda y: (y.upper(), y.lower()), letras))

cadena = ("abCDeEFgH")
resultado = tuplas_letras(cadena)
print (resultado)

# %%
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

lista = ["Casa", "Examen", "Moto", "Avión", "", "Camioneta", "Cocodrilo"]
letra = "E"
print (list(filter(lambda palabra: palabra.startswith(letra), lista)))

# %%
#15. Crea una función lambda que sume 3 a cada número de una lista dada.

lista = [1, 4, 2, 45, 23, 5, 33, 25, 2, 5, 67, 123, 55, 82]
print (list(map(lambda x: x+3, lista)))

# %%
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n.
# Usa la función filter()

def lista_palabras(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda x: len(x) > n, palabras))

texto = "El lenguaje python es muy interesante"
num = 3
resultado = lista_palabras(texto, num)
print (resultado)

# %%
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572).
# Usa la función reduce()

from functools import reduce

numeros = [3, 5, 2]
print (reduce(lambda x, y: x*10 + y , numeros))



# %%
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter
#para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 87},
    {"nombre": "María", "edad": 19, "calificacion": 91},
    {"nombre": "Carlos", "edad": 21, "calificacion": 76},
    {"nombre": "Sofía", "edad": 20, "calificacion": 90}
]

mejores_estudiantes = list(filter(lambda x: x["calificacion"] >= 90, estudiantes))

for estudiante in mejores_estudiantes:
    print (estudiante)

# %%
#19. Crea una función lambda que filtre los números impares de una lista dada.

numeros = [37, 92, 5, 48, 76, 14, 61, 89, 23, 70]
print (list(filter(lambda x: x%2 != 0, numeros)))

# %%
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

elementos = [42, "manzana", 87, "sol", 13, "guitarra", "nube", 59, "río", 26]
print (list(filter(lambda x: type(x) == int, elementos)))

# %%
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

numero_cubo = lambda x: x**3
print (numero_cubo(7))

# %%
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()

numeros = [4, 6, 10]
print (reduce(lambda x, y: x*y, numeros))

# %%
#23. Concatena una lista de palabras.Usa la función reduce() 

palabras = ["montaña", "luz", "libro", "camino", "nube", "tierra", "cielo", "río", "puerta", "tiempo"]
print(reduce(lambda x, y: x +' '+ y, palabras))

# %%
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
from functools import reduce

numeros = [4, 15, 9, 2, 20]
diferencia_total = reduce(lambda acumulado, y: acumulado + abs(y-acumulado), numeros, 0)
print(diferencia_total)

# %%
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contador_caracteres(cadena):
    caracteres = 0
    for i in cadena:
        caracteres += 1
    return caracteres

cadena = "El sol brilla intensamente en el cielo azul."
print (contador_caracteres(cadena))

# %%
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

num1 = 27
num2 = 12
resto = lambda x, y: x%y
print (resto(num1, num2))

# %%
#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    acum = 0
    for i in lista:
        acum += i
    return acum/len(lista)

lista = [5, 6, 6, 7, 9, 8]
print (promedio(lista))

# %%
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def duplicado(lista):
    lista_aux = []
    for i in lista:
        if (i in lista_aux):
            return i
        else:
            lista_aux.append(i)
    return "No hay duplicados"

lista = [10, "manzana", 3.14, True, "perro", "calamar"]
elemento_duplicado = duplicado(lista)
print (elemento_duplicado)

# %%
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

from functools import reduce

def encriptar(elemento):
    contador = 0
    cadena = str(elemento)
    resultado = []
    for i in cadena:
        if (len(cadena) - contador <= 4):
            resultado.append(i)
        else:
            resultado.append('#')
        contador += 1
    return (reduce(lambda x, y: x + y, resultado))

variable = 3242353445
print (encriptar(variable))
        
    

# %%
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def anagrama(palabra_1, palabra_2):
    if(len(palabra_1)!=len(palabra_2)):
        return "No son anagramas"
    else:
        for i in range(len(palabra_1)):
            if palabra_1[i].lower() != palabra_2[len(palabra_1)-i-1].lower():
                return "No son anagramas"
        return "Si que son anagramas"

#Código corregido
def son_anagramas(palabra_1, palabra_2):
    return sorted(palabra_1.lower()) == sorted(palabra_2.lower())


palabra_1 = "amargana"
palabra_2 = "anagrama"
print (anagrama(palabra_1, palabra_2))
                

# %%
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista,
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def encontrar_nombre():
    try:
        lista_nombres = input(f"Lista de nombres, separalos por comas: ")
        nombres = [nombre.strip().lower() for nombre in lista_nombres.split(",")]       #he puesto el .lower() si te dejas la inicial mayúscula tambien encontrará el nombre
        nombre_buscado = input("Nombre buscado: ")
        if nombre_buscado.lower() in nombres:
            print (f"El nombre {nombre_buscado} ha sido encontrado")
        else:
            raise ValueError(f"El nombre {nombre_buscado} no esta en la lista")
    except ValueError as error:
        print (error)

encontrar_nombre()

# %%
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista,
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def puesto_trabajo(empleado_buscado, lista_empleados):
    for empleado in lista_empleados:
        if empleado_buscado.lower() == empleado['nombre'].lower():
            return (f"{empleado_buscado} trabaja como {empleado['puesto']}")
    return (f"{empleado_buscado} no trabaja aquí")
        
    


empleados = [
    {"nombre": "Ana García", "puesto": "Gerente"},
    {"nombre": "Luis Pérez", "puesto": "Analista"},
    {"nombre": "Carlos Gómez", "puesto": "Desarrollador"},
    {"nombre": "Pepito Vencedor", "puesto": "Técnico"}
]
nombre_buscado = "Carlos Gómez"
print (puesto_trabajo(nombre_buscado, empleados))

# %%
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista_1 = [2, 4, 2, 6, 2, 1]
lista_2 = [3, 5, 2, 1, 5, 3]
suma = map(lambda x, y: x + y, lista_1, lista_2)
print (list(suma))

# %%
"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.

Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol. """

class Arbol:
    def __init__(self, tronco = 1, ramas = None):
        self.tronco = tronco
        self.ramas = ramas if ramas is not None else []
        
    def crecer_tronco(self):
        self.tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)
    
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
    
    def quitar_rama(self, posicion):
        del self.ramas[posicion-1]
    
    def info_arbol(self):
        print (f"La longitud del tronco es de {self.tronco} unidad/es")
        print (f"El árbol tiene {len(self.ramas)} ramas")
        print (f"La longitud de las ramas son: {self.ramas} unidad/es")
        
#1. Crear un árbol.
objeto = Arbol()
#2. Hacer crecer el tronco del árbol una unidad.
objeto.crecer_tronco()
#3. Añadir una nueva rama al árbol.
objeto.nueva_rama()
#4. Hacer crecer todas las ramas del árbol una unidad.
objeto.crecer_ramas()
#5. Añadir dos nuevas ramas al árbol.
objeto.nueva_rama()
objeto.nueva_rama()
""" Se podría hacer de esta forma para añadir mas ramas a la vez
        def nueva_rama(self, numero_ramas):
            for i in range(numero_ramas):
                self.ramas.append(1)
"""
#6. Retirar la rama situada en la posición 2.
objeto.quitar_rama(2)
#7. Obtener información sobre el árbol.
objeto.info_arbol()

# %%
"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia"."""

class UsuarioBanco:
    
    def __init__(self, nombre, saldo, cc):
        self.nombre = nombre
        self.saldo = saldo
        self.cc = cc
    
    def retirar_dinero(self, cantidad):
        try:
            if (self.saldo < cantidad):
                raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} unidades, tu saldo es de {self.saldo}")
            else:
                self.saldo -= cantidad
                print (f"{self.nombre}, tu saldo ahora es de {self.saldo}")
                return True
        except ValueError as error:
            print (error)
            return False
            
        
        
    def transferir_dinero(self, usuario_2, cantidad):
        if (self.retirar_dinero(cantidad) == True):
            usuario_2.agregar_dinero(cantidad)
            print(f"El saldo de {self.nombre} ahora es de {self.saldo}")
            print(f"El saldo de {usuario_2.nombre} ahora es de {usuario_2.saldo}")
        
        
    def agregar_dinero(self, cantidad_2):
        self.saldo += cantidad_2
        print(f"El saldo de {self.nombre} ahora es de {self.saldo}")

#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
Alicia = UsuarioBanco("Alicia", 100, True)    
Bob = UsuarioBanco("Bob", 50, True)
#2. Agregar 20 unidades de saldo de "Bob".
Bob.agregar_dinero(30)
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
Bob.transferir_dinero(Alicia, 80)
#4. Retirar 50 unidades de saldo a "Alicia"."""
Alicia.retirar_dinero(50)

# %%
"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras , eliminar_palabra.
Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.

Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto"""

def contar_palabras(texto):
    resultado = {}
    palabras = texto.split()
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1
    return (resultado)
    

def reemplazar_palabras(palabra_original, palabra_nueva, texto):    
    palabras = texto.split()
    texto_nuevo = []
    for palabra in palabras:
        if palabra == palabra_original:
            texto_nuevo.append(palabra_nueva)
        else:
            texto_nuevo.append(palabra)
    
    resultado = " ".join(texto_nuevo)
    return (resultado)


def eliminar_palabra(palabra_eliminar, texto):
    palabras = texto.split()
    texto_nuevo = []
    for palabra in palabras:
        if palabra != palabra_eliminar:
            texto_nuevo.append(palabra)
    resultado = " ".join(texto_nuevo)
    return (resultado)


def procesar_texto(texto):
    while True:
        decision = input("Que quieres hacer, 'contar', 'reemplazar' o 'eliminar': ")
        if (decision == "contar"):
            print (contar_palabras(texto))
            break
        elif (decision == "reemplazar"):
            palabra_orig = input("¿Que palabra quieres reemplazar?")
            palabra_nueva = input("¿Por que palabra la quieres reemplazar?")
            print (reemplazar_palabras(palabra_orig, palabra_nueva, texto))
            break
        elif (decision == "eliminar"):
            palabra_eliminar = input("¿Que palabra quieres eliminar?")
            print (eliminar_palabra(palabra_eliminar, texto))
            break
        else:
            print ("Esta acción no existe, solo puedes elegir 'contar', 'reemplazar' o 'eliminar', prueba otra vez")
        
    
texto = "El sol brilla y el sol calienta. La luna brilla por la noche y la noche es tranquila. El sol y la luna son cuerpos celestes."
procesar_texto(texto)

# %%
#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

from datetime import datetime

entrada = input("Introduce una hora en formato HH:MM: ")
try:
    hora = datetime.strptime(entrada, "%H:%M")
    if (hora >= datetime.strptime("15:00", "%H:%M") and hora < datetime.strptime("21:00", "%H:%M")):
        print (f"A las {hora.strftime('%H:%M')} es por la tarde")
    elif (hora >= datetime.strptime("6:00", "%H:%M") and hora < datetime.strptime("15:00", "%H:%M")):
        print(f"A las {hora.strftime('%H:%M')} es de día")
    else:
        print(f"A las {hora.strftime('%H:%M')} es de noche")
except ValueError:
    print("Formato incorrecto, debes usar HH:mm")
    


# %%
"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
0 - 69 insuficiente
70 - 79 bien
80 - 89 muy bien
90 - 100 excelente"""

def calificacion(puntuacion):
    if (puntuacion >= 0 and puntuacion <= 69):
        print ("Insuficiente")
    elif (puntuacion >= 70 and puntuacion <= 79):
        print ("Bien")
    elif (puntuacion >= 80 and puntuacion <= 89):
        print("Muy bien")
    elif (puntuacion >= 90 and puntuacion <= 100):
        print ("Excelente")
    else:
        print ("Recuerda que debes introducir un numero entre 0 y 100")

try:
    cal_num = float(input("Introduce la calificación del alumno (0 - 100): "))
    calificacion(cal_num)
except ValueError:
    print ("Recuerda que debes introducir un numero entre 0 y 100, no puedes introducir otros caracteres")


# %%
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y
# datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    try:
        if (figura.lower() == "rectangulo"):
            base, altura = datos
            area = base*altura
            print (f"El area del rectangulo es: {area}")
        elif (figura.lower() == "circulo"):
            (radio,) = datos
            area = radio*radio*math.pi
            print (f"El area del circulo es: {area}")
        elif (figura.lower() == "triangulo"):
            base, altura = datos
            area = (base*altura)/2
            print (f"El area del triangulo es: {area}")
        else:
            print ("No tenemos esta figura")
    except ValueError:
        print("¡Cuidado! La cantidad de datos no es la correcta")
    except TypeError:
        print("¡Cuidado! Los datos deben ser numéricos")
        
datos_rec = (6, 3)
datos_cir = (5,)
datos_tri = (6, 4)
calcular_area("circulo", datos_cir)

# %%
"""41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea,
después de aplicar un descuento. El programa debe hacer lo siguiente:

1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python."""

def aplicar_descuento(precio, descuento):
    if (descuento > precio_original):
        return 0.0
    else:
        precio -= descuento
    return (precio)

try:
    precio_original = float(input("Introduce el precio original del articulo que quieres comprar: "))
    cupon = str(input("¿Tienes un cupón de descuento? (sí/no): "))
    if (cupon.lower() == "sí" or cupon.lower() == "si"):
        descuento = float(input("Ingresa el valor del cupón de descuento: "))
        if (descuento > 0):
            precio_final = aplicar_descuento(precio_original, descuento)
        else:
            precio_final = precio_original
        print (f"El precio final del artículo es de {precio_final}")
    elif (cupon.lower() == "no"):
        precio_final = precio_original
        print (f"El precio final del artículo es de {precio_final}")
    else:
        print ("Debes introducir 'sí' o 'no', empieza de nuevo.")
except ValueError:
    print("Debes introducir numeros tanto en el precio original como en el dupón de descuento, prueba otra vez.")


