from modules.base_datos import (
    listar_marcas,
    listar_repuestos_por_marca,
    sumar_stock
)
import csv
from datetime import datetime

# =========================
# INGRESO OPERARIO
# =========================
operario = input("Ingrese su ID de Bodega\n- ") # cualquier valor (testear sistema)

print(f"\nHola {operario} \nBienvenido al Sistema de \nGestión de Repuestos\n")


# =========================
# SELECCIÓN DE MARCA
# =========================
marcas = listar_marcas()

# Diccionario para números escritos
numeros_texto = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10
}

while True:
    print("- Seleccione por número o nombre de marca. \n (Ejemplo: 1, Hyundai, tres.) \n\nMarcas disponibles:")
    for i, marca in enumerate(marcas, 1):
        print(f"{i}. {marca}")

    entrada = input("\n\nEscriba aquí su selección: ").strip().lower() #strip #elimina espacios en blanco
    print("\n" + "=" * 50)

    marca_seleccionada = None

    # número (ej: 1)
    if entrada.isdigit():
        idx = int(entrada)
        if 1 <= idx <= len(marcas):
            marca_seleccionada = marcas[idx - 1]

    # número escrito (ej: "uno")
    elif entrada in numeros_texto:
        idx = numeros_texto[entrada]
        if 1 <= idx <= len(marcas):  #lend() # Length #Largo o Cantidad total
            marca_seleccionada = marcas[idx - 1]

    # nombre de marca (ej: "mazda")
    else:
        for marca in marcas:
            if marca.lower() == entrada:
                marca_seleccionada = marca
                break

    # salida del bucle
    if marca_seleccionada is not None:
        break

    print("\nSelección inválida. Intente nuevamente.")

print(f"\nRegistro para marca: {marca_seleccionada}")
print("\n" + "-" * 50)

# =========================
# REPUESTOS DE LA MARCA
# =========================
repuestos = listar_repuestos_por_marca(marca_seleccionada)

if repuestos:
    print("\nRepuestos existentes:\n")
    for i, r in enumerate(repuestos, 1): # recorre lista repuestos, entregame un número (i) y el repuesto (r)
        print(f"{i}. {r['nombre']} ({r['modelo']}) | Stock: {r['stock']}")
else:
    print("\nNo hay repuestos registrados para esta marca.")

# =========================
# SUMAR STOCK
# =========================
while True:
    entrada_repuesto = input("\nIngrese N° del repuesto para sumar a stock: ").strip()

    if not entrada_repuesto.isdigit():
        print("\n" + "=" * 50)
        print("\nError: Ingrese un número válido según la lista")
        print("\n" + "=" * 50)

        print("\nRepuestos disponibles:\n")
        for i, r in enumerate(repuestos, 1):
            print(f"{i}. {r['nombre']} ({r['modelo']}) | Stock: {r['stock']}")
        continue

    opcion_repuesto = int(entrada_repuesto)

    if opcion_repuesto < 1 or opcion_repuesto > len(repuestos):
        print("\n" + "=" * 50)
        print("\nError: Selección fuera de rango")
        print("\n" + "=" * 50)

        print("\nRepuestos disponibles:\n")
        for i, r in enumerate(repuestos, 1):
            print(f"{i}. {r['nombre']} ({r['modelo']}) | Stock: {r['stock']}")
        continue

    # selección válida
    repuesto_seleccionado = repuestos[opcion_repuesto - 1]
    nombre_repuesto = repuesto_seleccionado["nombre"]
    break


# =========================
# VALIDACIÓN DE CANTIDAD
# =========================
while True:
    cantidad_input = input("\nCantidad a agregar: ").strip()

    # Convertir a entero
    try:
        cantidad = int(cantidad_input)
        if cantidad <= 0:
            print("\nError: la cantidad debe ser un número entero positivo")
            print("=" * 50)
            continue  # vuelve a pedir cantidad
        break  # todo ok, salir del bucle
    except ValueError:
        print("\nError: la cantidad debe ser un número entero")
        print("=" * 50)
        continue  # vuelve a pedir cantidad

# Una vez válido, se suma al stock
stock_anterior, stock_actual = sumar_stock(
    marca_seleccionada,
    nombre_repuesto,
    cantidad
)
# =========================
# RESULTADO FINAL + CSV
# =========================
if stock_anterior is not None:
    print("\n!LISTO! \nACTUALIZACIÓN DE STOCK")
    print(f"Marca              : {marca_seleccionada}")
    print(f"Repuesto           : {nombre_repuesto}")
    print(f"Cantidad agregada  : +{cantidad}")
    print(f"Stock anterior     : {stock_anterior}")
    print(f"Stock nuevo        : {stock_actual}")

    # Guardar en CSV
    with open("data/repuestos_entradas.csv", mode="a", newline="", encoding="utf-8") as archivo: #abrir archivo # "a" append #newline evitar líneas en blanco
        writer = csv.writer(archivo) # writer sabe cómo escribir columnas separadas por coma

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([
            fecha,
            operario,
            marca_seleccionada,
            nombre_repuesto,
            cantidad,
            stock_anterior,
            stock_actual
        ])

    print("\nRegistro guardado en repuestos_entradas.csv \nSistema Terminado.")

else:
    print("\nRepuesto no encontrado")