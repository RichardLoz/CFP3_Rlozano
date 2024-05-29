#Crear la base de datos
import sqlite3

import sqlite3

# Conectar a la base de datos de SQlite
def conectar():
    conn = sqlite3.connect('usuarios.db')
    return conn

# Crear tabla de usuarios si no existe.
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS usuarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       usuario TEXT UNIQUE NOT NULL,
                       contraseña TEXT NOT NULL
                   )
                   ''')
    conn.commit()
    conn.close()

# Insertar usuarios en la base de datos:
def insertar_usuario(usuario, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)
                   ''', (usuario, contraseña))
    conn.commit()
    conn.close()

# Validar Usuario
def validar_usuario(usuario, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(''' 
                   SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?
                   ''', (usuario, contraseña))
    usuario_encontrado = cursor.fetchone()
    conn.close()
    return usuario_encontrado is not None

# Crear la tabla (Ejecuta la función crear_tabla)
crear_tabla()


insertar_usuario("Roberto","123456")

