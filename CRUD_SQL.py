import pyodbc

# Configuración de conexión al servidor


def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=PRODUCCION;'
        'DATABASE=ABCAP_CENTRAL;'
        'UID=APLICACION;'
        'PWD=CARCUR.AA1;'
    )

# READ: Leer todos los empleados


def read_employees():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM BAS_Tratamientos"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(
            f"ID: {row.ID},"
            f"Codigo: {row.Codigo},"
            f"Nombre: {row.Nombre},"
            f"FlagActivo: {row.FlagActivo}"
        )
    conn.close()

# Menú de prueba


if __name__ == "__main__":
    print("Opciones:")
    print("1. Agregar empleado")
    print("2. Leer empleados")
    print("3. Actualizar empleado")
    print("4. Eliminar empleado")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 2:
        read_employees()
