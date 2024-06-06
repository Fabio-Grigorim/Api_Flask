from api import ma
from marshmallow import Schema, fields

class PetSchema(ma.Schema):
    class Meta:
        fields = ("_id", "nomePet", "nomeTutor", "diaBanho")
    _id = fields.Str()
    nomePet = fields.Str(required=True)
    nomeTutor = fields.Str(required=True)
    diaBanho = fields.Str(required=True)
