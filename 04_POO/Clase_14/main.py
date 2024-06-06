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
        ttk.Button(frame, text="Guardar Producto", command=self.agregar_producto).grid(row=5, columnspan=2, sticky=W + E)
        
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
        ttk.Button(text="ELIMINAR", command=self.eliminar_productos).grid(row=8, column=0, columnspan=1, sticky= W + E)
        ttk.Button(text="EDITAR", command=self.editar_productos).grid(row=9, column=0, columnspan=1, sticky= W + E)
        
        # Llenar la tabla de productos existentes
        self.obtener_productos()
        
        #Metodo que agregar productos
    def agregar_producto(self):
        from backend import agregar_producto
        if self.validar_datos():
            agregar_producto(self.nombre.get(), self.categoria.get(), self.stock.get(), self.descripcion.get())
            self.mensaje['text'] = 'Producto {} agregago correctamente'.format(self.nombre.get())
            
            #Limpiar los campos de entrada
            #DELETE(I,F)
            self.nombre.delete(0, END)
            self.categoria.delete(0, END)
            self.stock.delete(0, END)
            self.descripcion.delete(0, END)
        else:
            self.mensaje['text'] = 'Todos los campos son requeridos'
        self.obtener_productos()
    
    #Validar que los datos no esten vacios.
    def validar_datos(self):
        return len(self.nombre.get()) != 0 and len(self.stock.get()) != 0 and len(self.categoria.get())!= 0  
        
    def obtener_productos(self):
        from backend import obtener_productos
        #Obtener todas las filas actuales de mi tabla
        grabados = self.tree.get_children() 
        for elemento in grabados:
            self.tree.delete(elemento)
        
        #Consulto los datos
        #LLamar a la funcion obtener_productos para obtener los productos de la DB
        productos = obtener_productos()
        for row in productos:
            self.tree.insert('',0, text=row[1],values=(row[2],row[3],row[4]))
            
    def eliminar_productos(self):
        from backend import eliminar_producto, obtener_productos
        self.mensaje['text'] = ''
        
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Debe seleccionar un producto'
            return
        
        nombre = self.tree.item(self.tree.selection())['text']
        eliminar_producto(nombre)
        self.mensaje['text'] = 'Producto {} eliminado correctamente'.format(nombre)
        self.obtener_productos()
        
    def editar_productos(self):
        self.mensaje['text'] = ''
        
        try:
            self.tree.item(self.tree.selection())['text'][0]
        
        except Exception as e:
            self.mensaje['text'] = "Debe seleccionar un producto"
            return
        #Obtener el nombre del producto
        nombre = self.tree.item(self.tree.selection())['text']
        stock_viejo = self.tree.item(self.tree.selection())['values'][1]
        #Crear una nueva ventana para editar el producto
        self.ventana_editar = Toplevel()
        self.ventana_editar.title = 'Editar Producto'
        
        #Etiqueta y campo de entrada para mostrar el nombre actual
        Label(self.ventana_editar, text='Nombre Actual: ').grid(row=0, column=1)
        Entry(self.ventana_editar, textvariable = StringVar(self.ventana_editar, value=nombre), state='readonly').grid(row=0, column=2)
        
        #Etiqueta y campo para el nuevo nombre:
        Label(self.ventana_editar,text='Nombre Nuevo: ').grid(row=1, column=1)
        nombre_nuevo = Entry(self.ventana_editar)
        nombre_nuevo.grid(row=1, column=2)
        
        #Etiqueta y campo de entrada para mostrar el stock actual
        Label(self.ventana_editar, text='Stock Actual: ').grid(row=2, column=1)
        Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=stock_viejo), state='readonly'
        ).grid(row=2, column=2)
        
        #Etiqueta y campo de entrada para el nuevo stock
        Label(self.ventana_editar, text='Stock Nuevo: ').grid(row=3, column=1) 
        stock_nuevo = Entry(self.ventana_editar)
        stock_nuevo.grid(row=3, column=2)
        
        #Boton para actualizar el producto con los nuevos valores
        Button(self.ventana_editar, text="Actualizar", command=lambda:self.actualizar_productos(nombre_nuevo.get(), nombre, stock_nuevo.get(), stock_viejo)).grid(row=4, column=2, sticky=W)
            
        
    def actualizar_productos(self, nombre_nuevo,nombre,stock_nuevo,stock_viejo):
        from backend import actualizar_producto, obtener_productos
        actualizar_producto(nombre_nuevo,nombre,stock_nuevo,stock_viejo)
        self.ventana_editar.destroy()
        self.mensaje['text'] = 'Producto {} actualizado correctamente'.format(nombre)
        self.obtener_productos()
            
            
            
        
        

        
if __name__ == '__main__':
    window = Tk()
    aplicacion = Productos(window)
    window.mainloop()