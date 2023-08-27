from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import datetime



from analytics.models.location import * 
#I think this API will not be used in future

class Add_university_location(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
            universities = request.json

            for universitiy in universities:

                location = universitiy["location"]
                if(location == "Location not found"):
                    continue
                location_attributes = location.split(",")
                location_name = location_attributes[0]
                state_name = location_attributes[1].lstrip()
                country_name = location_attributes[len(location_attributes)-1].lstrip()

                #Adding the location into database 
                new_location = LocationModel()
                new_location.location_name = location_name
                new_location.state_name = state_name
                new_location.country_name = country_name
            
                db.session.add(new_location)
                db.session.commit()

            return jsonify({"message":"All locations added successfully"})
        except Exception as e:
            print({"message":"exception occured in add_university_location"})
            print(e)
            return jsonify({"message":"exception occured in add_university_location"})
