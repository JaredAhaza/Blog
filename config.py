import os


class Config:
    '''
    Perent configurations class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
    '''
    child configuration with production configurations
    '''
    pass

class DevConfig(Config):
    '''
    Child Config with development configurations
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jared:12345@localhost/blog'
    DEBUG = True

class TestConfig(Config):
    """
    Child Config with test configurations to test database ralationships
    """
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}