# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor

if numero_1 > numero_2:
    print('{} es mayor que {}'.format(numero_1, numero_2))
else:
    print('{} es mayor que {}'.format(numero_2 , numero_1))


# Imprima en pantalla según corresponda



# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if ( numero_1 % 2 ) == 0:
    print (numero_1, 'es par')
else:
    print (numero_1, 'es impar')
    
if ( numero_2 % 2 ) == 0:
    print (numero_2, 'es par')
else:
    print (numero_2, 'es impar')
# Verifique si el numero_1 es mayor a 0 y menor a 100

if (numero_1 > 0) and (numero_1 < 100):
    print (numero_1, 'es mayor a 0 y es menor que 100')
elif (numero_1 > 0) and (numero_1 > 100):
     print (numero_1, 'no cumple la condiciòn, es mayor que 100')
else:
    print ('es menor a 0')  
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
if (numero_2 > -2) and (numero_2 < 10):
    print (numero_2, 'es mayor a -2 y es menor que 10')
elif (numero_2 > -2) and (numero_2 > 10):
     print (numero_2, 'no cumple la condiciòn, es mayor que 10')
else:
    print (numero_2, 'es menor a -2')  
# Imprima en pantalla si se cumple o no la condición
