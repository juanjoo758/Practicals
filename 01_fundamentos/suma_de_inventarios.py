resistor_precio = 0.05
resistor_cantidad = int(input("Ingrese la cantidad de resistores: "))
capacitor_precio = 0.12
capacitor_cantidad = int(input("Ingrese la cantidad de capacitores: "))
#calcular precio 

total_inventario = (resistor_precio * resistor_cantidad) + (capacitor_precio * capacitor_cantidad)
print("El total es:", total_inventario)