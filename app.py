# from ast import Or
# import json
# import psycopg2
from flask import Flask, request, Response
from flask_marshmallow import Marshmallow

from db import *
from models.clients import Clients
from models.pet_information import PetInformation
import endpoints
# from models.user import users_schema, Users, user_schema
# from models.org import Organizations, organizations_schema, organization_schema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sarahroy@localhost:5432/petinfo"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

def create_all():
  with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("All done!")


    # print("Querying for Sarah Roy...")
    # client_data = db.session.query(Clients).filter(Clients.email == 'sarah@devpipeline.com').first()
    # if client_data == None:
    #   print("Sarah Roy not found! Creating Sarah's account...")
    #   first_name = 'Sarah'
    #   last_name = 'Roy'
    #   email = 'sarah@devpipeline.com'
    #   phone = '3852014194'
    #   street_address = '1263 N Locust Ln'
    #   city = 'Provo'
    #   state = 'Utah'
    #   postal_code = '84604'
    #   active = True

    #   client_record = Clients(first_name, last_name, email, phone, street_address, city, state, postal_code, active)

    #   db.session.add(client_record)
    #   db.session.commit()
    # else:
    #   print("Sarah Roy found!")

    
    # print("Querying for Sarah's Pet...")
    # pet_data = db.session.query(PetInformation).filter(PetInformation.name == 'Artemis').first()
    # if pet_data == None:
    #   print("Sarah's Pet' not found! Creating Sarah's Pet's account...")
    #   name = 'Artemis'
    #   age = '1'
    #   pet_type = 'Cat'
    #   acitve = True
    #   owner_id = Clients.client_id where 

    #   client_record = Clients(first_name, last_name, email, phone, street_address, city, state, postal_code, active)

    #   db.session.add(client_record)
    #   db.session.commit()
    # else:
    #   print("Sarah Roy found!")







if __name__ == '__main__':
  create_all()
  app.run(host='0.0.0.0', port="4000")