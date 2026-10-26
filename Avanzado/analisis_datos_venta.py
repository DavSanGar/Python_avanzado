'''Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el
monto de la venta y la ubicación del comprador. Realiza un análisis avanzado
de estas ventas.
1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda.
A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada: - Registro de ventas (json,dic,etc)
Salida: Ubicaciones por promedio, ej. : [Chile, Ecuador]
'''



from datetime import datetime
#Función principal
def analizar_ventas(ventas):
    
    #1. Filtrar último trimestre de ventas
    ventas_filtradas = [venta for venta in ventas if datetime.strptime(venta["fecha_venta"], "%Y-%m-%d").month>=10]

    #2. Seleccionamos sólo las ventas mayores a $500
    ventas_filtradas = [venta for venta in ventas_filtradas if venta["monto"]>500]

    #3. Agrupar ventas por ubicacion del comprador
    ventas_agrupadas = {}

    for venta in ventas_filtradas:
        ubicacion = venta["ubicacion"]
        if ubicacion not in ventas_agrupadas:
            ventas_agrupadas[ubicacion]= []
        ventas_agrupadas[ubicacion].append(venta)
    print(ventas_agrupadas)

ventas = [
    {"nombre_producto": "Smartphone X200", "fecha_venta": "2025-10-01", "monto": 599.99, "ubicacion": "Madrid"},
    {"nombre_producto": "Portátil Pro 15", "fecha_venta": "2025-10-03", "monto": 499.50, "ubicacion": "Barcelona"},
    {"nombre_producto": "Tablet Z10", "fecha_venta": "2025-11-05", "monto": 899.00, "ubicacion": "Madrid"},
    {"nombre_producto": "Auriculares Inalámbricos S", "fecha_venta": "2025-11-07", "monto": 199.99, "ubicacion": "Sevilla"},
    {"nombre_producto": "Monitor UltraWide 34", "fecha_venta": "2025-10-09", "monto": 799.99, "ubicacion": "Madrid"},
    {"nombre_producto": "Cámara 4K Pro", "fecha_venta": "2025-12-11", "monto": 1199.00, "ubicacion": "Granada"},
    {"nombre_producto": "Smartwatch Fit 3", "fecha_venta": "2025-11-13", "monto": 249.99, "ubicacion": "Zaragoza"},
    {"nombre_producto": "Teclado Mecánico RGB", "fecha_venta": "2025-12-15", "monto": 149.00, "ubicacion": "Málaga"},
    {"nombre_producto": "Disco Duro SSD 1TB", "fecha_venta": "2025-11-17", "monto": 679.99, "ubicacion": "Madrid"},
    {"nombre_producto": "Router WiFi 6 Pro", "fecha_venta": "2025-10-19", "monto": 999.99, "ubicacion": "Barcelona"}
]

analizar_ventas(ventas)