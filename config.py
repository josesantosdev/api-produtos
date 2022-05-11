from instance import config

#Habilita o ambiente de desenvolvimento
DEBUG=True

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db}'
DATA_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False