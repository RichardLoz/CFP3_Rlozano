#Libreria TKINTER ==> Entorno grafico
from tkinter import *
from tkinter import messagebox
from Logica_login import validar_usuario

#Funcion que se llama al hacer click en el boton "Iniciar Sesion"
def iniciar_sesion():
    usuario = nombreEntry.get() # Obtener el texto ingresado en el campo usuario
    contraseña = contraseñaEntry.get()
    
    if validar_usuario(usuario,contraseña):
        messagebox.showinfo("Exito","Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error","Usuario o contraseña incorrectos")

#TODO: 1- VENTANA PRINCIPAL
root = Tk()
root.title("Login de usuario")
root.geometry("300x250")
root.config(bg="skyblue")

#TODO: 2- FRAME
mainframe = Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20)
mainframe.config(width=250, height=230)

#TODO: Titulo
titulo = Label(mainframe, text="Login de usuario", font=("Arial", 24))
titulo.grid(column=0, row=0, columnspan=2, pady=10)

#TODO: 3- Label - Entry ==> Usuario
nombreLabel = Label(mainframe, text="Usuario: ")
nombreLabel.grid(column=0, row=1, sticky=W, pady=5)

nombreEntry = Entry(mainframe, width=30)
nombreEntry.grid(column=1, row=1)   

contraseñaLabel = Label(mainframe, text="Contraseña: ")
contraseñaLabel.grid(column=0, row=2, sticky=W, pady=5)

contraseñaEntry = Entry(mainframe, width=30, show="*")
contraseñaEntry.grid(column=1, row=2)  

#TODO: 4- BOTON
iniciarSesionBtn = Button(mainframe, text="Iniciar Sesión", command=iniciar_sesion)
iniciarSesionBtn.grid(column=0, row=3, columnspan=2, pady=20)

root.mainloop()