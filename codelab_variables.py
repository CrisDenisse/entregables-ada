"""Codelab: variables python
Codelab Variables Python

1 Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso
2 Crea un nuevo archivo .py
3 Define una variable de cada tipo de primitivo
4 Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
5 Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
6 Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
7 Imprimir los resultados de las tareas anteriores
8 Envía el link del archivo en el repositorio con las respuesta"""

#Define una variable de cada tipo de primitivo
#string 
pais= "Soy de Venezuela"
#entero
edad= 29
#flotante 
tamaño= 1.60
#booleano 
boolean = True

#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
resultado_concatenacion = pais + " tengo " + str(edad) + " años y mido " + str(tamaño) + " " + str(boolean)

#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

"""Límite de enteros: ±(2^31 - 1) para sistemas de 32 bits y ±(2^63 - 1) para sistemas de 64 bits
Límite de flotantes: alrededor de 1.8e308 para números positivos y 2.2e-308 para números negativos"""

#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
# Define una variable de tipo entero
n = 7 

# Aplica la fórmula de la suma de los primeros n números pares
suma_pares = n * (n + 1)

# Imprime el resultado de la suma de los primeros n números pares
print("Resultado de la suma de los primeros", n, "números pares:", suma_pares)

#Imprimir los resultados de las tareas anteriores
print("Resultado de la concatenación:", resultado_concatenacion)
print("Resultado de la suma de los primeros", n, "números pares:", suma_pares)





