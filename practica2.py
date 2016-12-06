print (" --------- PRÁCTICA 2 ------- ")
print (" --------- TIPOS DE DATOS ------- ")
# Uso de la función type  para tipos de datos
"""
print (type (10))
print (type (5.5))
print (type (1+5j))
"""
# Comentar bloques con tres comillas dobles antes y después


print (type (10))
print (type (5.5))
print (type (1+5j))

#Operadores
print()
print ("Manejo de operadores matemáticos")
print ("================================")
#endl="\n\n"
print(2**10)
print (2+4)
print (1+5j)

print()
print ("Manejo de cadena de caracteres")
print ("==============================")
print ('Ángela')
print ("""
Línea 1
Línea 2
Línea 3
""")
print (type ("esto es una cadena"))
#Concatenando cadenas
print ("Concatenando cadenas: ")
print ("cadena 1 " + "cadena 2")
#Multiplicación de una cadena por un escalar
print ("cadena 1 "*3)

#Valores booleanos
print (type(True))

#Operadores a nivel de bit
print (3 & 1)
print (3 & 2)
print (3 << 1)
print (3 << 2)
print ()

#Operadores de acumulación
a = 10
a = a + 9
print (a)
a +=9
print (a)
print ()

#Operadores lógicos
a = True
resultado = a and True
print (resultado)
print ()

#Operadores de comparación
res = a == 2
print (res)
print ()

nombre1 = "Ángela"
nombre2 = "Ángela"
print (nombre1 == nombre2)
print ()

nombre1 = "Ángela"
nombre2 = "Ángeles"
print (nombre1 != nombre2)
print ()

nombre1 = "Ángela"
nombre2 = "Ángeles"
print (nombre1 > nombre2)
print ()

anio_nacimiento = 1986
print ("Mayor de edad")
print ((2016 - anio_nacimiento) >= 18)
print ()

edad = 15
print ("Adolescente ?? - rango de 12 a 18 años")
#print ( edad >= 12 and edad <= 18 )    ambas líneas son equivalentes
print ( 12 <= edad <= 18 )
print ()

edad = 60
print ("Edad no laboral ??")
print ( 1 <= edad <= 18 or  80 <= edad <= 120)
print ()

