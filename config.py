import os


class Config:
    '''
    Perent configurations class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'posgresql+psycopg2://neorendo:postgres@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    '''
    child configuration with production configurations
    '''

class DevConfig(Config):
    '''
    Child Config with development configurations
    '''
    DEBUG = True

class TestConfig(Config):
    """
    Child Config with test configurations
    """
    pass


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}