from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import requests
from analytics.models.location import * 

class Get_locations_based_on_analysis(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def post(self):

        try:
          
            #filtering locations based on "preferable living cost " which is provided by user..here a location will be selected if the avg_living_cost of that location is in the range of [preferable_living_cost-500 , preferable_living_cost+500]

            preferable_living_cost = request.json['preferable_living_cost']
            fields_of_interest = request.json['fields_of_interest']

            locations_based_on_living_cost = LocationModel.query.filter(LocationModel.avg_living_cost >= preferable_living_cost-500 , LocationModel.avg_living_cost <= preferable_living_cost+500).order_by(LocationModel.avg_living_cost.asc()).all()

            location_ids_based_on_preferable_living_cost=[]
            for location in locations_based_on_living_cost:
                location_ids_based_on_preferable_living_cost.append(location.id)
   

            #here "fields_of_interest" are sending to "Professor-Service" and and the "Professor-service" will return a list of "location_id" for those locations in which the professors live who has those area of interest"
            # so to to send "fields_of_interest" to "Professor-Service" ,we are converting this list to a json(or dictionary) format

            field_of_interest_dict={}
            field_of_interest_dict['fields_of_interest']=fields_of_interest #e.g. {'fields_of_interest':["field1","field2",...]}
            
            response = requests.post('http://localhost:5002/api/professors/get_location_ids_based_on_field_of_interest',json= field_of_interest_dict)

            location_id_dict=response.json()

            location_ids_based_on_field_of_interest = location_id_dict['location_ids']

            #So far, we got two list of location_ids for two type of analysis(one for "preferable living cost" and another one for "field of interest" ),Now we will suggest the user a list of location(aka "final_list_of_location_ids" ) merging these two type of analysis

            final_list_of_location_ids = list(set(location_ids_based_on_preferable_living_cost).intersection(set(location_ids_based_on_field_of_interest)))

            #Now we will find the details of each filtered locations
            suggestable_locations = LocationModel.query.filter(LocationModel.id.in_(final_list_of_location_ids)).all()

            suggestable_locations_details_dicts=[]

            for location in suggestable_locations:
                suggestable_locations_details_dicts.append(
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
                        'unemployment_rate': location.unemployment_rate

                   }

                )

            #sorting the suggested_locations based on living_cost,weather_comfort_index    

            sorted_list = sorted(suggestable_locations_details_dicts, key=lambda x: (x['avg_living_cost'], x['weather_comfort_index']))
    

            return jsonify(sorted_list)
        



        except Exception as e:
            print({"message":"exception occured in get_location_based_on_analysis"})
            print(e)
            return jsonify({"message":"exception occured in get_location_based_on_analysis"})      



