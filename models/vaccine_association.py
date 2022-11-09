from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma

# from models.clients import Clients



class Vaccines(db.Model):
  __tablename__ = 'Vaccines'
  vaccine_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  name = db.Column(db.String(), db.ForeignKey('PetInforamtion.pet_type'), nullable=False)
  pet_id = db.Column(UUID(as_uuid=True), db.ForeignKey('PetInformation.pet_id'), nullable=False)
  date = db.Column(db.DateTime(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)
  pet_info = db.relationship('PetInformation', backref=db.backref('PetInformation', lazy=True))


  def __init__(self, name, pet_id, date, active):
    self.name = name
    self.pet_id = pet_id
    self.date = date
    self.active = active


class VaccinesSchema(ma.Schema):
  class Meta:
    fields = ['vaccine_id', 'name', 'pet_id', 'date', 'active', 'pet_info']

vaccine_schema = VaccinesSchema()
vaccines_schema = VaccinesSchema(many=True)