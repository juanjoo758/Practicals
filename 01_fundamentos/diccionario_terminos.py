inventario = {
    "R001": {"nombre": "Resistor 1kΩ", "cantidad": 100, "precio": 0.05},
    "C001": {"nombre": "Capacitor 100µF", "cantidad": 50, "precio": 0.12},
    "L001": {"nombre": "LED Rojo", "cantidad": 25, "precio": 0.15},
    "T001": {"nombre": "Transistor 2N2222", "cantidad": 30, "precio": 0.25}}

#escoge si quiere o no todo 

v = input ("¿Desea ver todo el inventario? (s/n): ").lower()
if v == "s":
    for i in inventario:
        print(f"{i}: {inventario[i]}")
elif v == "n":

 # buscar un componente por su código y dice todo sobre él

 el = input("Ingrese el código del componente (R001, C001, L001, T001): ").upper()

 # si quiere conocer algo especifico

dato = input("¿Qué dato desea conocer? nombre (n), cantidad (c), precio (p), todos (t): ").lower()
if dato == "n":
    dato = "nombre"
elif dato == "c":
    dato = "cantidad"
elif dato == "p":
    dato = "precio"
elif dato == "t":
    dato = "todos"
else:
    print("Dato no válido.")

if dato == "nombre":
    print("Nombre:", inventario[el]["nombre"])
elif dato == "cantidad":
    print("Cantidad:", inventario[el]["cantidad"])
elif dato == "precio":
    print("Precio:", inventario[el]["precio"])
elif dato == "todos" and el in inventario:
    componente = inventario[el]
    print(f"Nombre: {componente['nombre']}")
    print(f"Cantidad: {componente['cantidad']}")
    print(f"Precio: ${componente['precio']:.2f}")
else:
    print("Componente no encontrado.")



