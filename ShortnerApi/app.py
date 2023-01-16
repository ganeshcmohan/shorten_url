from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db
from shortner import Shortner, ShortnerCreate, shortner_ns

# from marshmallow import ValidationError

app = Flask(__name__)
bluePrint = Blueprint("api", __name__, url_prefix="/api")
api = Api(bluePrint, doc="/doc", title="URL Shortner Application")
app.register_blueprint(bluePrint)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

api.add_namespace(shortner_ns)


@app.before_first_request
def create_tables():
    db.create_all()


shortner_ns.add_resource(ShortnerCreate, "/create")
shortner_ns.add_resource(Shortner, "/<string:shortkey>")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
