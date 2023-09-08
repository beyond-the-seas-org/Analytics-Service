from app import db

class LocationModel(db.Model):

    """
    primary key: id
    other fields: location_name(basically city name),area_type(rural or city),state_name,country_name,avg_living_cost(e.g 2500-3000$),weather,public_transportation,population,avg_income,summer_comfort_index(comfort_index is a measurement which indicate how much the weather is comfortable to live),winter_comfort_index,unemployment_rate(in %)
    """

    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    location_name = db.Column(db.String(50), nullable=False)
    area_type = db.Column(db.String(50))
    state_name = db.Column(db.String(50))
    country_name = db.Column(db.String(30), nullable=False)
    avg_living_cost = db.Column(db.String(20))
    public_transportation = db.Column(db.String(100))
    population = db.Column(db.String(20))
    avg_income = db.Column(db.String(20))
    summer_comfort_index = db.Column(db.String(20)) 
    winter_comfort_index = db.Column(db.String(20))
    unemployment_rate = db.Column(db.String(20))
    image = db.Column(db.String(250))
    #extra added
    home_price = db.Column(db.String(20))
    economic_details = db.Column(db.String(1000))
    cost_of_living_details = db.Column(db.String(1000))
    weather_details = db.Column(db.String(1000))
    population_details = db.Column(db.String(1000))
    transportation_details = db.Column(db.String(1000))
    real_estate_details = db.Column(db.String(1000))
    school_details = db.Column(db.String(1000))





    # create a json method
    def json(self):
        return {
            'id': self.id,
            'location_name': self.location_name,
            'area_type': self.area_type,
            'state_name' :self.state_name,
            'country_name': self.country_name,
            'avg_living_cost': self.avg_living_cost,
            'public_transportation':self.public_transportation,
            'avg_income':self.avg_income,
            'population':self.population,
            'summer_comfort_index':self.summer_comfort_index,
            'winter_comfort_index':self.winter_comfort_index,
            'unemployment_rate': self.unemployment_rate,
            "image" : self.image,

            "home_price" : self.home_price,
            "economic_details" : self.economic_details,
            "cost_of_living_details" : self.cost_of_living_details,
            "weather_details" : self.weather_details,
            "population_details" : self.population_details,
            "transportation_details" : self.transportation_details,
            "real_estate_details" : self.real_estate_details,
            "school_details" : self.school_details


        }