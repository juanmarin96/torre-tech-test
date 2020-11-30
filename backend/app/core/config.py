from environs import Env

env = Env()
env.read_env()


class Settings:
    SQLALCHEMY_DATABASE_URL = env('SQLALCHEMY_DATABASE_URL')


settings = Settings()
