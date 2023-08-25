from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import datetime

from analytics.models.location import * 
#this class is for adding new location info into database

class Add_location(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            new_location = LocationModel()
            new_location.location_name = request.json['location_name']
            new_location.country_name = request.json['country_name']
            new_location.area_type = request.json['area_type']
            new_location.avg_living_cost = request.json['avg_living_cost']
            new_location.population = request.json['population']
            new_location.public_transportation = request.json['public_transportation']
            new_location.avg_income = request.json['avg_income']
            new_location.unemployment_rate = request.json['unemployment_rate']
            new_location.summer_comfort_index = request.json['summer_comfort_index']
            new_location.winter_comfort_index = request.json['winter_comfort_index']


            db.session.add(new_location)
            db.session.commit()

            # new_post_id = db.session.query(func.max(PostModel.id)).scalar() #return the highest id of the post table
            # return jsonify({"post_id":new_post_id})
            return new_location.json()
        except Exception as e:
            print({"message":"exception occured in add_location"})
            print(e)
            return jsonify({"message":"exception occured in add_location"})
