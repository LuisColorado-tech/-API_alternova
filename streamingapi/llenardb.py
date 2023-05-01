from .models import Pelicula, Serie
from imdb import IMDb
from faker import Faker
import random
fake = Faker()


generos = ['Comedia', 'Drama', 'Acción', 'Aventuras', 'Ciencia ficción', 'Terror', 'Romance']

def llenar_db():
    peliculas = []
    for i in range(20):
        pelicula = {
            'nombre': fake.sentence(nb_words=3),
            'genero': random.choice(generos),
            'tipo': 'pelicula',
            'visualizaciones': fake.random_int(min=0, max=1000),
            'puntaje': round(fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5), 1)
        }
        peliculas.append(pelicula)

    series = []
    for i in range(20):
        serie = {
            'nombre': fake.sentence(nb_words=3),
            'genero': random.choice(generos),
            'tipo': 'serie',
            'visualizaciones': fake.random_int(min=0, max=1000),
            'puntaje': round(fake.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5), 1)
        }
        series.append(serie)
    # Guardar las películas
    for pelicula in peliculas:
        p = Pelicula(nombre=pelicula['nombre'], genero=pelicula['genero'], tipo=pelicula['tipo'], visualizaciones=pelicula['visualizaciones'], puntaje=pelicula['puntaje'])
        p.save()

    # Guardar las series
    for serie in series:
        s = Serie(nombre=serie['nombre'], genero=serie['genero'], tipo=serie['tipo'], visualizaciones=serie['visualizaciones'], puntaje=serie['puntaje'])
        s.save()

def ver_ids_peliculas():
    peliculas = Pelicula.objects.all()
    for pelicula in peliculas:
        print(pelicula.id)
