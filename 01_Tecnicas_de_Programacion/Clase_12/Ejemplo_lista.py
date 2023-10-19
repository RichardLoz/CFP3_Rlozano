import os

# Ruta de la carpeta principal donde se crearán las subcarpetas
carpeta_parcial = "C:/Users/Richard/Desktop/Prueba_Carpetas" 


# Nombres de las subcarpetas en un array
carpetas_alumnos = ["Jesica_Riveros","Roberto Zare", "Milagros Cornejo", "Ronal Gonzales", "Bryam Navarro", "Tania Guerrero","Deivis Rivas","Fulanito"]

# Comprobamos si la carpeta principal existe, si no existe, la creamos
if not os.path.exists(carpeta_parcial):
    os.makedirs(carpeta_parcial)

# Crear las subcarpetas
for carpeta_alumnos in carpetas_alumnos:
    subcarpeta_path = os.path.join(carpeta_parcial, carpeta_alumnos)
    os.makedirs(subcarpeta_path)
    print(f'Se ha creado la subcarpeta:{carpeta_alumnos} en {carpeta_parcial}')