from tkinter import ttk
from tkinter import *

import backend

class Productos:
    def __init__(self,window):
        self.window = window
        self.window.title("Sistema de Stock")
        backend.inicializar_db()
        
        #Creación del contenedor
        frame = LabelFrame(self.window, text="Registrar nuevo producto")
        frame.grid(row=0, column=0, columnspan=6, pady=25)
        
        #Input para el nombre del producto
        Label(frame, text="Producto: ").grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)
        
        #Input para la categoria del producto
        Label(frame, text="Categoria: ").grid(row=2, column=0)
        self.categoria = Entry(frame)
        self.categoria.grid(row=2, column=1)
        
        #Input para el stock del producto
        Label(frame, text="Stock: ").grid(row=3, column=0)
        self.stock = Entry(frame)
        self.stock.grid(row=3, column=1)
        
        #Input para la descripcion del producto
        Label(frame, text="Descripción: ").grid(row=4, column=0)
        self.descripcion = Entry(frame)
        self.descripcion.grid(row=4, column=1)
        
        #Boton para agregar producto
        ttk.Button(frame, text="Guardar Producto").grid(row=5, columnspan=2, sticky=W + E)
        
        #Mensaje de confirmación
        self.mensaje = Label(text="", fg="red")
        self.mensaje.grid(row=6, column=0, columnspan=4, sticky=W + E)
        
        #Tabla para mostrar los productos
        self.tree = ttk.Treeview(height=10, columns=("Categoria", "Stock", "Descripcion"))
        self.tree.grid(row=5, column=0)
        self.tree.heading('#0', text="Producto", anchor=CENTER)
        self.tree.heading('Categoria', text="Categoría", anchor=CENTER)
        self.tree.heading('Stock', text="Stock", anchor=CENTER)
        self.tree.heading('Descripcion', text="Descripcion", anchor=CENTER)
        
        # Ancho de columnas
        self.tree.column('#0', width=100)
        self.tree.column('Categoria', width=100)
        self.tree.column('Stock', width=100)
        self.tree.column('Descripcion', width=150)
        
        #Botones para eliminar y editar productos
        ttk.Button(text="ELIMINAR").grid(row=8, column=0, columnspan=1, sticky= W + E)
        ttk.Button(text="EDITAR").grid(row=9, column=0, columnspan=1, sticky= W + E)
        
        # Llenar la tabla de productos existentes
        #self.obtener_productos()
if __name__ == '__main__':
    window = Tk()
    aplicacion = Productos(window)
    window.mainloop()