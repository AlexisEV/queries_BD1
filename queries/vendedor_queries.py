from django.db import connection

def obtenerVendedor(vendedor_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM vendedor WHERE vendedor_id = %s", [vendedor_id])
        vendedor = cursor.fetchone()
    return vendedor

def registrarVendedor(usuario_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO vendedor (usuario_id) VALUES (%s)", [usuario_id])
    except Exception as e:
        print(f"Ocurrió un error al agregar el vendedor: {e}")