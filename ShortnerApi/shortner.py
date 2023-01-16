from flask import request
from flask_restplus import Resource, fields, Namespace

from models import ShortnerModel
from schemas.urlshortner import ShortnerSchema

URL_NOT_FOUND = "Url not found."


shortner_ns = Namespace("shortner", description="Shortner related operations")

shortner_schema = ShortnerSchema()

# Model required by flask_restplus for expect


shortner = shortner_ns.model(
    "Shortner",
    {
        "long": fields.String,
    },
)


class Shortner(Resource):
    def get(self, url):
        print("In detail")
        short_url = ShortnerModel.find_by_url(url)
        if short_url:
            return short_url.json()
        return {"message": URL_NOT_FOUND}, 404


class ShortnerCreate(Resource):
    @shortner_ns.expect(shortner)
    @shortner_ns.doc("Store a new url")
    def post(self):
        print("In post")
        shorter_json = request.get_json()
        shorter_data = shortner_schema.load(shorter_json)
        shorter_data.save_to_db()
        return shorter_data.json(), 201
