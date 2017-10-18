import os

class Config:
    '''
    General configurations Parent class
    '''

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The Parent configuration class with general configuration settings
    '''

    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The Parent configuration class with general configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
