"""Simula un sistema de órdenes de compra para una tienda de componentes electrónicos."""
inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}
pedido = {}

while True:
    item = input("¿Qué item quiere?, resistor (R), capacitor (C), LED (L), transistor (T) (o factura'F'): ").strip().upper()
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

print(f"Ha pedido {pedido}.")
print(f"El total de su pedido es: ${suma(pedido)}")
