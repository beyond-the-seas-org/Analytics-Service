from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api

from analytics.models.location import * 

#this API will take "location_name,state_name and country_name" from "Professor-service" and will return the "location_id" to the "Professor-service"

class Get_location_id(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            location_name = request.json['location_name']
            state_name = request.json['state_name']
            country_name = request.json['country_name']

            location_id = LocationModel.query.filter(LocationModel.location_name == location_name,LocationModel.state_name == state_name,LocationModel.country_name == country_name).first().id

            return jsonify({'location_id':location_id})

        except Exception as e:
            print({"message":"exception occured in get_location_id"})
            print(e)
            return jsonify({"message":"exception occured in get_location_id"})
