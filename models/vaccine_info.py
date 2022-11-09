# from concurrent.futures.process import _python_exit
# import email
# from db import db 
# from sqlalchemy.dialects.postgresql import UUID
# import uuid
# from flask_marshmallow import Marshmallow
# import marshmallow as ma


# class VaccineInfo(db.Model):
#   __tablename__ = 'VaccineInfo'
#   vaccine_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#   name = db.Column(db.String(), nullable=False)
#   description = db.Column(db.String(), nullable=False)
#   active = db.Column(db.Boolean(), default=False, nullable=False)


#   def __init__(self, name, description, active):
#     self.name = name
#     self.description = description
#     self.active = active


# class VaccineInfoSchema(ma.Schema):
#   class Meta:
#     fields = ['vaccine_id', 'name', 'description', 'active']

# vaccine_info_schema = VaccineInfoSchema()
# vaccines_info_schema = VaccineInfoSchema(many=True)