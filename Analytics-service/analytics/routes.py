from analytics.apis.Add_location import *
from analytics.apis.Get_locations_based_on_analysis import *
from analytics.apis.Get_professors_short_details_of_a_location import *
from analytics.apis.Get_location_id import *
from analytics.apis.Get_location_info import *
from analytics.apis.Get_all_locations import *



Newsfeed = api.namespace('api/analytics')

Newsfeed.add_resource(Add_location,'/add_location') 
Newsfeed.add_resource(Get_locations_based_on_analysis,'/get_locations_based_on_analysis') 
Newsfeed.add_resource(Get_professor_Short_Details_of_a_Location,'/<location_id>/get_professors_short_details') 
Newsfeed.add_resource(Get_location_id,'/get_location_id') 
Newsfeed.add_resource(Get_location_info,'/<int:location_id>/get_location_info') 
Newsfeed.add_resource(Get_all_locations,'/get_all_locations') 

