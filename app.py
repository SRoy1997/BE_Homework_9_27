# from ast import Or
# import json
# import psycopg2
from flask import Flask, request, Response, jsonify
from flask_marshmallow import Marshmallow

from db import *
from models.clients import Clients
from models.pet_information import PetInformation
# from models.pet_information import PetInformation
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

def populate_object(obj, data_dictionary):
  fields = data_dictionary.keys()
  for field in fields:
    if getattr(obj, field): 
      setattr(obj, field, data_dictionary[field])

@app.route("/client/add", methods=["POST"])
def client_add():
  post_data = request.json

  if not post_data:
    post_data = request.post
  
  first_name = post_data.get('first_name')
  last_name = post_data.get('last_name')
  phone = post_data.get('phone')
  email = post_data.get('email')
  street_address = post_data.get('street_address')
  city = post_data.get('city')
  state = post_data.get('state')
  postal_code = post_data.get('postal_code')
  active = post_data.get('active')

  add_client(first_name, last_name, phone, email, street_address, city, state, postal_code, active)

  return jsonify("Client created"), 201

def add_client(first_name, last_name, phone, email, street_address, city, state, postal_code, active): 
  new_client = Clients(first_name, last_name, phone, email, street_address, city, state, postal_code, active)
  
  db.session.add(new_client)
  db.session.commit()


@app.route("/pet/add", methods=["POST"])
def pet_add():
  post_data = request.json

  if not post_data:
    post_data = request.post
  
  name = post_data.get('name')
  age = post_data.get('age')
  pet_type = post_data.get('pet_type')
  active = post_data.get('active')
  owner_id = post_data.get('owner_id')
  

  add_pet(name, age, pet_type, active, owner_id)

  return jsonify("Pet created"), 201

def add_pet(name, age, pet_type, active, owner_id): 
  new_pet = PetInformation(name, age, pet_type, active, owner_id)
  
  db.session.add(new_pet)
  db.session.commit()







if __name__ == '__main__':
  create_all()
  app.run(host='0.0.0.0', port="8089")