# Lista para almacenar las frutas
frutas = []

# ingresar frutas
def ingresar_frutas():
    print("Ingreso de frutas:")
    for i in range(10):
        nombre = input(f"Ingrese el nombre de la fruta {i + 1}: ")
        while True:
            try:
                precio = float(input(f"Ingrese el precio de la fruta {i + 1}: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para el precio.")
        
        # Almacenar la fruta en un diccionario
        fruta = {
            "nombre": nombre,
            "precio": precio
        }
        
        # Añadir la fruta a la lista
        frutas.append(fruta)

# Función para ordenar las frutas por precio de mayor a menor
def ordenar_frutas():
    # Ordenar la lista de frutas por el precio en orden descendente
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio'], reverse=True)
    
    # Mostrar las frutas ordenadas
    print("\nFrutas ordenadas por precio (de mayor a menor):")
    for fruta in frutas_ordenadas:
        print(f"Nombre: {fruta['nombre']} | Precio: {fruta['precio']}")

# Función principal que ejecuta el programa
def main():
    ingresar_frutas()  # Ingresar las frutas
    ordenar_frutas()   # Ordenar y mostrar las frutas

# Ejecutar el programa
main()