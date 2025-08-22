//1. Algoritmo para imprimir números del 1 al 10

for (let i = 1; i<=10; i++)
{
    console.log(i);
}

//2. Algoritmo para sumar los primeros 10 números

let sum = 0;
for (let i = 1; i<=10; i++)
{
    sum += i
}
console.log(sum)

//3. Algoritmo para generar la tabla de un numero dado por argumento en una función

//Algoritmo para generar una tabla tipo función

function tablaMultiplicar(num)
{
    for(let i = 1; i<=10; i++)
    {
        console.log(num + " x "+ i + " = "+num*i)
    }
}
tablaMultiplicar(7)

//4. Algoritmo para contar ocurrencias de 'a' en un texto

function cuentaA(word)
{
    let cont = 0;
    for (let i = 0; i<word.length; i++)
    {

    if(word[i].toLowerCase() == "a")
    {
        cont++
    }
}
console.log(cont)
}

cuentaA("matematicas")

//5. Algoritmo para calcular el factorial de un número

function factorial(fact)
{
    let mult = 1;
    for(let i = 1; i<=fact; i++)
    {
        mult = mult*i
    }
    console.log(mult)
}

factorial(5)

//6. Escribe una función que reciba un array de números y devuelva un nuevo array que contenga solo los números pares.

function pairs(numP)
{
    for (let i = 0; i<=numP; i++)
    {
        console.log(numP[i])
    }
    const numPares = []

    for (let i=0; i<numP.length; i++)
    {
        if(numP[i]%2==0)
        {
            numPares.push(numP[i]);
        }
    }
    console.log(numPares)    
}
numP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs(numP)

//7. Implementa una función que calcule la suma de los cuadrados de los primeros N números naturales.

function sumaPotencia(pot)
{
    
    let suma = 0;
    for(let i = 0; i<=pot; i++)
    {
        suma = suma + Math.pow(i,2)
    }
    console.log(suma)
}

sumaPotencia(10)

//8. Escribe una función que calcule la potencia de un número (base^exponente) utilizando un ciclo for, sin usar el operador de potencia **.

function potencia(base, exp)
{    
    res = 1;
    for(let i = 1; i<=exp; i++)
    {
        res = res*base
    }
    console.log(res)
    
}
potencia (2,6)
//9. Desarrolla una función que genere y devuelva los primeros N términos de la serie de Fibonacci.

function Fibonacci(num3)
{
    let cont1=0;
    let cont2=1;
    let serie=0;
    for (let i=0; i<num3; i++)
    {
        console.log(cont1)
        serie = cont1+cont2;
        cont1=cont2;
        cont2=serie;        
    }    
}
Fibonacci(4)


//10. Desarrolla una función que genere el total de las tablas de multiplicar dado un numero entero.
function generarTabla(num1)
{
    for(let i = 1; i<=num1; i++)
    {
        for(let j = 1; j<=10; j++)
        {
            console.log(i+"x"+j+"="+i*j)
        }
    }
}
generarTabla(5)