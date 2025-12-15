base_repuestos = {
    "Hyundai": [
        {
            "sku": "FILTRO-POLEN-001",
            "nombre": "Filtro de Polwn",
            "modelo": "Accent",
            "anio": 2015,
            "precio": 12900,
            "stock": 8
        },
        {
            "sku": "FILTRO-AIR-001",
            "nombre": "Filtro de aire",
            "modelo": "Accent",
            "anio": 2015,
            "precio": 12900,
            "stock": 8
        }
    ],
    "Mazda": [
        {
            "sku": "BUJIA-KIA-6",
            "nombre": "Bujía de encendido",
            "modelo": "6",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        }
    ],
    "Volkswagen": [
        {
            "sku": "BUJIA-VW",
            "nombre": "Bujía de encendido GENUINE PARTS",
            "modelo": "NIVUS",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        },
        {
            "sku": "BUJIA-NGK",
            "nombre": "Bujía de encendido NGK",
            "modelo": "NIVUS",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        }
    ],
    "Suzuki": [
        {
            "sku": "BUJIA-SUZUKI",
            "nombre": "Bujía Genuine Parts",
            "modelo": "SWIFT",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        },
        {
            "sku": "BUJIA-NGK",
            "nombre": "Bujía NGK",
            "modelo": "SWIFT",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        }
    ],
    "Kia": [
        {
            "sku": "BUJIA-KIA",
            "nombre": "Bujía BOSCH",
            "modelo": "Rio",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        },
        {
            "sku": "KIA-FILTRO-AIR",
            "nombre": "FILTRO DE AIRE GENUINE PARTS",
            "modelo": "Rio",
            "anio": 2019,
            "precio": 5900,
            "stock": 40
        }
    ]
}

# Estructura de funciones en Base de Datos

def listar_marcas(): 
    # función que obtiene todas las marcas disponibles en la base de datos

    return list(base_repuestos.keys()) # obtiene todas las claves del diccionario (las marcas)
    # list(x) convierte las claves en una lista manipulable
    # return entrega la lista de marcas al programa principal

def listar_repuestos_por_marca(marca):
    # función que obtiene la lista de repuestos asociados a una marca específica

    return base_repuestos.get(marca, [])
    # get(marca, []) busca la clave 'marca' dentro del diccionario base_repuestos
    # si la marca existe devuelve la lista de repuestos
    # si la marca NO existe devuelve una lista vacía []

def sumar_stock(marca, nombre_repuesto, cantidad): 
    for repuesto in base_repuestos.get(marca, []): #recorrer repuestos
        if repuesto["nombre"].lower() == nombre_repuesto.lower(): #comparar nombres (sin importar mayúsculas)
            stock_anterior = repuesto["stock"] #guardar stock anterior
            repuesto["stock"] += cantidad #sumar el stock
            return stock_anterior, repuesto["stock"] #devolver resultado útil - TUPLE
    return None, None #tuple - caja cerrada, valores ordenados. Ideal para devolver varios datos de una función.