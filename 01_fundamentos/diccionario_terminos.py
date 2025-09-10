inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}

# buscar un componente por su código

el = input("Ingrese el código del componente (R001, C001, L001, T001): ").upper()
if el in inventario:
    componente = inventario[el]
    print(f"Nombre: {componente['nombre']}")
    print(f"Cantidad: {componente['cantidad']}")
    print(f"Precio: ${componente['precio']:.2f}")
else:
    print("Componente no encontrado.")

# mostrar todo el inventario
for i in inventario:
    print(f"{inventario[i]}: {inventario[i]}")

