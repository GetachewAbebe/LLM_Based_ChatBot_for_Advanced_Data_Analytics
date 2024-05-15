from quart import Quart
from models.database import db
from controllers.routes import data_blueprint
from config import config

app = Quart(__name__)
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(data_blueprint, url_prefix='/data')

if __name__ == '__main__':
    app.run()
