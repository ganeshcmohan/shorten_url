from ma import ma
from models import ShortnerModel


class ShortnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShortnerModel
        load_instance = True
        # load_only = ("encode_url",)   
        # exclude = ("short", )

    id = ma.auto_field()
