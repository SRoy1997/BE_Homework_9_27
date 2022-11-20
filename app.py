# from ast import Or
# import json
# import psycopg2
from flask import Flask, request, Response, jsonify
from flask_marshmallow import Marshmallow

from db import *
from models.clients import Clients, clients_schema
from models.pet_information import PetInformation, pets_information_schema
from models.pet_type import PetType, pet_type_schema
from models.opperation_info import OpperationInfo, opperations_info_schema
from models.vaccine_info import VaccineInfo, vaccines_info_schema

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

@app.route('/clients/get', methods=['GET'] )
def get_clients():
  results = db.session.query(Clients).filter(Clients.active == True).all()

  if results:
    return jsonify(clients_schema.dump(results)), 200
  
  else:
    return jsonify('No Client Found'), 404


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

@app.route('/pets/get', methods=['GET'] )
def get_pets():
  results = db.session.query(PetInformation).filter(PetInformation.active == True).all()

  if results:
    return jsonify(pets_information_schema.dump(results)), 200
  
  else:
    return jsonify('No Pets Found'), 404



@app.route("/pet_type/add", methods=["POST"])
def pet_type_add():
  post_data = request.json

  if not post_data:
    post_data = request.post
  
  pet_id = post_data.get('pet_id')
  pet_type = post_data.get('pet_type')
  breed_species = post_data.get('breed_species')
  size = post_data.get('size')
  weight = post_data.get('weight')
  temperment = post_data.get('temperment')
  active = post_data.get('active')
  

  add_pet_type(pet_id, pet_type, breed_species, size, weight, temperment, active)

  return jsonify("Pet Type created"), 201

def add_pet_type(pet_id, pet_type, breed_species, size, weight, temperment, active): 
  new_pet_type = PetType(pet_id, pet_type, breed_species, size, weight, temperment, active)
  
  db.session.add(new_pet_type)
  db.session.commit()

@app.route('/pet_type/get/<pet_id>', methods=['GET'] )
def get_pet_type(pet_id):
  results = db.session.query(PetType).filter(PetType.pet_id == pet_id).first()

  if results:
    return jsonify(pet_type_schema.dump(results)), 200
  
  else:
    return jsonify('No Pet Type Found'), 404



@app.route("/opperation/add", methods=["POST"])
def opperation_add():
  post_data = request.json

  if not post_data:
    post_data = request.post
  
  name = post_data.get('name')
  description = post_data.get('description')
  active = post_data.get('active')
  

  add_opperation(name, description, active)

  return jsonify("Opperation created"), 201

def add_opperation(name, description, active): 
  new_opperation = OpperationInfo(name, description, active)
  
  db.session.add(new_opperation)
  db.session.commit()

@app.route('/opperations/get', methods=['GET'] )
def get_opperations():
  results = db.session.query(OpperationInfo).filter(OpperationInfo.active == True).all()

  if results:
    return jsonify(opperations_info_schema.dump(results)), 200
  
  else:
    return jsonify('No Opperations Found'), 404



@app.route("/vaccine/add", methods=["POST"])
def vaccine_add():
  post_data = request.json

  if not post_data:
    post_data = request.post
  
  name = post_data.get('name')
  description = post_data.get('description')
  active = post_data.get('active')
  

  add_vaccine(name, description, active)

  return jsonify("Vaccine created"), 201

def add_vaccine(name, description, active): 
  new_vaccine = VaccineInfo(name, description, active)
  
  db.session.add(new_vaccine)
  db.session.commit()

@app.route('/vaccine/get', methods=['GET'] )
def get_vaccine():
  results = db.session.query(VaccineInfo).filter(VaccineInfo.active == True).all()

  if results:
    return jsonify(vaccines_info_schema.dump(results)), 200
  
  else:
    return jsonify('No Vaccines Found'), 404





if __name__ == '__main__':
  create_all()
  app.run(host='0.0.0.0', port="8089")