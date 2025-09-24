from decouple import config


class Settings:
    DB_USER: str = config('USER')
    DB_PASS: str = config('PASSWORD')
    DB_HOST: str = config('HOST')
    DB_PORT: str = 5432
    DB_NAME: str = config('DATABASE')

    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()
