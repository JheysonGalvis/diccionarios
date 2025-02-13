# --------------------Página 10-----------------------------

# En python un diccionario es un tipo de contenedor que almacena pares clave - valor, cada valor en un diccionario está asociado a una clave que actúa como identificador. Aquí te explico los aspectos de los diccionarios en Python:

# Declaración de un Diccionario:
# Puedes declarar un diccionario utilizando llaves {} 

# Diccionario de Pokémon de Ash
# Diccionario de Pokémon de Ash
pokemones_de_ash = {
    'pikachu': 'El compañero inseparable de Ash, tipo Eléctrico.',
    'bulbasaur': 'Tipo Planta/Veneno, se negó a evolucionar y es muy leal.',
    'charmander': 'Tipo Fuego, abandonado por su entrenador original, evolucionó a Charizard.',
    'squirtle': 'Tipo Agua, líder del Escuadrón Squirtle, siempre con sus gafas de sol.'
}

mi_familia = {
    'mama' : 'yuddy',
    'abuela' : 'emma',
    'mujer' : 'michelle',
    'tio' : 'leo',
    'gato' : 'pandita'
}




# Acceso a elementos por clave: Accede a los elementos de un diccionario utilzando sus claves.

valor_asociado_a_la_clave = mi_familia['mama']
print(valor_asociado_a_la_clave)
print(mi_familia.keys())

valor_asociado_a_la_clave1 = pokemones_de_ash['pikachu']
print(valor_asociado_a_la_clave1)

# ---------------------Página 11-----------------------------

# Modificación y Adición de Elementos: Puedes modificar el valor asociado a una clave existente o agregar nuevas parejas clave - valor.

pokemones_de_ash['pikachu'] = 'Una rata amarilla'
print(pokemones_de_ash)
# Agregar un nuevo elemento al diccionario
pokemones_de_ash['mew'] = 'protagonista de la primera pelicula de Pokemon'
print(pokemones_de_ash)

# Eliminación de Elementos: Puedes eliminar elementos de un diccionario utilizando la clave correspondiente.

del pokemones_de_ash['mew']
print(pokemones_de_ash)

# ---------------------Página 12-----------------------------

# Verificación de Existencia en Claves: Puedes verificar si una clave existe en un diccionario utilizando el operador in

existe_clave_pikachu = 'pikachu' in pokemones_de_ash
print(existe_clave_pikachu)

existe_clave_mew = 'mew' in pokemones_de_ash
print(existe_clave_mew)

# Longitud del Diccionario: Puedes obtener la cantidad de elementos de un diccionario con la función len().

cantidad_de_elementos = len(pokemones_de_ash)
print(cantidad_de_elementos)

# ---------------------Página 13-----------------------------

# Iteración a través de claves, valores o elementos: Puedes iterar a través de las claves, valores o pares clave - valor en un diccionario:

for clave in pokemones_de_ash:
    valor = pokemones_de_ash[clave]
    print(f"{clave}: {valor}")
    
#f-string en Python,  permite incluir variables dentro de una cadena de texto de manera más clara y legible.

# ---------------------Página 14-----------------------------

# Diccionarios Anidados: Puedes tener diccionario dentro de diccionarios, creando así estructuras más complejas.

mi_top_5_de_canciones = {
            'kany Garcia': {
                'demasiado bueno': 2012,
                'confieso': 2019
                },
            'queen': {
                'killer queen': 1974,
                'dont Stop Me Now': 1978
                },
            'fangoria':{
                'un poco de todo': 2023
            },
            'dua Lipa':{
                'training season': 2024,
                'breaking my heart': 2020,
            }
            
}
print(mi_top_5_de_canciones['dua Lipa']['training season'])
# Mensaje personalizado con el resultado
print(f"Mi canción favorita de Dua Lipa se lanzó en '{mi_top_5_de_canciones['dua Lipa']['training season']}' 🎶🔥")

"""🔹 Explicación:

Cada artista es una clave en el diccionario.
El valor asociado a cada clave es otro diccionario con canciones y su año de lanzamiento.
Puedes acceder a una canción específica usando diccionario['Artista']['Canción']."""

# ---------------------Ejercicios página 16 -----------------------------------------------

# Creación de Tuplas:

# Cree una tupla llamada mi_tupla con tres elementos de tu elección.

mi_tupla = (1, 2, 3)
print(mi_tupla)

# Intente modificar un elemento de la tupla. ¿Que pasa?

# mi_tupla[0] = 4     
# print(mi_tupla)

# Sale un error porque las tuplas son inmutables.

# Desempaquetado de Tuplas:

# Cree una tupla de dos elementos llamada coordenadas con valores de latitud y longitud.

coordenadas = (40.7128, -74.0060)
# Utilice el desempaquetado de tuplas para asignar estos valores a dos variables distintas.
latitud, longitud = coordenadas
print("Latitud:", latitud)
print("Longitud:", longitud)

# ---------------------Ejercicios página 17 -----------------------------------------------

# Operaciones Básicas con Diccionarios:

# Cree un diccionario llamado mi_diccionario con al menos tres pares clave valor

mi_diccionario = {'clave1': 1, 'clave2': 2, 'clave3': 3}
print(mi_diccionario) 

# Agregue una nueva clave-valor a mi_diccionario.

mi_diccionario['clave4'] = 4
print(mi_diccionario)

# Imprima solo las claves del diccionario.

print(mi_diccionario.keys())

# Imprima solo los valores del diccionario.

print(mi_diccionario.values())

# Diccionarios Anidados

# Cree un diccionario anidado llamado contactos con información de al menos dos personas (nombre, edad, etc)

contactos = {
    'persona1': {
        'nombre': 'Juan',
        'edad': 25,
        'telefono': '1234567890'
    },
    'persona2': {
        'nombre': 'Maria',
        'edad': 30,
        'telefono': '9876543210'
    }
}
print(contactos)

# Acceda e imprima información específica de una persona utilizando el diccionario anidado.

persona1 = contactos['persona1']
print(persona1['nombre'])
print(persona1['edad'])
print(persona1['telefono'])

# Iteración y actualización

# Utilice un bucle for para imprimir todas las claves y valores de mi_diccionario.

for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
    
# Actualice el valor de una clave en mi_diccionario.

mi_diccionario['clave2'] = 20
print(mi_diccionario)

# Operaciones Básicas:

# Cree una lista vacía llamada mi_lista

mi_lista = []

# Agregue los números del 1 al 5 a mi_lista.

for i in range(1, 6):
    mi_lista.append(i)
print(mi_lista)

# Imprima mi_lista

print(mi_lista)

# Elimine el número 3 de mi_lista.

mi_lista.remove(3)
print(mi_lista)

# Rebanado de listas:

# Cree una lista llamada números del 1 al 10.

numeros_del_1_al_10 = list(range(1, 11))
print(numeros_del_1_al_10)

# Imprima los primeros tres elementos de la lista.

print(numeros_del_1_al_10[:3])

# Imprima los elementos desde el tercero hasta el sexto

print(numeros_del_1_al_10[2:6])     

# Imprima los últimos dos elementos.

print(numeros_del_1_al_10[-2:])

# Listas y ciclos

# Utilice un bucle for para imprimir cada elemento de mi_lista.

for elemento in mi_lista:
    print(elemento)