"""for i in range(10):
    print(i)
"""

#___________________________________________________________________________________________________

"""
for i in range(1,10,2): #da saltos de 2 en 2
    print(i)"""
'''    
for i in range (1,10+1): #el 1 del principio es para que inicie desde alli 
    print(i)'''

#___________________________________________________________________________________________________

"""    
for i in range(0,5+1):
    print("tabla del",i)
    for j in range(1,10+1):
        print(i,"*",j,"=",i*j)
"""
#PD: se le da prioridad al segundo for 

#___________________________________________________________________________________________________

"""
for i in [0,1,2]:
    print("Emeneses", i)  #se imprimira emeneses 0,1,2 por que es el valor de la lista
"""

#___________________________________________________________________________________________________

"""
for i in [2,4,8]:
    print("El valor de" ,i, "y su cuadrado es", i**2)
"""

#___________________________________________________________________________________________________

"""
for i in ["Edison",20,"Ecuador","True"]:
    print("El valor de i es " ,i,)
"""

#___________________________________________________________________________________________________

"""
for i in [1,2,3,4,5]:
    print("tabla del",i)
    for j in [1,2,3,4,5]:
        print(i,"*",j,"=",i*j)
"""

#___________________________________________________________________________________________________

"""
par=[]
impar=[]

resto=[1,2,3,4,5,6,7,8,9,10]
for i in resto:

    if i%2==0:
        (f"el numero {i} es par")
        par.append(i)
    else:
        (f"el numero {i} es impar")
        impar.append(i)
        
print("los numeros pares son:",par)
print("los numeros impares son:",impar)
"""

#alternariva de imprimir los numeros pares e impares

#___________________________________________________________________________________________________

"""
for i in range(1,11):
    if i%2==0:
        print("el numero",i,"es par")
for j in range(1,11):
    if j%2!=0:
        print("el numero",j,"es impar")
"""

