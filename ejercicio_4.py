pedido = {}

while True:
    item = input("¿Qué item quiere? (o 'salir' para terminar): ")
    if item == "salir":
        break
    
    cantidad = int(input(f"¿Cuántos {item} quiere? "))
    pedido[item] = cantidad
    