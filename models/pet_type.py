from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma

# from models.clients import Clients



class PetType(db.Model):
  __tablename__ = 'PetType'
  pet_id = db.Column(UUID(as_uuid=True), db.ForeignKey('PetInformation.pet_id'), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  pet_type = db.Column(db.String(), db.ForeignKey('PetInforamtion.pet_type'), nullable=False)
  breed_species = db.Column(db.String(), nullable=False)
  size = db.Column(db.String(), nullable=False)
  weight = db.Column(db.String(), nullable=False)
  temperment = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)
  pet_info = db.relationship('PetInformation', backref=db.backref('PetInformation', lazy=True))


  def __init__(self, pet_id, pet_type, breed_species, size, weight, temperment, active):
    self.pet_id = pet_id
    self.pet_type = pet_type
    self.breed_species = breed_species
    self.size = size
    self.weight = weight
    self.temperment = temperment
    self.active = active


class PetTypeSchema(ma.Schema):
  class Meta:
    fields = ['pet_id', 'pet_type', 'breed_species', 'size', 'weight', 'temperment', 'active', 'pet_info']

pet_type_schema = PetTypeSchema()
pets_type_schema = PetTypeSchema(many=True)