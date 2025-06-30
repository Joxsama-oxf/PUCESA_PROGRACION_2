#Ejercicio de palandromos
#contador


"""def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    
    # Comparar la palabra con su reverso
    return palabra == palabra[::-1]


palabra = input("Ingrese una palabra o frase: ")    
if palindromo(palabra):
    print(f"La palabra o frase '{palabra}' es un palíndromo.")
    print("contador:", count)
else:
    print(f"La palabra o frase '{palabra}' no es un palíndromo.")
    print("contador:", count)
"""
    
cont = 0

def palindromo_recursivo(palabra):
    global cont
    palabra = palabra.lower().replace(" ", "")

    if len(palabra) <= 1:    
        cont += 1
        return True, cont
    elif palabra[0] != palabra[-1]:
        
        cont += 1
        return False, cont
    else:
        return palindromo_recursivo(palabra[1:-1])

usuario = input("Ingrese una palabra o frase: ")

if palindromo_recursivo(usuario):
    print(f"La palabra o frase '{usuario}' es un palíndromo.")
else:
    print(f"La palabra o frase '{usuario}' no es un palíndromo.")

print("contador:", cont)