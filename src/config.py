from decouple import config

class Config:
    SECRECT_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True

config={
    'development' : DevelopmentConfig
}



