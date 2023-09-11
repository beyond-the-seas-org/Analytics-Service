from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
from analytics.models.location import * 

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401

class Get_all_locations(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self):

        try:
          
            all_locations = LocationModel.query.all() 

            all_locations_details_dicts=[]
            for location in all_locations:
                all_locations_details_dicts.append(location.json())
                

            #sorting the all_locations based on living_cost,weather_comfort_index    

            sorted_list = sorted(all_locations_details_dicts, key=lambda x: (x['avg_living_cost']))
            return jsonify(sorted_list)
        



        except Exception as e:
            print({"message":"exception occured in get_all_locations"})
            print(e)
            return jsonify({"message":"exception occured in get_all_locations"})      



