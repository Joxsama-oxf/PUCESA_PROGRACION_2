Separator1 = "-------------------------------------------------------------------------------------------------------------------------------------------------"
separator2 = "||---------------------------------------------------------------------------------------------------------------------------------------------||"

Titulo=[]
Autor=[]
Año=[]



def presentacion():
    print(separator2)
    print("Nombre: Alejandro Sutherland")
    print("Fecha: 11/04/2025")
    print("Clase Programacion Orientada a Objetos")
    print(separator2)
    
presentacion()   

def Menu():
    print(separator2)
    print("Crear una clase libro")
    print("1. Titulo")
    print("2. Autor")
    print("3. Año")
    print("4. Datos del libro")
    print("5. salir")
    print(separator2)
    
while True:
    
    Menu()
    Opcion = int(input("Ingrese una opcion: "))
    while Opcion <1 or Opcion >5:
        print("Opcion invalida. Intente nuevamente.")
        Opcion = int(input("Ingrese una opcion: "))
    
    if Opcion == 1:
            titulo = input("Ingrese el titulo del libro: ")
            Titulo.append(titulo)
            
    elif Opcion == 2:
            autor = input("Ingrese el autor del libro: ")
            Autor.append(autor)
            
    elif Opcion == 3:
            año = input("Ingrese el año del libro: ")
            Año.append(año)
            
    elif Opcion == 4:
            if len(Titulo) > 0 and len(Autor) > 0 and len(Año) > 0:
                print("Datos del libro: ")
                for i in range(len(Titulo)):
                    print("Titulo:", Titulo[i])
                    print("Autor:", Autor[i])
                    print("Año:", Año[i])
            else:
                print("No hay datos del libro registrados.")
    
    
    elif Opcion == 5:
            print("Saliendo del programa.")
            break