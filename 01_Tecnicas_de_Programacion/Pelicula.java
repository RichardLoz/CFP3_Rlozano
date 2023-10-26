import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Pelicula {
    private String titulo;
    private String nombreCliente;

    public Pelicula(String titulo) {
        this.titulo = titulo;
        this.nombreCliente = "";
    }

    public String getTitulo() {
        return titulo;
    }

    public String getNombreCliente() {
        return nombreCliente;
    }

    public void presta(String cliente) {
        if (nombreCliente.isEmpty()) {
            nombreCliente = cliente;
        } else {
            System.out.println("La película ya está prestada a " + nombreCliente);
        }
    }

    public void devuelve(String cliente) {
        if (nombreCliente.equals(cliente)) {
            nombreCliente = "";
        } else {
            System.out.println("La película no está prestada a " + cliente);
        }
    }
}

public class VideoClub {
    private Map<String, List<Pelicula>> peliculasPorGenero;

    public VideoClub() {
        peliculasPorGenero = new HashMap<>();
        peliculasPorGenero.put("accion", new ArrayList<>());
        peliculasPorGenero.put("suspenso", new ArrayList<>());
        peliculasPorGenero.put("comedia", new ArrayList<>());
        peliculasPorGenero.put("drama", new ArrayList<>());
    }

    public void añadePelicula(Pelicula pelicula, String genero) {
        List<Pelicula> peliculas = peliculasPorGenero.get(genero.toLowerCase());

        if (peliculas != null) {
            boolean peliculaExiste = false;
            for (Pelicula p : peliculas) {
                if (p.getTitulo().equals(pelicula.getTitulo())) {
                    peliculaExiste = true;
                    break;
                }
            }

            if (!peliculaExiste) {
                peliculas.add(pelicula);
                System.out.println("Película agregada al género " + genero);
            } else {
                System.out.println("La película ya existe en el género " + genero);
            }
        } else {
            System.out.println("Género no válido: " + genero);
        }
    }

    private Pelicula buscaPelicula(String titulo, String genero) {
        List<Pelicula> peliculas = peliculasPorGenero.get(genero.toLowerCase());
        if (peliculas != null) {
            for (Pelicula pelicula : peliculas) {
                if (pelicula.getTitulo().equals(titulo)) {
                    return pelicula;
                }
            }
        }
        return null;
    }

    public void prestaPelicula(String titulo, String genero, String cliente) {
        Pelicula peliculaEncontrada = buscaPelicula(titulo, genero);
        if (peliculaEncontrada != null) {
            peliculaEncontrada.presta(cliente);
            System.out.println("Película prestada a " + cliente);
        } else {
            System.out.println("La película no existe en el género " + genero);
        }
    }

    public void eliminaPelicula(String titulo, String genero) {
        Pelicula peliculaEncontrada = buscaPelicula(titulo, genero);
        if (peliculaEncontrada != null) {
            List<Pelicula> peliculas = peliculasPorGenero.get(genero.toLowerCase());
            peliculas.remove(peliculaEncontrada);
            System.out.println("Película eliminada");
        } else {
            System.out.println("La película no existe en el género " + genero);
        }
    }

    public void devuelvePelicula(String titulo, String genero, String cliente) {
        Pelicula peliculaEncontrada = buscaPelicula(titulo, genero);
        if (peliculaEncontrada != null) {
            peliculaEncontrada.devuelve(cliente);
            System.out.println("Pelicula devuelta por " + cliente);
        } else {
            System.out.println("La película no existe en el género " + genero);
        }
    }

}

public class Main {
    public static void main(String[] args) {
        VideoClub videoClub = new VideoClub();

        Pelicula pelicula1 = new Pelicula("Pelicula 1");
        Pelicula pelicula2 = new Pelicula("Pelicula 2");
        Pelicula pelicula3 = new Pelicula("Pelicula 3");

        videoClub.añadePelicula(pelicula1, "accion");
        videoClub.añadePelicula(pelicula2, "comedia");
        videoClub.añadePelicula(pelicula3, "suspenso");

        videoClub.prestaPelicula("Pelicula 1", "accion", "Cliente A");
        videoClub.prestaPelicula("Pelicula 2", "comedia", "Cliente B");
        videoClub.devuelvePelicula("Pelicula 1", "accion", "Cliente A");

        videoClub.eliminaPelicula("Pelicula 3", "suspenso");
    }
}
