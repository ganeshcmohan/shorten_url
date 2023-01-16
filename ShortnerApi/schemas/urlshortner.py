from ma import ma
from models import ShortnerModel


class ShortnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShortnerModel
        load_instance = True
        # load_only = ("short",)
        include_fk = True
        # exclude = ("encode")

    id = ma.auto_field()
