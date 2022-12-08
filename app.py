from flask import Flask, request, Response, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID


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

@app.route('/client/update', methods=['POST', 'PUT'] )
def client_update():
  post_data = request.get_json()
  client_id = post_data.get("client_id")
  if client_id == None:
    return jsonify("ERROR: client_id missing"), 400
  first_name = post_data.get('first_name')
  last_name = post_data.get('last_name')
  phone = post_data.get('phone')
  email = post_data.get('email')
  street_address = post_data.get('street_address')
  city = post_data.get('city')
  state = post_data.get('state')
  postal_code = post_data.get('postal_code')
  active = post_data.get('active')

  if active == None:
    active = True
    
    client_data = None

    if client_id != None:
      client_data = db.session.query(Clients).filter(Clients.client_id == client_id).first()

    if client_data:
      client_id = client_data.client_id
      if first_name:
        client_data.first_name = first_name
      if last_name is not None:
        client_data.last_name = last_name
      if phone is not None:
        client_data.phone = phone
      if email is not None:
        client_data.email = email
      if street_address is not None:
        client_data.street_address = street_address
      if city is not None:
        client_data.city = city
      if state is not None:
        client_data.state = state
      if postal_code is not None:
        client_data.postal_code = postal_code
      if active is not None:
        client_data.active = active

      db.session.commit()

      return jsonify('Client Information Updated'), 200
    else:
      return jsonify("Client Not Found"), 404
  else:
    return jsonify("ERROR: request must be in JSON format"), 400

@app.route('/client/activate/<client_id>', methods=['GET'] )
def client_activate(client_id):
  results = db.session.query(Clients).filter(Clients.client_id == client_id).first()
  results.active=True
  db.session.commit()
  return jsonify('Client Activated'), 200

@app.route('/client/deactivate/<client_id>', methods=['GET'] )
def client_deactivate(client_id):
  results = db.session.query(Clients).filter(Clients.client_id == client_id).first()
  results.active=False
  db.session.commit()
  return jsonify('Client Deactivated'), 200

@app.route('/client/delete/<client_id>', methods=['DELETE'] )
def client_delete(client_id):
  results = db.session.query(Clients).filter(Clients.client_id == client_id).first()
  db.session.delete(results)
  db.session.commit()
  return jsonify('Client Deleted'), 200

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

@app.route('/pet/update', methods=['POST', 'PUT'] )
def pet_update():
  post_data = request.get_json()
  pet_id = post_data.get("pet_id")
  if pet_id == None:
    return jsonify("ERROR: pet_id missing"), 400
  name = post_data.get('name')
  age = post_data.get('age')
  pet_type = post_data.get('pet_type')
  active = post_data.get('active')
  owner_id = post_data.get('owner_id')
  opperation_id = post_data.get('opperation_id')
  vaccine_id = post_data.get('vaccine_id')

  if active == None:
    active = True
    
    pet_data = None

    if pet_id != None:
      pet_data = db.session.query(PetInformation).filter(PetInformation.pet_id == pet_id).first()

    if pet_data:
      pet_id = pet_data.pet_id
      if name:
        pet_data.name = name
      if age is not None:
        pet_data.age = age
      if pet_type is not None:
        pet_data.pet_type = pet_type
      if active is not None:
        pet_data.active = active
      if owner_id is not None:
        pet_data.owner_id = owner_id
      if active is not None:
        pet_data.active = active
      if opperation_id != None or opperation_id != '':
        opperation = db.session.query(OpperationInfo).filter(OpperationInfo.opperation_id == opperation_id).first()
        if opperation != None:
          opperation.pet_info.append(pet_data)
      if vaccine_id != None or vaccine_id != '':
        vaccine = db.session.query(VaccineInfo).filter(VaccineInfo.vaccine_id == vaccine_id).first()
        if vaccine != None:
          vaccine.pet_info.append(pet_data)

      db.session.commit()

      return jsonify('Pet Information Updated'), 200
    else:
      return jsonify("Pet Not Found"), 404
  else:
    return jsonify("ERROR: request must be in JSON format"), 400

@app.route('/pet/activate/<pet_id>', methods=['GET'] )
def pet_activate(pet_id):
  results = db.session.query(PetInformation).filter(PetInformation.pet_id == pet_id).first()
  results.active=True
  db.session.commit()
  return jsonify('Pet Activated'), 200

@app.route('/pet/deactivate/<pet_id>', methods=['GET'] )
def pet_deactivate(pet_id):
  results = db.session.query(PetInformation).filter(PetInformation.pet_id == pet_id).first()
  results.active=False
  db.session.commit()
  return jsonify('Pet Deactivated'), 200

@app.route('/pet/delete/<pet_id>', methods=['DELETE'] )
def pet_delete(pet_id):
  results = db.session.query(PetInformation).filter(PetInformation.pet_id == pet_id).first()
  db.session.delete(results)
  db.session.commit()
  return jsonify('Pet Deleted'), 200


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

