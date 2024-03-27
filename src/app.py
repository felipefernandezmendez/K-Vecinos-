from utils import db_connect
import pandas as pd


engine = db_connect()

engine
if engine:
    print("Conexión exitosa")

data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv')
data.to_sql('tabla_peliculas', engine, if_exists='replace', index=False)

data2 = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv')
data2.to_sql('tabla_creditos', engine, if_exists='replace', index=False)

# Unir las dos tablas por el título
query = """
SELECT *
FROM tabla_peliculas AS peliculas
JOIN tabla_creditos AS creditos
ON peliculas.title = creditos.title
"""



