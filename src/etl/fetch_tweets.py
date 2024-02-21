import os
import asyncio
from dotenv import load_dotenv

# Suponiendo que twscrape es una biblioteca hipotética, reemplázala por la que uses.
from twscrape import API, gather

async def fetch_tweets(api, query, limit=100):
  # Esta función asincrónica extrae tweets usando la API de twscrape.
  tweets = await gather(api.search(query, limit=limit))
  return tweets

async def main():
  load_dotenv() # Carga las variables de entorno desde un archivo .env

  # Estas líneas obtienen las credenciales de Twitter desde las variables de entorno
  username = os.getenv('TWITTER_USERNAME')
  password = os.getenv('TWITTER_PASSWORD')
  email = os.getenv('TWITTER_EMAIL')
  email_password = os.getenv('TWITTER_EMAIL_PASSWORD')

  # Inicializa y configura la API de twscrape con las credenciales de usuario
  api = API()
  await api.pool.add_account(username, password, email, email_password)
  await api.pool.login_all()

  # Define una lista de figuras políticas y sus términos de búsqueda
  figuras = {
    "petro": ["@petrogustavo", "#petro", "#petro2026", "#pactohistorico", "Colombia+Humana"],
    "boric": ["@gabrielboric", "#boric", "#apruebo", "#frenteamplio", "Convergencia Social"],
    "lacallepou": ["@LuisLacallePou", "#lacallepou", "#Uruguay", "#coalicion multicolor", "Partido Nacional"],
    "lasso": ["@lassoguillermo", "#lasso", "#Ecuador", "#creo", "CREO"],
    "bukele": ["@nayibbukele", "#bukele", "#ElSalvador", "#nuevacapa", "Nuevas Ideas"],
    "amlo": ["@lopezobrador_", "#amlo", "#Mexico", "#cuartadetransformacion", "MORENA"],
    "lula": ["@LulaOficial", "#lula", "#brasil"],
    "cristina": ["@CFKArgentina", "#cristina", "#argentina"],
    "evo": ["@evoespueblo", "#evo", "#bolivia"],
    "arreaza": ["@jaarreaza", "#venezuela", "#chavismo"],
    "guaido": ["@jguaido", "#venezuela", "#guaido"],
  }

  # Itera por las figuras y extrae tweets para cada una
  for nombre, terminos in figuras.items():
    for termino in terminos:
      tweets = await fetch_tweets(api, termino)
      # Imprime los tweets o guárdalos en un archivo/base de datos
      for tweet in tweets:
        print(f"{tweet.id}\t{tweet.rawContent}\n")

if __name__ == "__main__":
  asyncio.run(main())

