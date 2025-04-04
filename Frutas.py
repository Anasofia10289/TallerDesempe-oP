
frutas = []


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
        
        
        fruta = {
            "nombre": nombre,
            "precio": precio
        }
        
       
        frutas.append(fruta)

def ordenar_frutas():
    # Ordenar la lista de frutas por el precio en orden descendente
    frutas_ordenadas = sorted(frutas, key=lambda x: x['precio'], reverse=True)
    
    print("\nFrutas ordenadas por precio (de mayor a menor):")
    for fruta in frutas_ordenadas:
        print(f"Nombre: {fruta['nombre']} | Precio: {fruta['precio']}")

def main():
    ingresar_frutas()  # Ingresar las frutas
    ordenar_frutas()   # Ordenar y mostrar las frutas

main()
