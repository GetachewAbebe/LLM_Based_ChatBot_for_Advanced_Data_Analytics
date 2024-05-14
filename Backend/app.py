from quart import Quart
from backend.controllers.routes import bp as routes_bp

app = Quart(__name__)
app.register_blueprint(routes_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
