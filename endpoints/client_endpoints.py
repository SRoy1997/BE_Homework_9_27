from flask import request, jsonify

from db import *
from models.clients import Clients


def client_add(request):
  post_data = request.json
  
  first_name = post_data.get('first_name')
  last_name = post_data.get('last_name')
  email = post_data.get('email')
  phone = post_data.get('phone')
  street_address = post_data.get('street_address')
  city = post_data.get('city')
  state = post_data.get('state')
  postal_code = post_data.get('postal_code')
  active = post_data.get('active')

  add_client(first_name, last_name, email, phone, street_address, city, state, postal_code, active)

  return jsonify("User created"), 201

def add_client(first_name, last_name, email, phone, street_address, city, state, postal_code, active): 
  new_client = Clients(first_name, last_name, email, phone, street_address, city, state, postal_code, active)
  
  db.session.add(new_client)
  db.session.commit()

