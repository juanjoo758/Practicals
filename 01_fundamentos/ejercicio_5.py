"""sistema para controlar el stock de una tienda de componentes electrónicos."""

inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}
pedido = {}  # Diccionario para almacenar el pedido del cliente

user = input("¿qué desea hacer? (ver stock 'S', hacer pedido 'P'): ").strip().upper()
