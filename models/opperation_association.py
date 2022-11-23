from db import db 
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma


opperation_association_table = db.Table(
  "OpperationAssociation",
  db.Model.metadata,
  db.Column('pet_id', db.ForeignKey('PetInformation.pet_id'), primary_key=True),
  db.Column('opperation_id', db.ForeignKey('OpperationInfo.opperation_id'), primary_key=True)
)