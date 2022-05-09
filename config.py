import os


class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MOVIE_API_KEY = '87098bb29fb165ab9f109114be82f215'
    SECRET_KEY = 'KevinMalomba'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}