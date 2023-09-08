from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import datetime

from analytics.models.location import * 
#this class is for adding new location info into database

class Add_locations(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:

            locations = request.json

            for location in locations:

                #checking if the location alra=eady exists in database or not
                old_location = LocationModel.query.filter_by(location_name=location['location_name'],state_name = location['state'],country_name=location['country']).first()

                if old_location:
                    continue
            

                new_location = LocationModel()
                new_location.location_name = location['location_name']
                new_location.state_name = location['state']
                new_location.country_name =  location['country']
                #new_location.area_type = request.json['area_type']
                new_location.avg_living_cost = location['cost_of_living']
                new_location.population = location['population']
                #new_location.public_transportation = request.json['public_transportation']
                new_location.avg_income = location['median_income']
                new_location.unemployment_rate = location['unemployment_rate']

                weather_comfort_index = location['weather_comfort_index'] #e.g weather_comfort_index  8.5 / 3.1
                summer_and_winter_comfort_index = weather_comfort_index.split(" / ")

                new_location.summer_comfort_index = summer_and_winter_comfort_index[0]
                new_location.winter_comfort_index = summer_and_winter_comfort_index[1]

                new_location.image = location['image_link']
                new_location.home_price = location['home_price']

                #for detailed info

                detailed_info = location['detailed_info']

                new_location.economic_details = detailed_info['ECONOMY']
                new_location.cost_of_living_details =detailed_info['COST OF LIVING']
                new_location.weather_details = detailed_info['WEATHER & CLIMATE']
                new_location.population_details = detailed_info['POPULATION']
                new_location.transportation_details = detailed_info['TRANSPORTATION']
                new_location.real_estate_details =detailed_info['REAL ESTATE']
                new_location.school_details = detailed_info['SCHOOLS']

                #print(new_location.json())


                db.session.add(new_location)
                db.session.commit()

            return {"message":"All locations added successfully"}
        except Exception as e:
            print({"message":"exception occured in add_locations"})
            print(e)
            return jsonify({"message":"exception occured in add_locations"})
