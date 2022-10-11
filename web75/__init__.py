import os
from flask import Flask

def create_app(test_config=None):
    #creando y configurando app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        DATABASE=os.path.join(app.instance_path, "web75.sqlite"),
    )
    
    if test_config is None:
        # carga la configuracion de la instancia, si es que existe, cuando no es una prueba
        app.config.from_pyfile('config.py', silent=True)
    else:
        # cargue la configuracion de prueba si es pasada
        app.config.from_mapping(test_config)
    
    # asegura que el folder de la instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Apps
    from . import conocenos
    app.register_blueprint(conocenos.bp)
    
    return app
