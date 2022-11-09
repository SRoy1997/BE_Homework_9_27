from flask import request, jsonify

from db import *
from models.clients import Clients
from models.pet_information import PetInformation


def pet_add():
  post_data = request.json
  
  name = post_data.get('name')
  age = post_data.get('age')
  pet_type = post_data.get('pet_type')
  owner_id = post_data.get('owner_id')
  active = post_data.get('active')

  add_pet(name, age, pet_type, owner_id, active)

  return jsonify("User created"), 201

def add_pet(name, age, pet_type, owner_id, active): 
  new_pet = PetInformation(name, age, pet_type, owner_id, active)
  
  db.session.add(new_pet)
  db.session.commit()

