from flask import request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from analytics import db
from analytics import api
import requests
from analytics.models.location import * 
from sqlalchemy import cast, String, Float


from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


class Get_locations_based_on_analysis(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def post(self):

        try:
          
            #filtering locations based on "preferable living cost " which is provided by user..here a location will be selected if the avg_living_cost of that location is in the range of [preferable_living_cost-500 , preferable_living_cost+500]

            preferable_living_cost = request.json['preferable_living_cost']
            fields_of_interest = request.json['fields_of_interest']

            #converting "preferable_living_cost" to float

            # locations_based_on_living_cost = LocationModel.query.filter(float(LocationModel.avg_living_cost.split(' / ')[0]) >= preferable_living_cost-50 , float(LocationModel.avg_living_cost.split(' / ')[0])  <= preferable_living_cost+50).order_by(LocationModel.avg_living_cost.asc()).all()

            expr = func.split_part(LocationModel.avg_living_cost, ' / ', 1)

            locations_based_on_living_cost = (
                LocationModel.query
                .filter(
                    cast(expr, Float) >= preferable_living_cost-50,
                    cast(expr, Float) <= preferable_living_cost+50
                )
                .order_by(cast(expr, Float).asc())
                .all()
            )

            location_ids_based_on_preferable_living_cost=[]
            for location in locations_based_on_living_cost:
                location_ids_based_on_preferable_living_cost.append(location.id)
   

            #here "fields_of_interest" are sending to "Professor-Service" and and the "Professor-service" will return a list of "location_id" for those locations in which the professors live who has those area of interest"
            # so to to send "fields_of_interest" to "Professor-Service" ,we are converting this list to a json(or dictionary) format

            field_of_interest_dict={}
            field_of_interest_dict['fields_of_interest']=fields_of_interest #e.g. {'fields_of_interest':["field1","field2",...]}
            
            response = requests.post('http://localhost:5002/api/professors/get_location_ids_based_on_field_of_interest',json= field_of_interest_dict)

            location_id_dict=response.json()


            location_ids_based_on_field_of_interest = location_id_dict.get('location_ids')


            #So far, we got two list of location_ids for two type of analysis(one for "preferable living cost" and another one for "field of interest" ),Now we will suggest the user a list of location(aka "final_list_of_location_ids" ) merging these two type of analysis

            print(location_ids_based_on_field_of_interest)
            print(location_ids_based_on_preferable_living_cost)
            suggestable_locations_details_dicts=[]


            if location_ids_based_on_field_of_interest and location_ids_based_on_preferable_living_cost:
                final_list_of_location_ids = list(set(location_ids_based_on_field_of_interest) & set(location_ids_based_on_preferable_living_cost))

      
                #Now we will find the details of each filtered locations
                suggestable_locations = LocationModel.query.filter(LocationModel.id.in_(final_list_of_location_ids)).all()

                suggestable_locations_details_dicts=[]

                for location in suggestable_locations:
                    suggestable_locations_details_dicts.append(location.json())

                #sorting the suggested_locations based on living_cost,weather_comfort_index    

                sorted_list = sorted(suggestable_locations_details_dicts, key=lambda x: (x['avg_living_cost']))
        

                return jsonify(sorted_list)
            



        except Exception as e:
            print({"message":"exception occured in get_location_based_on_analysis"})
            print(e)
            return jsonify({"message":"exception occured in get_location_based_on_analysis"})      



