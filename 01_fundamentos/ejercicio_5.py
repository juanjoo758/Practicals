"""sistema para controlar el stock de una tienda de componentes electrónicos."""

inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}
pedido = {}  # Diccionario para almacenar el pedido del cliente


user = input("¿qué desea hacer? (ver stock 'S', hacer pedido 'P'): ").strip().upper()

item = ""

def hacer_automatico(item_automatico): 
    if item_automatico:  # Si se pasó un item automático
          while True:
            try:
                cantidad = int(input(f"¿Cuántos {inventario[item_automatico]['nombre']} quiere para reposición? "))
                total = cantidad * inventario[item_automatico]['precio']
                return total
            except ValueError:
                print("Cantidad inválida.")
    return total
   

def hacer_pedido():
   
    while True:
        item = input("¿Qué item quiere?, resistor (R), capacitor (C), LED (L), transistor (T) (o factura 'F'): ").strip().upper()
        if item == "F":
            break

        if item == "R":
            codigo_item = "R001"
        elif item == "C":
            codigo_item = "C001"
        elif item == "L":
            codigo_item = "L001"
        elif item == "T":
            codigo_item = "T001"
        else:
            print("Item no válido.")
            continue

        try:
            cantidad = int(input(f"¿Cuántos {inventario[codigo_item]['nombre']} quiere? "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        if cantidad > inventario[codigo_item]['cantidad']:
            print(f"No hay suficiente stock de {inventario[codigo_item]['nombre']}. Stock disponible: {inventario[codigo_item]['cantidad']}")
            pedido[codigo_item] = inventario[codigo_item]['cantidad']
        else:
            pedido[codigo_item] = cantidad

    def suma(pedido_dict):
        total = 0
        for item, cantidad in pedido_dict.items():
            total += cantidad * inventario[item]['precio']
        return total
    return pedido

if user == "S":
    print("Stock disponible:")
    for codigo, item in inventario.items():
        print(f"{item['nombre']} (Código: {codigo}) - Cantidad: {item['cantidad']} - Precio: ${item['precio']}")
        if item['cantidad'] < 100:
            AC = input(f"¿Desea hacer un pedido de reposición? de {item['nombre']} (S/N): ").strip().upper()
            if AC == "S":
                total_item = hacer_automatico(codigo) 
                continue
                
            elif AC == "N":
                continue
            else:
                print("Opción no válida.")
                break
        

elif user == "P":
    pedido = hacer_pedido()
    

    
else: 
    print("Opción no válida.")

    if item in inventario:
        print(f"Ha pedido {pedido}.")
    print(f"El total de su pedido es: ${suma(pedido)}")
    print("Gracias por su compra.")

print("El total de su pedido es: $", total_item)
