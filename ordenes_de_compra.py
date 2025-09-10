inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}
pedido = {}

while True:
    item = input("¿Qué item quiere?, resistor (R), capacitor (C), LED (L), transistor (T) (o 'continuar'): ").strip().upper()
    if item == "CONTINUAR":
        break

    if item == "R":
        item = "R001"
    elif item == "C":
        item = "C001"
    elif item == "L":
        item = "L001"
    elif item == "T":
        item = "T001"
    else:
        print("Item no válido.")
        continue

    cantidad = int(input(f"¿Cuántos {inventario[item]['nombre']} quiere? "))
    pedido[item] = cantidad
total = 0
def suma(pedido):
    total = 0
    for item, cantidad in pedido.items():
        total += cantidad * inventario[item]['precio']
    return total

print(f"Ha pedido {pedido}.")
print(f"El total de su pedido es: {suma(pedido)}")