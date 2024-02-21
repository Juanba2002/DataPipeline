import os
import asyncio
from dotenv import load_dotenv

# Suponiendo que twscrape es una biblioteca hipotética, reemplázala por la que uses.
from twscrape import API, gather

async def fetch_tweets(api, queries, limit=100):
    # Esta función asincrónica extrae tweets usando la API de twscrape.
    all_tweets = []
    for query in queries:
        tweets = await gather(api.search(query, limit=limit))
        all_tweets.extend(tweets)
    return all_tweets

async def main():
    load_dotenv()  # Carga las variables de entorno desde un archivo .env

    # Estas líneas obtienen las credenciales de Twitter desde las variables de entorno
    username = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')
    email = os.getenv('TWITTER_EMAIL')
    email_password = os.getenv('TWITTER_EMAIL_PASSWORD')

    # Inicializa y configura la API de twscrape con las credenciales de usuario
    api = API()
    await api.pool.add_account(username, password, email, email_password)
    await api.pool.login_all()
    
    queries = ['Gustavo Petro', 'Nayib Bukele']

    # Llama a la función fetch_tweets para extraer tweets con un término específico
    tweets = await fetch_tweets(api, queries, limit=100)

    # Ejemplo de cómo podrías manejar los tweets extraídos
    for tweet in tweets:
        print(f"{tweet.id}\t{tweet.rawContent}\n")

if __name__ == "__main__":
    asyncio.run(main())
