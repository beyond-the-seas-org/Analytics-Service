from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import requests

from analytics.models.location import *

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Get_professor_Short_Details_of_a_Location(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self,user_id,location_id):

        try:
            token = request.headers.get('Authorization')
            if token and token.startswith('Bearer '):
               access_token = token.split(' ')[1]

            response = requests.get(f'http://localhost:5002/api/professors/{user_id}/{location_id}/get_location_based_professors',  headers={'Authorization': f'Bearer {access_token}'})
            
            return response.json()

        except Exception as e:
            print({"message":"exception occured in get_professors_of_a_location"})
            print(e)
            return jsonify({"message":"exception occured in get_professors_of_a_location"})      