@app.route('/pet_type/update', methods=['POST', 'PUT'] )
def pet_type_update():
  post_data = request.get_json()
  pet_id = post_data.get("pet_id")
  if pet_id == None:
    return jsonify("ERROR: pet_id missing"), 400
  pet_type = post_data.get('pet_type')
  breed_species = post_data.get('breed_species')
  size = post_data.get('size')
  weight = post_data.get('weight')
  temperment = post_data.get('temperment')
  active = post_data.get('active')

  if active == None:
    active = True
    
    pet_type_data = None

    if pet_id != None:
      pet_type_data = db.session.query(PetType).filter(PetType.pet_id == pet_id).first()

    if pet_type_data:
      pet_id = pet_type_data.pet_id
      if pet_type:
        pet_type_data.pet_type = pet_type
      if breed_species is not None:
        pet_type_data.breed_species = breed_species
      if size is not None:
        pet_type_data.size = size
      if weight is not None:
        pet_type_data.weight = weight
      if temperment is not None:
        pet_type_data.temperment = temperment
      if active is not None:
        pet_type_data.active = active

      db.session.commit()

      return jsonify('Pet Type Information Updated'), 200
    else:
      return jsonify("Pet Type Not Found"), 404
  else:
    return jsonify("ERROR: request must be in JSON format"), 400



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

@app.route('/opperation/update', methods=['POST', 'PUT'] )
def opperation_update():
  post_data = request.get_json()
  opperation_id = post_data.get("opperation_id")
  if opperation_id == None:
    return jsonify("ERROR: opperation_id missing"), 400
  name = post_data.get('name')
  description = post_data.get('description')
  active = post_data.get('active')

  if active == None:
    active = True
    
    pet_type_data = None

    if opperation_id != None:
      pet_type_data = db.session.query(OpperationInfo).filter(OpperationInfo.opperation_id == opperation_id).first()

    if pet_type_data:
      opperation_id = pet_type_data.opperation_id
      if name:
        pet_type_data.name = name
      if description is not None:
        pet_type_data.description = description
      if active is not None:
        pet_type_data.active = active

      db.session.commit()

      return jsonify('Opperaton Information Updated'), 200
    else:
      return jsonify("Opperaton Not Found"), 404
  else:
    return jsonify("ERROR: request must be in JSON format"), 400

@app.route('/opperation/activate/<opperation_id>', methods=['GET'] )
def opperation_activate(opperation_id):
  results = db.session.query(OpperationInfo).filter(OpperationInfo.opperation_id == opperation_id).first()
  results.active=True
  db.session.commit()
  return jsonify('Opperation Activated'), 200

@app.route('/opperation/deactivate/<opperation_id>', methods=['GET'] )
def opperation_deactivate(opperation_id):
  results = db.session.query(OpperationInfo).filter(OpperationInfo.opperation_id == opperation_id).first()
  results.active=False
  db.session.commit()
  return jsonify('Opperation Deactivated'), 200

@app.route('/opperation/delete/<opperation_id>', methods=['DELETE'] )
def opperation_delete(opperation_id):
  results = db.session.query(OpperationInfo).filter(OpperationInfo.opperation_id == opperation_id).first()
  db.session.delete(results)
  db.session.commit()
  return jsonify('Opperation Deleted'), 200



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

@app.route('/vaccine/update', methods=['POST', 'PUT'] )
def vaccine_update():
  post_data = request.get_json()
  vaccine_id = post_data.get("vaccine_id")
  if vaccine_id == None:
    return jsonify("ERROR: vaccine_id missing"), 400
  name = post_data.get('name')
  description = post_data.get('description')
  active = post_data.get('active')

  if active == None:
    active = True
    
    pet_type_data = None

    if vaccine_id != None:
      pet_type_data = db.session.query(VaccineInfo).filter(VaccineInfo.vaccine_id == vaccine_id).first()

    if pet_type_data:
      vaccine_id = pet_type_data.vaccine_id
      if name:
        pet_type_data.name = name
      if description is not None:
        pet_type_data.description = description
      if active is not None:
        pet_type_data.active = active

      db.session.commit()

      return jsonify('Vaccine Information Updated'), 200
    else:
      return jsonify("Vaccine Not Found"), 404
  else:
    return jsonify("ERROR: request must be in JSON format"), 400

@app.route('/vaccine/activate/<vaccine_id>', methods=['GET'] )
def vaccine_activate(vaccine_id):
  results = db.session.query(VaccineInfo).filter(VaccineInfo.vaccine_id == vaccine_id).first()
  results.active=True
  db.session.commit()
  return jsonify('Vaccine Activated'), 200

@app.route('/vaccine/deactivate/<vaccine_id>', methods=['GET'] )
def vaccine_deactivate(vaccine_id):
  results = db.session.query(VaccineInfo).filter(VaccineInfo.vaccine_id == vaccine_id).first()
  results.active=False
  db.session.commit()
  return jsonify('Vaccine Deactivated'), 200

@app.route('/vaccine/delete/<vaccine_id>', methods=['DELETE'] )
def vaccine_delete(vaccine_id):
  results = db.session.query(VaccineInfo).filter(VaccineInfo.vaccine_id == vaccine_id).first()
  db.session.delete(results)
  db.session.commit()
  return jsonify('Vaccine Deleted'), 200





if __name__ == '__main__':
  create_all()
  app.run(host='0.0.0.0', port="8089")