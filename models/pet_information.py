from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma
from models.clients import ClientsSchema
from models.opperation_association import OpperationsSchema
from models.opperation_info import OpperationInfoSchema


class PetInformation(db.Model):
  __tablename__ = 'PetInformation'
  pet_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.String(), nullable=False)
  pet_type = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Clients.client_id'), nullable=True)
  owner = db.relationship('Clients', backref=db.backref('Clients', lazy=True))
  opperations = db.relationship('OpperationInfo', secondary='Opperations', back_populates = 'pet_id')
  opperation_dates = db.relationship('Opperations', back_populates = 'opperation_info')


  def __init__(self, pet_id, name, age, pet_type, active, owner_id):
    self.pet_id = pet_id
    self.name = name
    self.age = age
    self.pet_type = pet_type
    self.active = active
    self.owner_id = owner_id


class PetInformationSchema(ma.Schema):
  class Meta:
    fields = ['name', 'age,', 'pet_type', 'active', 'owner', 'opperations', 'opperation_dates']
  owner = ma.fields.Nested(ClientsSchema(only=("client_id", "first_name", "last_name")))
  opperations = ma.fields.Nested(OpperationInfoSchema(only=("opperation_id", "name", "description"), many=True))
  opperation_dates = ma.fields.Nested(OpperationsSchema(only=("opperation_id", "date"), many=True))

pet_information_schema = PetInformationSchema()
pets_information_schema = PetInformationSchema(many=True)