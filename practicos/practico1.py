# Mostrar por pantalla: “Hola Mundo, esto es Python!”.

# print('!Hola Mundo, esto es Python¡');

# Escriba un programa que solicite el nombre del usuario y luego muestre el mensaje de salida

# nombre = input('A continuacion introduzca su nombre: ');
# print('Hola ' + nombre);

# Solicite al usuario su nombre y luego solicite su apellido y por último muestre el mensaje de
# salida “Hola nombre apellido”.

# nombreYApellido = input('Introduzca su nombre: ') + ' ' + input('Introduzca su apellid: ');
# print('Hola ' + nombreYApellido);

# Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en pantalla: “La
# respuesta es XX”.

# sum = int(input('Por favor, ingrese el primer numero: ')) + int(input('Por favor, ingrese el segundo numero: '));

# print(sum);

# Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”.

# sum = int(input('Por favor, ingrese el primer numero: ')) + int(input('Por favor, ingrese el segundo numero: '));

# multiplicacion = int(input('Ingrese el numero por el cual desea multiplicar: ')) * sum;

# print(multiplicacion);

# Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

# cuenta = int(input('Introduzca el precio total de la cuenta: '));
# comensa = int(input('Introduzca la cantidad de comensales: '));

# divi = round(cuenta / comensa);

# print('Cada uno debera pagar:', divi);


# Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días.

# dias = int(input('Ingrese un numero de dias: '))

# horas = dias * 24;
# minutos = dias * 1440;
# segundos = dias * 86400;

# print('Su dia tiene horas', horas, 'minutos', minutos, 'y segundo', segundos);


# Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
# luego imprimir por pantalla la superficie total.

# b = int(input('Ingrese la base: '))
# a = int(input('Ingrese la altura: '))
# s = round(b * a / 2);

# print(s);

# Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

# text = str(input('Ingrese un texto: '))

# invertir = text[::-1]

# print(invertir);

# Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
# derecho que al revés. Por ejemplo: rayar, kayak, somos.

# def esPolindromo(palabra):
#     if str(palabra) == str(palabra)[::-1]:
#         return 'Es polindromo'
#     else:
#         return 'No es polindromo'

# print(esPolindromo('rayar'));


# Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
# de texto ingresada por el usuario.

# cadena = "holaaaaa";

# print(str(cadena[0:5]))

# Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
# día, mes y año. Ej:
# Usuario ingresa: 17/05/1985
# Programa imprime: Día: 17, Mes: 05 y Año: 1985

# fecha = input('Ingrese una fecha en formato dd/mm/aaaa: ')
# fecha = fecha.split('/')
# dia = fecha[0];
# mes = fecha[1];
# año = fecha[2];

# print('Dia:',dia,'Mes:',mes,'Año:',año);












