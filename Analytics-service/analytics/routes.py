from analytics.apis.Add_locations import *
from analytics.apis.Get_locations_based_on_analysis import *
from analytics.apis.Get_professors_short_details_of_a_location import *
from analytics.apis.Get_location_id import *
from analytics.apis.Get_location_info import *
from analytics.apis.Get_all_locations import *
from analytics.apis.Get_all_fields import *
from analytics.apis.Add_university_location import *



Namespace = api.namespace('api/analytics')

Namespace.add_resource(Add_locations,'/add_locations') 
Namespace.add_resource(Get_locations_based_on_analysis,'/get_locations_based_on_analysis') 
Namespace.add_resource(Get_professor_Short_Details_of_a_Location,'/<location_id>/get_professors_short_details') 
Namespace.add_resource(Get_location_id,'/get_location_id') 
Namespace.add_resource(Get_location_info,'/<int:location_id>/get_location_info') 
Namespace.add_resource(Get_all_locations,'/get_all_locations') 
Namespace.add_resource(Get_all_fields,'/get_all_fields') 
Namespace.add_resource(Add_university_location,'/add_university_location') #this API will not be used in future (may be) 

