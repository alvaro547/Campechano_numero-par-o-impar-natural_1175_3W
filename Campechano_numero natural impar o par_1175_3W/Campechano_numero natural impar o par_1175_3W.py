print(" ")
print("Alvaro Campechano 3W")
print(" ")
def main():
    """
    Función principal que solicita un número natural al usuario
    y verifica si es par o impar.
    """
    # Solicitar al usuario un número natural
    try:
        numero = int(input("Ingresa un número natural: "))
        
        # Verificar que el número sea natural
        if numero < 1:
            print("Por favor, ingresa un número natural válido (mayor o igual a 1).")
            return
        
        # Determinar si el número es par o impar
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")
    
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número natural.")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
