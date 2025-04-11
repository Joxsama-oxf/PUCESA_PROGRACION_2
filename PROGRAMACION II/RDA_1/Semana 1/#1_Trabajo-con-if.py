#Menu de opciones
#1 sumar
#2 restar
#3 multiplicar
#4 dividir
#5 seleccionar opciones
#6 ingrsar por teclado 2 numeros verifique el tipo de dato
#7 validar que el segundo numero no sea cero
#8 realizar la operacion seleccionada
#9 mostrar el resultado
#10 validar que la opcion seleccionada sea correcta
#11 mostrar un mensaje de error si la opcion no es correcta
#12 salir del programa




separator0="__________________________________________________________"
separator1="----------------------------------------------------------"
separator2="=========================================================="

print(separator0)
print("MENU DE OPCIONES")
print(separator1)  
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
print(separator1)

#_____________________________________________________________________________________________

Operacion=int(input("Seleccione la operacion a realizar: "))
if Operacion<1 or Operacion>5:
    print("||ERROR|| La opcion seleccionada no es correcta")
    print(separator0)
    print("Por favor seleccione una de las opciones del menu")
print(separator0)

#_____________________________________________________________________________________________

Numero1=float(input(f"Ingrese el primer numero : "))
Numero2=float(input(f"Ingrese el segundo numero : "))
tipo1=print(f"El numero {Numero1} es de tipo",type(Numero1))
tipo2=print(f"El numero {Numero2} es de tipo",type(Numero2))
print(separator0)

#_____________________________________________________________________________________________
if tipo2==0 and Operacion ==4:
    print("No se puede dividir entre cero")
    print(separator0)

elif Operacion==1:
    print("La suma es:",Numero1+Numero2)
elif Operacion==2:
    print("La resta es:",Numero1-Numero2)
elif Operacion==3:
    print("La multiplicacion es:",Numero1*Numero2)
elif Operacion==4:
    print("La division es:",Numero1/Numero2)
elif Operacion==5:
    print("Saliendo del programa...")


#_____________________________________________________________________________________________