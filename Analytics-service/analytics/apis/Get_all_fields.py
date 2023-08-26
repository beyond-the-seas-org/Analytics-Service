from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import requests
from analytics.models.location import * 

class Get_all_fields(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

   #this api will get "all_field_names" from "Professor Service" 
    def get(self):

        try:

            response = requests.get('http://localhost:5002/api/professors/get_all_fields')
            fields_json=response.json()
            return fields_json

        except Exception as e:
            print({"message":"exception occured in get_all_fields"})
            print(e)
            return jsonify({"message":"exception occured in get_all_fields"})      



