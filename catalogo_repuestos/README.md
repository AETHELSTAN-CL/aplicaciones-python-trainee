- Este proyecto corresponde a un sistema básico de gestión de repuestos automotrices, desarrollado en Python, orientado al control de stock por marca.

Sistema:

1. Agregar repuesto
2. Buscar repuesto
3. Listar repuestos
4. Actualizar stock
5. Exportar datos a CSV
6. Salir

- Cada repuesto se representa mediante una estructura de diccionario con los siguientes campos:

Estructura
{
    "sku": "FILTRO-001",
    "nombre": "Filtro de aire",
    "marca": "Hyundai",
    "modelo": "Accent",
    "anio": 2015,
    "precio": 12900,
    "stock": 8
}

- Los repuestos se organizan en una estructura principal llamada base_repuestos, que es un diccionario donde la clave corresponde a la marca del vehículo y el valor es una lista de repuestos asociados a dicha marca. Conceptualmente, la estructura se organiza de la siguiente forma:

base_repuestos
│
├── "Hyundai"
│   ├── repuesto 1 (diccionario)
│   └── repuesto 2 (diccionario)
│
├── "Mazda"
│   └── repuesto 1
│
├── "Kia"
│   ├── repuesto 1
│   └── repuesto 2

Apuntes generales:
- La lógica de acceso a los datos sigue el siguiente principio:
 - Si la marca existe dentro del diccionario base_repuestos, el resultado es la lista de repuestos asociada a esa marca.
 - Si la marca no existe, el resultado es una lista vacía.

Dictionary List
repuestos = []

SI existe marca en la tabla:
    resultado = tabla[marca]
SI NO existe:
    resultado = []

Elemento           Significa
  marca             entrada
  base_repuestos     tabla
  []                 cero
  return             salida

