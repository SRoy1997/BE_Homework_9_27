import endpoints
from flask import request, Response, Blueprint

client = Blueprint('clients', __name__)

@client.route("/client/add", methods=["POST"])
def client_add() -> Response:
    return endpoints.client_add(request)