class Config:
    '''
    General configurations Parent class
    '''

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

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
