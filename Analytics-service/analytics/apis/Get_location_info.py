from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api

from analytics.models.location import * 

#this API will take "Location_id" from "Professor-service" and will return the "location_name,state_name and country name" to the "Professor-service"

class Get_location_info(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self,location_id):

        try:          
            location = LocationModel.query.get(location_id)
            return jsonify(location.json())

        except Exception as e:
            print({"message":"exception occured in get_location_id"})
            print(e)
            return jsonify({"message":"exception occured in get_location_id"})
