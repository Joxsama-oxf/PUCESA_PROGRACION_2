
while True:

   try:
      print("\n<----------    ✨ MENÚ ✨    ---------->")
      print("\n||1|| 🍎 Busca frutas 🍓 ||1||")
      print("\n||2|| 🔍 Busca tu número 🔍 ||2||") 
      print
      print("\n||3|| 👋 SALIDA 👋 ||3||")

      opcion = int(input("\n|| Selecciona una opción del menú ||--> "))
   except ValueError:
      print("\nError: Por favor, ingrese un número válido.")
      continue
   if opcion ==1:
         def Busca_frutas(lista, objetivo): #asignamos una funcion con el nombre de Busca_frutas (y dentro el valor de lista y objetivo)
            for i in range(len(lista)): #Aqui buscamos dentro de la lista el rango con el cual va a ir guiandose el i
               if lista[i] == objetivo: #si encontra el valor se lo devolverta
                  return i #valor del objetivo
            return -1 #aqui va eliminando las opciones mediante la eliminacion de valor total de la lista "va recorriendo"

         frutas = ["manzana", "pera", "guanabana", "cambur", "patilla", "lechoza", "tamarindo", "durazno", "melocoton", "fresa"] #lista con las frutas
         buscar = input("\n|| Ingrese el nombre de la fruta que desea buscar ||--> ").lower() #interacción del usuario

         busqueda = Busca_frutas(frutas, buscar) #buscamos en la funcion Busca_frutas y le asignamos los valores los cuales van a tomar Busquedaicion de lista y objetivo 
         if busqueda != -1: #Es lo mismo que el return i
            print(f"\n'{buscar}' se encontró en la posición {busqueda}.")
         else:
            print(f"\n'{buscar}' no se encuentra en la lista.") #Si no se encuentra el valor una vez que se acabe el -1 de la lista
      #Entonces nos dara la fruta que buscamos mas el mensaje de no se encuentra

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  
   elif opcion ==2:
      def busqueda_num (lista, objetivo, contador=0): #asignamos una funcion con el nombre de busca_num (y dentro el valor de lista y objetivo)
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

      numeros = [10,20,30,40,50,60,70,80,90,100]
      buscar = int(input("\nIngrese el número a buscar: "))

      Busqueda = busqueda_num (numeros, buscar) #asignamos una funcion con el nombre de busca_num (y dentro el valor de lista y objetivo)
      if Busqueda != -1:
         print(f"\n'{buscar}' se encontró en la posición {Busqueda}.")
      else:
         print(f"\n'{buscar}' no se encuentra en la lista, solo numeros en intervalos de 10 en 10.") #Si no se encuentra el valor en la lista
      

   elif opcion ==3:
      print("\n\t||--< nos vemos >--||\n")
      break

   else:
      print("\nOpción no válida. Por favor, selecciona una opción del menú.")
