from marshmallow import Schema, fields, post_load
from football_api.models.player import Player

class PlayerSchema(Schema):
    """
    Player Marshmallow Schema
    Marshmallow schema used for loading/dumping Players
    """
