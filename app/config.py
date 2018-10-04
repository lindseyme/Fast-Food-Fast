import os

base_dir = os.path.abspath(os.path.dirname(__file__))
#postgres_local_base = 'postgresql://postgres:123456@localhost/'
#database_name = 'api'


class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'thisissecret')
    
class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
   
class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    # AUTH_TOKEN_EXPIRY_DAYS = 0
    # AUTH_TOKEN_EXPIRY_SECONDS = 3
    # AUTH_TOKEN_EXPIRATION_TIME_DURING_TESTS = 5
    


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = True
    
