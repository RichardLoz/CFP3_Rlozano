# Nos va a permitir descargar videos de youtube.
# pip install pytube

#Importar la biblioteca pytube, que se utiliza para descargar videos de Youtube




import pytube

# Define una función llamada descargar_video que toma dos parámetros: la URL del video y la carpeta de destino
def descargar_video(url, carpeta):
    # Crea un objeto YouTube con la URL proporcionada
    youtube = pytube.YouTube(url)
    
    # Filtra los streams de video para obtener el primer stream que tenga una resolución de 720p
    video = youtube.streams.filter(res="720p").first()
    
    # Descarga el video en la carpeta especificada
    video.download(output_path=carpeta)
    # Imprime un mensaje indicando que el video se está descargando en la carpeta especificada
    print(f"El video se está descargando en {carpeta}")
    # Filtra los streams progresivos (que contienen tanto video como audio)
    streams = youtube.streams.filter(progressive=True)
    # Itera sobre los streams filtrados y imprime la resolución de cada stream
    for stream in streams:
        print(stream.resolution)

# # C:\Users\richi\Downloads\Videos
# Llama a la función descargar_video con una URL específica de YouTube y una carpeta de destino
descargar_video("https://m.youtube.com/watch?v=EQRERIwnE_g", "C:/Users/richi/Downloads/Videos")