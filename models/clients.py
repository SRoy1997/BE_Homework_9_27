from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma



class Clients(db.Model):
  __tablename__ = 'Clients'
  client_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  first_name = db.Column(db.String(), nullable=False)
  last_name = db.Column(db.String(), nullable=False)
  phone = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False)
  street_address = db.Column(db.String(), nullable=False)
  city = db.Column(db.String(), nullable=False)
  state = db.Column(db.String(), nullable=False)
  postal_code = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)
  pet_info = db.relationship('PetInformation', back_populates='owner_info')

  def __init__(self, first_name, last_name, phone, email, street_address, city, state, postal_code, active):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email
    self.street_address = street_address
    self.city = city
    self.state = state
    self.postal_code = postal_code
    self.active = active


class ClientsSchema(ma.Schema):
  pet_info = ma.fields.Nested('PetInformationSchema', many=True, only=['pet_id', 'name'])
  class Meta:
    fields = ['client_id', 'first_name', 'last_name', 'phone', 'email', 'street_address', 'city', 'state', 'postal_code', 'active', 'pet_info']


client_schema = ClientsSchema()
clients_schema = ClientsSchema(many=True)