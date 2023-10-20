#Base de Conocimiento

# Crear una base de conocimiento de películas usando un diccionario
base_de_conocimiento = {
    "Star Wars": {
        "director": "George Lucas",
        "lanzamiento": 1977,
        "genero": "Ciencia Ficcion",
        "actores": ["Mark Hamill", "Harrison Ford", "Carrie Fisher"]
    },
    "The Shawshank Redemption": {
        "director": "Frank Darabont",
        "lanzamiento": 1994,
        "genero": "Drama",
        "actores": ["Tim Robbins", "Morgan Freeman"]
    },
    "Inception": {
        "director": "Christopher Nolan",
        "lanzamiento": 2010,
        "genero": "Ciencia Ficcion",
        "actores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]
    }
}

# Consulta la base de conocimiento para obtener información sobre una película
pelicula = "Star Wars"
if pelicula in base_de_conocimiento:
    informacion = base_de_conocimiento[pelicula]
    print(f"Informacion sobre la pelicula {pelicula}:")
    print(f"Director: {informacion['director']}")
    print(f"Lanzamiento: {informacion['lanzamiento']}")
    print(f"Genero: {informacion['genero']}")
    print(f"Actores: {', '.join(informacion['actores'])}")
else:
    print(f"No se encontro informacion sobre la pelicula {pelicula}")

