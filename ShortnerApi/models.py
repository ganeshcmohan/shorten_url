import base64
from db import db
from typing import List
from datetime import date
import enum
from sqlalchemy.ext.hybrid import hybrid_property
# from sqlalchemy_utils.types.choice import ChoiceType


class ShortnerModel(db.Model):

    __tablename__ = "shortner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # long = db.Column(db.String(200), nullable=True)
    encode_url = db.Column(db.String(250), nullable=True)
    short = db.Column(db.String(80), nullable=True)

    # def __init__(self, long, short):
    #     self.long = long
    #     self.short = short

    # def __repr__(self):   
    #     return "ShortnerModel(long=%s, short=%s)" % (
    #         self.encode_url,
    #         # self.short
    #     )

    def long(self):
        return str(base64.urlsafe_b64decode(self.encode_url))

    # @hybrid_property   
    # def encode_url(self):   
    #     return self._encode_url

    # @encode_url.setter
    # def encode_url(self, value):
    #     return base64.urlsafe_b64encode(str(value).encode("ascii"))

    # def short(self):
    #     desired_length = 6
    #     return str(self.encode_url[:desired_length])

    # @short.setter
    # def short(self, url):
    #     desired_length = 6
    #     encoded_hash = base64.urlsafe_b64encode(str(hash(self.long)).encode("ascii"))
    #     return encoded_hash[:desired_length]

    def json(self):
        return {
            "long": self.long(),
            "short": self.short,
        }

    @classmethod
    def find_by_shortkey(cls, _key) -> "ShortnerModel":
        # encoded = base64.urlsafe_b64encode(str(_url).encode("ascii"))
        return cls.query.filter_by(short=_key).first()

    @classmethod
    def find_all(cls) -> List["ShortnerModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
