import sqlite3
#TODO: LOGICA DB

db_nombre = 'base_datos.db'

def run_query(query, parameters=()):
    with sqlite3.connect(db_nombre) as conn:
        cursor = conn.cursor()
        resultado = cursor.execute(query, parameters)
        conn.commit()
    return resultado

def inicializar_db():
    query = '''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        stock INTEGER NOT NULL,
        descripcion TEXT
    )
    '''
    run_query(query)


def obtener_productos():
    query = 'SELECT * FROM productos ORDER BY nombre DESC'
    db_rows = run_query(query)
    return db_rows

def agregar_producto(nombre, categoria, stock, descripcion):
    query = 'INSERT INTO productos VALUES (NULL,?,?,?,?)'
    parameters = (nombre, categoria, stock, descripcion)
    run_query(query, parameters)

def eliminar_producto(nombre):
    query = 'DELETE FROM productos WHERE nombre = ?'
    run_query(query,(nombre,))

def actualizar_producto(nombre_nuevo, nombre, stock_nuevo, stock_viejo):
    query = 'UPDATE productos set nombre = ?, stock = ?, where nombre = ? and stock = ?'
    parameters = (nombre_nuevo, stock_nuevo, nombre, stock_viejo)
    run_query(query, parameters)
    
    
    
    