DB_HOST='127.0.0.1'
DB_PORT='5432'
DB_NAME='AsyncFastapiTest'
DB_PASS='postgres'
DB_USER='postgres'

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_ECHO = True