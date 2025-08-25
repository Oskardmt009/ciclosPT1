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
