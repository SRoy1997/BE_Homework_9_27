from flask import request, jsonify

from db import *
from models.clients import Clients
from models.pet_information import PetInformation


def opperation_add():
  post_data = request.json
  
  name = post_data.get('name')
  description = post_data.get('description')
  active = post_data.get('active')

  add_opperation(name, description, active)

  return jsonify("Opperation created"), 201

def add_opperation(name, description, active): 
  new_opperation = PetInformation(name, description, active)
  
  db.session.add(new_opperation)
  db.session.commit()

