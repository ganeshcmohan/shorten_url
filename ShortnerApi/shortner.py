from flask import request
from flask_restplus import Resource, fields, Namespace
import base64
from models import ShortnerModel
from schemas.urlshortner import ShortnerSchema

URL_NOT_FOUND = "Url not found."


shortner_ns = Namespace("shortner", description="Shortner related operations")

shortner_schema = ShortnerSchema()

# Model required by flask_restplus for expect


shortner = shortner_ns.model(
    "Shortner",
    {
        "encode_url": fields.String,
        "short": fields.String,
    },  
)


class Shortner(Resource):
    @shortner_ns.expect(shortner)
    def get(self, shortkey):
        print("In detail")
        short_url = ShortnerModel.find_by_shortkey(shortkey)
        if short_url:
            return short_url.json()
        return {"message": URL_NOT_FOUND}, 404


class ShortnerCreate(Resource):
    @shortner_ns.expect(shortner)
    @shortner_ns.doc("Store a new url")
    def post(self):
        print("In post")
        shorter_json = request.get_json()
        shorter_json["encode_url"] = base64.urlsafe_b64encode(str(shorter_json['url']).encode("ascii"))
        desired_length = 6
        shorter_json["short"] = shorter_json["encode_url"][:desired_length]
        shorter_json.pop('url')
        shorter_data = shortner_schema.load(shorter_json)
        # shorter_data = ShortnerModel()
        # shorter_data._encode_url = encode_url
        shorter_data.save_to_db()
        return shorter_data.json(), 201
