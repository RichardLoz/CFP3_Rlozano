import tkinter as tk
from tkinter import ttk
import random

class GeneradorNumerosAleatorios:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Números Aleatorios")

        # Variables para almacenar los datos
        self.nombres = []
        self.resultados = []

        # Etiqueta y entrada para el nombre
        self.label_nombre = ttk.Label(root, text="Nombre:")
        self.entry_nombre = ttk.Entry(root)
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Botón para generar números aleatorios
        self.boton_generar = ttk.Button(root, text="Generar", command=self.generar_numeros)
        self.boton_generar.grid(row=1, column=0, columnspan=2, pady=10)

        # Grilla para mostrar resultados
        self.tree = ttk.Treeview(root, columns=("Nombre", "Ejercicio 1", "Ejercicio 2"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Ejercicio 1", text="Ejercicio 1")
        self.tree.heading("Ejercicio 2", text="Ejercicio 2")
        self.tree.column("#0", width=30, stretch=tk.NO)
        self.tree.column("Nombre", anchor=tk.W, width=100)
        self.tree.column("Ejercicio 1", anchor=tk.CENTER, width=80)
        self.tree.column("Ejercicio 2", anchor=tk.CENTER, width=80)
        self.tree.grid(row=2, column=0, columnspan=2, pady=10)

    def generar_numeros(self):
        nombre = self.entry_nombre.get()

        if nombre:
            # Generar dos números aleatorios no iguales
            numero1 = random.randint(1, 5)
            numero2 = random.randint(1, 5)
            while numero2 == numero1:
                numero2 = random.randint(1, 5)

            # Almacenar en las listas
            self.nombres.append(nombre)
            self.resultados.append((numero1, numero2))

            # Mostrar en la grilla
            item_id = len(self.nombres)
            self.tree.insert("", "end", text=item_id, values=(nombre, numero1, numero2))

            # Limpiar la entrada para el próximo nombre
            self.entry_nombre.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
app = GeneradorNumerosAleatorios(root)
root.mainloop()
