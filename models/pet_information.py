from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma
from models.clients import ClientsSchema
from models.opperation_association import opperation_association_table
from models.vaccine_association import vaccine_association_table
# from models.opperation_association import OpperationsSchema
# from models.opperation_info import OpperationInfoSchema
# from models.vaccine_association import VaccinesSchema
# from models.vaccine_info import VaccineInfoSchema


class PetInformation(db.Model):
  __tablename__ = 'PetInformation'
  pet_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  name = db.Column(db.String(), nullable=False)
  age = db.Column(db.String(), nullable=False)
  pet_type = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)
  owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Clients.client_id'), nullable=True)
  
  owner_info = db.relationship('Clients', back_populates='pet_info')
  opperations = db.relationship('OpperationInfo', secondary=opperation_association_table, back_populates='pet_info')
  vaccines = db.relationship('VaccineInfo', secondary=vaccine_association_table, back_populates='pet_info')

  def __init__(self, name, age, pet_type, active, owner_id):
    self.name = name
    self.age = age
    self.pet_type = pet_type
    self.active = active
    self.owner_id = owner_id


class PetInformationSchema(ma.Schema):
  owner_info = ma.fields.Nested('ClientsSchema', only=['client_id', 'first_name', 'last_name'])
  opperations = ma.fields.Nested('OpperationInfoSchema', many=True, only=['opperation_id', 'name', 'description'])
  vaccines = ma.fields.Nested('VaccineInfoSchema', many=True, only=['vaccine_id', 'name', 'description'])
  class Meta:
    fields = ['pet_id', 'name', 'age,', 'pet_type', 'active', 'opperations', 'vaccines', 'owner_info']


pet_information_schema = PetInformationSchema()
pets_information_schema = PetInformationSchema(many=True)






