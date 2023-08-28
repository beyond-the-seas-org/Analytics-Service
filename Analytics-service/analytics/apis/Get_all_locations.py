from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
from analytics.models.location import * 

class Get_all_locations(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def get(self):

        try:
          
            all_locations = LocationModel.query.filter(LocationModel.id <= 6).all() 

            all_locations_details_dicts=[]
            for location in all_locations:
                all_locations_details_dicts.append(
                   {
                        'id': location.id,
                        'location_name': location.location_name,
                        'state_name':location.state_name,
                        'area_type': location.area_type,
                        'country_name': location.country_name,
                        'avg_living_cost': location.avg_living_cost,
                        'public_transportation':location.public_transportation,
                        'avg_income':location.avg_income,
                        'population':location.population,
                        'summer_comfort_index':location.summer_comfort_index,
                        'winter_comfort_index':location.winter_comfort_index,
                        'weather_comfort_index':(location.summer_comfort_index + location.winter_comfort_index)/2,
                        'unemployment_rate': location.unemployment_rate,
                        'image_link':location.image

                   }

                )

            #sorting the all_locations based on living_cost,weather_comfort_index    

            sorted_list = sorted(all_locations_details_dicts, key=lambda x: (x['avg_living_cost'], x['weather_comfort_index']))
            return jsonify(sorted_list)
        



        except Exception as e:
            print({"message":"exception occured in get_all_locations"})
            print(e)
            return jsonify({"message":"exception occured in get_all_locations"})      



