componentes = ["Resistor", "Capacitor", "LED", "Transistor"]
cantidades = [100, 50, 25, 30]

inv = input("cantidad de resistores (R) cantidad de capacitores (C) cantidad de LED (L) cantidad de transistores (T)").lower()
# Mostrar inventario
if inv == "r":
    print("Cantidad de resistores:", cantidades[0])
elif inv == "c":
    print("Cantidad de capacitores:", cantidades[1])
elif inv == "l":
    print("Cantidad de LED:", cantidades[2])
elif inv == "t":
    print("Cantidad de transistores:", cantidades[3])
else:
    print("Componente no encontrado.")