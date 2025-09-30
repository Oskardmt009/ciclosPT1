## 1. Algoritmo para imprimir números del 1 al 10

for num in range(1,11):
    
    print(num)

##2. Algoritmo para sumar los primeros 10 números

sum = 0

for num1 in range (1,11):
    sum = sum + num1
print(sum)

## //3. Algoritmo para generar la tabla de un numero dado por argumento en una función

def tablaMultiplicar(num2):
    for i in range(1,11):
        print(f"{num2} x {i} = {num2 * i}")

   
tablaMultiplicar(7)

## 4 Algoritmo para contar ocurrencias de 'a' en un texto

def cuentaA(word):
    cont = 0
    for letra in word:
        if letra.lower() == 'a':
            cont += 1
    print(cont)

cuentaA("matematicas")  # Salida: 3

## 5. Algoritmo para calcular el factorial de un número

def factorial(num3):
    mult=1
    for i in range(1,num3):
        mult=mult*i
    print(mult)

factorial(6)

#6. Escribe una función que reciba un array de números y devuelva un 
# nuevo array que contenga solo los números pares.

def pair(numP): # definimos la función
    numPares = [] # creamos el arreglo donde se almacenará los números pares
    for j in range(len(numP)): # se crea el ciclo for hasta la última posición
        if numP[j] % 2 == 0: # valida que sea par
            numPares.append(numP[j]) # agrega solo los números pares al nuevo arreglo
    return numPares # retorna numPares.

numP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pair(numP):
    return [n for n in numP if n % 2 == 0]
print(pair(numP))

#7. Implementa una función que calcule la suma 
# de los cuadrados de los primeros N números naturales.

def sumaPotencia(pot):
    suma = 0
    for i in range(1, pot + 1):
        suma += i ** 2
    print(suma)

sumaPotencia(10)

# 8 Escribe una función que calcule la potencia de un número (base^exponente) 
# utilizando un ciclo for, sin usar el operador de potencia **.

def potencia(base, exp):
    res = 1
    for k in range(1, exp + 1):
        res = res*base
    print(res)
potencia(2,6)



# 9 Desarrolla una función que genere y devuelva los primeros N términos 
# de la serie de Fibonacci.

def fibonacci(num3):
    cont1 = 0
    cont2 = 1
    for i in range(num3):
        print(cont1)
        serie = cont1 + cont2
        cont1 = cont2
        cont2 = serie

fibonacci(10)

def fibonacci(num3):
    cont1 = 0
    cont2 = 1
    resultado = []
    for i in range(num3):
        resultado.append(cont1)
        serie = cont1 + cont2
        cont1 = cont2
        cont2 = serie
    return resultado

print(fibonacci(10))

#10 Desarrolla una función que genere el total de 
# las tablas de multiplicar dado un numero entero.
def generar_tabla(num1):
    for i in range(1, num1 + 1):
        print("-------------")
        for j in range(1, 11):
            print(f"{i}x{j}={i * j}")

generar_tabla(5)
