from db import db 
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma


vaccine_association_table = db.Table(
  "VaccineAssociation",
  db.Model.metadata,
  db.Column('pet_id', db.ForeignKey('PetInformation.pet_id'), primary_key=True),
  db.Column('vaccine_id', db.ForeignKey('VaccineInfo.vaccine_id'), primary_key=True)
)