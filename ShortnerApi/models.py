from base64 import decode, encode
import base64
from db import db
from typing import List
from datetime import date
import enum

# from sqlalchemy_utils.types.choice import ChoiceType


class ShortnerModel(db.Model):

    __tablename__ = "shortner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # long = db.Column(db.String(200), nullable=True)
    _encode_url = db.Column(db.String(250), nullable=True)
    # _short = db.Column(db.String(80), nullable=True)

    def __init__(self, long, short):
        self.long = long
        self.short = short

    def __repr__(self):
        return "ShortnerModel(long=%s, short=%s, encode_url=%s)" % (
            self.long,
            self.short,
            self.encode_url,
        )

    @property
    def long(self):
        return decode(self.encode_url)

    @property
    def encode_url(self):
        return self._encode

    @encode_url.setter
    def encode_url(self, url):
        return base64.urlsafe_b64encode(str(url).encode("ascii"))
        return encode(url)

    @property
    def short(self):
        desired_length = 6
        return self.encode_url[:desired_length]

    # @short.setter
    # def short(self, url):
    #     desired_length = 6
    #     encoded_hash = base64.urlsafe_b64encode(str(hash(self.long)).encode("ascii"))
    #     return encoded_hash[:desired_length]

    def json(self):
        return {
            "long": self.long,
            "short": self.short,
            "encode_url": self.encode_url,
        }

    @classmethod
    def find_by_url(cls, _url) -> "ShortnerModel":
        encoded = base64.urlsafe_b64encode(str(_url).encode("ascii"))
        return cls.query.filter_by(encode_url=encoded).first()

    @classmethod
    def find_all(cls) -> List["ShortnerModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
