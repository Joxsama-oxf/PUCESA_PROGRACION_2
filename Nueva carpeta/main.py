from thiss import insertion_sort_por_nombre, selection_sort_por_precio, busqueda_binaria_nombre, clientes

while True:
   
    try:
      print("\n<----------    ✨ MENÚ ✨    ---------->")
      print("\n|<1>| Ordenar por nombre la lista-tupla |<1>|")
      print("|<2>| Ordenar por precio la lista-tupla |<2>|")
      print("|<3>| Buscar nombre por busqueda binaria (que este primero ordenada) |<3>|")
      print("|<4>| Agregar cliente |<4>|")
      print("|<5>| SALIDA |<5>|")

      opcion = int(input("\n|| Selecciona una opción del menú ||--> "))
    except ValueError:
      print("\nError: Por favor, ingrese un número válido.")
      continue

    if opcion == 1:
        print("\nLista original:")
        for producto in clientes:
            print(producto)
        
        clientes_ordenados_por_nombre = insertion_sort_por_nombre(clientes.copy())
        print("\nLista ordenada por nombre:")
        for producto in clientes_ordenados_por_nombre:
            print(producto)

    elif opcion == 2:
        print("\nLista original:")
        for producto in clientes:
            print(producto)
        
        clientes_ordenados_por_precio = selection_sort_por_precio(clientes.copy())
        print("\nLista ordenada por precio:")
        for producto in clientes_ordenados_por_precio:
            print(producto)

    elif opcion == 3:
        objetivo = input("\n|| Ingrese el nombre del cliente que desea buscar ||--> ").strip()
        clientes_ordenados_por_nombre = insertion_sort_por_nombre(clientes.copy())
        indice, comparaciones = busqueda_binaria_nombre(clientes_ordenados_por_nombre, objetivo)
        
        if indice != -1:
            print(f"\n'{objetivo}' se encontró en la posición {indice} después de {comparaciones} comparaciones.")
        else:
            print(f"\n'{objetivo}' no se encuentra en la lista.")
    
    elif opcion == 4:
        nombre = input("\n|| Ingrese el nombre del cliente ||--> ").lower().strip()
        precio = float(input("|| Ingrese el precio del cliente ||--> "))
        clientes.append((nombre, precio))
        print(f"\nCliente '{nombre}' con precio {precio} agregado a la lista.")

    elif opcion == 5:
        print("\nTerminado hasta la proximaa")
        break