from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api

from analytics.models.location import * 

#this API will take "Location_id" from "Professor-service" and will return the "location_name,state_name and country name" to the "Professor-service"

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Get_location_info(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self,location_id):

        try:          
            location = LocationModel.query.get(location_id)
            return jsonify(location.json())

        except Exception as e:
            print({"message":"exception occured in get_location_id"})
            print(e)
            return jsonify({"message":"exception occured in get_location_id"})
