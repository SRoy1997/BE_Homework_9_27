# from concurrent.futures.process import _python_exit
# import email
# from db import db 
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from flask_marshmallow import Marshmallow
# import marshmallow as ma


# class Opperations(db.Model):
#   __tablename__ = 'Opperations'
#   opperation_id = db.Column('opperation_id', UUID(as_uuid=True), db.ForeignKey('OpperationInfo.opperation_id'), primary_key=True, nullable=False)
#   pet_id = db.Column('pet_id', UUID(as_uuid=True), db.ForeignKey('PetInformation.pet_id'), primary_key=True, nullable=False)
#   date = db.Column(db.DateTime(), nullable=False)
#   operation_info = db.relationship('PetInformation', back_populates = 'opperation_dates')


#   def __init__(self, opperation_id, pet_id, date):
#     self.opperation_id = opperation_id
#     self.pet_id = pet_id
#     self.date = date


# class OpperationsSchema(ma.Schema):
#   class Meta:
#     fields = ['opperation_id', 'pet_id', 'date', 'operation_info']

# opperation_schema = OpperationsSchema()
# opperations_schema = OpperationsSchema(many=True)