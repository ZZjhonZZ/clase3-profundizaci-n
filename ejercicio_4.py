# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '10'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
numtxt1 = str(texto_1)
numtxt2 = str(texto_2)

if numtxt1 > numtxt2:
    print (numtxt1, 'es mayor alfabeticamente que ', numtxt2)
else:
    print (numtxt2, 'es mayor alfabeticamente que ', numtxt1)
    

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
num1 = int(numtxt1)
num2 = int(numtxt2)

# Compare las nuevas variables para ver cual es mayor o menor
if num1 > num2:
    print (num1, 'es mayor numericamente que', num2)
else:
    print (num2, 'es mayor numericamene que ', num2)
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
