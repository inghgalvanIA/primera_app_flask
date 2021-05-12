#intruccion para la clave secreta
class Config:
    pass
#clase para la configuracion de desarrollo
class DevelopmentConfig(Config):
    DEBUG=True

config = {
    'development': DevelopmentConfig,
    'default' : DevelopmentConfig

}