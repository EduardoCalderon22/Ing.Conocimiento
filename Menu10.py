from time import sleep 
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Ejercicio 1")
    print ("2. Ejercicio 2")
    print ("3. Ejercicio 3")
    print ("4. Ejercicio 4")
    print ("5. Ejercicio 5")
    print ("6. Ejercicio 6")
    print ("7. Ejercicio 7")
    print ("8. Ejercicio 8")
    print ("9. Ejercicio 9")
    print ("10. Ejercicio 10")
    print ("11. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Si un cierto tipo de tapete se vende a $9 por yarda cuadrada. Cual es su precio por metro cuadrado?")
        yarda = 0.914**2 
        total1 = (9/yarda)
        print("El precio por metro cuadrado es: $",total1)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 2:
        print ("La velocidad de luz es 2.99776X10 m/seg. Calcular el numero de metros en un año-luz.")
        opm = (2.99*10**8)*(3.20*10**7)
        print("El numero de metros serian: ",opm," metros")
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 3:
        print("La densidad media de la tierra es 5.522 g/cm. Determinar la masa de la tierra en gramos.")
        gxgramos = (5.522)*(1*10**6)
        print("Los gramos totales seria: ",gxgramos,"g/m^3")
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 4:
        print("Nancy presentó 4 pruebas finales, siendo sus calificaciones 9.5, 6.8, 9.2 y 9.1. Hacer un algoritmo para calcular e imprimir el promedio de Nancy")
        c1 = 9.5
        c2 = 6.8
        c3 = 9.2
        c4 = 9.1
        promediofinal = (c1+c2+c3+c4)/4
        print ("El promedio final de Nancy es: ",promediofinal)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 5:
        print("Escribir un programa que convierta los pesos de los miembros del equipo de futbol escolar de libras a kilogramos.")
        lbs = float(input("Ingrese el peso en libras: "))
        kg = lbs / 2.204
        print("El peso en kg es: ",kg)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 6:
        print("El Mariner 9 empleo 167 dias para ir de la Tierra a Marte, qeu se encuentra a una distancia de 34900000 millas, aproximadamente. Expresar esta distancia en km. Cual fue su velocidad promedio en km/h?")
        millasxkm = 34900000 * 1.609
        diaxhora = 167 * 24 
        velocidadkmh = millasxkm/diaxhora
        print ("La distancia recorrida en km es: ",millasxkm)
        print ("La velocidad promedio fue km/h: ",velocidadkmh)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 7:
        print("En Miami, Florida, Lulu Rocket se presenta en varios actos sociales como Senorita Metrica. Su estadistica vital es 89-58-89 cm. Mide 170 cm y pesa 53 kg. Imprimir sus medidas en pulgadas, su estatura en pies y pulgadas, y su peso en libras.")
        medidasxpulgadas= 89/2.54
        medidasxpulgadas2 = 58/2.54
        alturaxpies = 1.70*3.281
        pesoxlibras = 53*2.205
        print ("Sus medidas en pulgadas es: ",medidasxpulgadas,"-",medidasxpulgadas2,"-",medidasxpulgadas)
        print ("Sus altura en pies es: ",alturaxpies)
        print ("Sus peso en libras es: ",pesoxlibras)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 8:
        print("Calcular e imprimir el numero de segundos que hay en una semana, en tres semanas, en un mes y tres dias.")
        segundoxsemana = 604800
        segundox3semana = 3 * 604800
        segundoxmes = 2628000
        segundox3dias = 3 * 86400
        print("La cantidad de segundos que hay en una semana es: ",segundoxsemana)
        print("La cantidad de segundos que hay en tres semanas es: ",segundox3semana)
        print("La cantidad de segundos que hay en un mes es: ",segundoxmes)
        print("La cantidad de segundos que hay en tres dias es: ",segundox3dias)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 9:
        print("Calcular e imprimir el numero de segundos en D dias, H horas, M minutos y S segundos. Por ejemplo en 4 dias, 6 horas, 24 minutos y 11 segundos hay 368651 segundos")
        dia = int(input("Ingrese el numero de dias: "))
        horas = int(input("Ingrese el numero de horas: "))
        minutos = int(input("Ingrese el numero de minutos: "))
        segundos = int(input("Ingrese el numero de segundos: "))
        totalsumas = (dia*86400)+(horas*3600)+(minutos*60)+(segundos)
        print("La cantidad de segundos serian: ",totalsumas)
        print("Regresando al menu")
        sleep(5) 
    elif opcion == 10:
        print("Leer N y una lista de N numeros. Imprimirlos en orden de magnitud creciente.")
        numeros=list(eval(input("Ingrese 5 numeros separados por comas: ")))
        numeros.sort()
        for n10 in numeros:
            print (n10)
        print("Regresando al menu")
        sleep(5)
    elif opcion == 11:
        salir = True
    else:
        print ("Introduce un numero valido")
 
print ("Fin")
    