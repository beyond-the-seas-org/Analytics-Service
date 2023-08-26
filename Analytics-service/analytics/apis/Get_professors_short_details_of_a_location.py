from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import requests

from analytics.models.location import * 

class Get_professor_Short_Details_of_a_Location(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self,location_id):

        try:

            response = requests.get(f'http://localhost:5002/api/professors/{location_id}/get_location_based_professors')
            return response.json()

        except Exception as e:
            print({"message":"exception occured in get_professors_of_a_location"})
            print(e)
            return jsonify({"message":"exception occured in get_professors_of_a_location"})      



