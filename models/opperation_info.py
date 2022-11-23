from concurrent.futures.process import _python_exit
import email
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma
from models.opperation_association import opperation_association_table


class OpperationInfo(db.Model):
  __tablename__ = 'OpperationInfo'
  opperation_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  name = db.Column(db.String(), nullable=False)
  description = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)

  pet_info = db.relationship('PetInformation', secondary=opperation_association_table, back_populates='opperations')

  def __init__(self, name, description, active):
    self.name = name
    self.description = description
    self.active = active


class OpperationInfoSchema(ma.Schema):
  pet_info = ma.fields.Nested('PetInformationSchema', many=True, only=['pet_id', 'name', 'pet_type', 'owner_id'])
  class Meta:
    fields = ['opperation_id', 'name', 'description', 'active', 'pet_info']

opperation_info_schema = OpperationInfoSchema()
opperations_info_schema = OpperationInfoSchema(many=True)