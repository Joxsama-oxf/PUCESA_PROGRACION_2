#1. ¿Qué es la búsqueda lineal? ¿Cómo funciona?
"""La busqueda lineal es la forma de buscar un elemento que tengamos en una lista
de forma secuencial, es decir, que va buscando uno por uno hasta encontrar el elemento deseado
o llegar al final de la lista sin importar el orden (pd: no importa el orden).

funciona de forma que si encuentra el valor va a retornar el valor de la posicion, pero si no la
encuentra en esa posiciion va a seguir buscando hasta llegar al final de la lista"""
#2. ¿Qué es la búsqueda binaria? ¿Qué condición especial debe cumplir la lista?
"""La busqueda binaria es una forma diferente de buscar un elemento en una lista, pero esta
funciona partiendo en partes a la lista de mitad en mitad, pero tiene una particularidad, la cual es que la lista
debe estar ordenada. (pd: si es solo una lista con texto, no importa el orden, pero si es una lista con numeros)

¡¡SOLO FUNCIONA EN LISTAS ORDENADAS!!

"""
#3. ¿En qué casos conviene usar cada una?

"""La busqueda lineal es conveniente cuando no poseemos una lista ordenada y no tenemos una cantidad grande de datos

La busqueda binaria es conveniente cuando tenemos una lista ordenada y tenemos una gran cantidad de datos, ya que
al momento de partir en partes y no ir de uno en uno nos ahorra memoria"""
counter=0
counter2=0
while True:
   
   try:
      print("\n<----------    ✨ MENÚ ✨    ---------->")
      print("\n|<1>| Busqueda de libro (lineal) |<1>|")
      print("|<2>| Busqueda de libro (binaria) |<2>|")
      print("|<3>| Cuantas veces se uso cada busqueda  |<3>|")
      print("|<4>| SALIDA |<4>|")

      opcion = int(input("\n|| Selecciona una opción del menú ||--> "))
   except ValueError:
      print("\nError: Por favor, ingrese un número válido.")
      continue
   if opcion ==1:
         counter+=1
         def Busca_libros(lista, objetivo):
             #asignamos una funcion con el nombre de Busca_libros (y dentro el valor de lista y objetivo)
            for i in range(len(lista)): #Aqui buscamos dentro de la lista el rango con el cual va a ir guiandose el i
               if lista[i] == objetivo: #si encontra el valor se lo devolverta
                  return i #valor del objetivo
            return -1 #aqui va eliminando las opciones mediante la eliminacion de valor total de la lista "va recorriendo"

         Libros = ["cero", "uno", "dos", "tres", "cuatro",
                    "cinco", "seis", "siete", "ocho", "nueve", "diez",
                    "once", "doce", "trece", "catorce", "quince", "dieciséis",
                      "diecisiete", "dieciocho", "diecinueve", "veinte"
                      ] #lista con las Libros
         buscar = input("\n|| Ingrese el nombre del libro que desea buscar ||--> ").strip().lower() #interacción del usuario

         busqueda = Busca_libros(Libros, buscar) #buscamos en la funcion Busca_libros y le asignamos los valores los cuales van a tomar Busquedaicion de lista y objetivo 
         if busqueda != -1: #Es lo mismo que el return i
            print(f"\n'{buscar}' se encontró en la posición {busqueda}.")
         else:
            print(f"\n'{buscar}' El libro que buscas no se encuentra en la lista.") #Si no se encuentra el valor una vez que se acabe el -1 de la lista
      #Entonces nos dara la fruta que buscamos mas el mensaje de no se encuentra

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  
   elif opcion ==2:
      counter2+=1
      def busqueda_libros (lista, objetivo, contador=0): #asignamos una funcion con el nombre de busca_num (y dentro el valor de lista y objetivo)
         cont = 0
         inicio = 0
         final = len(lista) - 1 #Asignamos una variable llamada "final" con el índice del último elemento de la 'lista'.

         while inicio <= final:
            cont += 1
            medio = (inicio + final) // 2 #Calcula el elemento central de la parte actual de la lista
            if lista[medio] == objetivo: #Si el elemento central es igual al objetivo, se devuelve la posición del medio.
                  print(f"\nNúmero de iteraciones: {cont}")
                  return medio
            elif lista[medio] < objetivo: #Si el elemento central es menor que el objetivo,se busca en la mitad superior de la lista.
                  inicio = medio + 1 #aumenta el inicio al siguiente elemento
            else:
                  final = medio - 1 #Si el elemento central es mayor que el objetivo, se busca en la mitad inferior de la lista.
            contador += 1  
            print(f"Iteración {contador}: {lista[inicio:final+1]}")       
         return -1, contador

      Libros = ["cero", "uno", "dos", "tres", "cuatro",
                    "cinco", "seis", "siete", "ocho", "nueve", "diez",
                    "once", "doce", "trece", "catorce", "quince", "dieciséis",
                      "diecisiete", "dieciocho", "diecinueve", "veinte"
                      ]
      buscar = input("\nIngrese el libro a buscar: ").strip().lower() #interacción del usuario

      Busqueda = busqueda_libros (Libros, buscar) #asignamos una funcion con el nombre de busca_num (y dentro el valor de lista y objetivo)
      if Busqueda != -1:
         print(f"\n'{buscar}' se encontró en la posición {Busqueda}.")
      else:
         print(f"\n'{buscar}' El libro que buscas no se encuentra en la lista.") #Si no se encuentra el valor en la lista
      
   elif opcion ==3:
      
    print("La busqueda lineal se ha usado: ", counter, "veces")
    print("La busqueda binaria se ha usado: ", counter2, "veces")
   
       
      

   elif opcion ==4:
      print("\n\t||--< nos vemos >--||\n")
      break

   else:
      print("\nOpción no válida. Por favor, selecciona una opción del menú.")