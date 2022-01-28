from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Worksheet:
    db = 'ALEz_schema'

    def __init__(self, data):
        self.id = data['id']
        self.claim_number = data['claim_number']
        self.date_of_loss = data['date_of_loss']
        self.normal_housing = data['normal_housing']
        self.normal_utilities_heat = data['normal_utilities_heat']
        self.normal_utilities_electricity = data['normal_utilities_electricity']
        self.normal_utilities_water = data['normal_utilities_water']
        self.normal_food_residence = data['normal_food_residence']
        self.normal_food_restaurant = data['normal_food_restaurant']
        self.normal_food_other = data['normal_food_other']
        self.normal_services_laundry = data['normal_services_laundry']
        self.normal_services_dry_cleaning = data['normal_services_dry_cleaning']
        self.normal_services_other = data['normal_services_other']
        self.normal_transportation_gas = data['normal_transportation_gas']
        self.normal_transportation_taxi = data['normal_transportation_taxi']
        self.normal_transportation_rideshare = data['normal_transportation_rideshare']
        self.normal_storage_unit = data['normal_storage_unit']
        self.normal_storage_moving = data['normal_storage_moving']
        self.normal_storage_other = data['normal_storage_other']
        self.total_NLE = data['total_NLE']
        self.addtl_housing = data['addtl_housing']
        self.addtl_utilities_heat = data['addtl_utilities_heat']
        self.addtl_utilities_electricity = data['addtl_utilities_electricity']
        self.addtl_utilities_water = data['addtl_utilities_water']
        self.addtl_food_residence = data['addtl_food_residence']
        self.addtl_food_restaurant = data['addtl_food_restaurant']
        self.addtl_food_other = data['addtl_food_other']
        self.addtl_services_laundry = data['addtl_services_laundry']
        self.addtl_services_dry_cleaning = data['addtl_services_dry_cleaning']
        self.addtl_services_other = data['addtl_services_other']
        self.addtl_transportation_gas = data['addtl_transportation_gas']
        self.addtl_transportation_taxi = data['addtl_transportation_taxi']
        self.addtl_transportation_rideshare = data['addtl_transportation_rideshare']
        self.addtl_storage_unit = data['addtl_storage_unit']
        self.addtl_storage_moving = data['addtl_storage_moving']
        self.addtl_storage_other = data['addtl_storage_other']
        self.total_AE = data['total_AE']
        self.total_ALE_claim = data['total_ALE_claim']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.insured = None

# get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM worksheets JOIN users ON users.id = user_id;"
        worksheets_from_db = connectToMySQL(cls.db).query_db(query)
        print(worksheets_from_db)
        worksheets = []
        for worksheet in worksheets_from_db:
            #1 make a paintings object
            this_worksheet = cls(worksheet)
            #2 make a dictionary for artist info
            insured_info = {
                'id':  worksheet ['users.id'],
                'f_name':  worksheet ['f_name'],
                'l_name':  worksheet ['l_name'],
                'email':  worksheet ['email'],
                'password':  worksheet ['password'],
                'created_at':  worksheet ['users.created_at'],
                'updated_at':  worksheet ['users.updated_at'],
            }
            #3 make a user object
            this_user = user.User(insured_info)
            #4 set that user object as an attribute of the painting
            this_worksheet.insured = this_user
            #5 add the painting object to the list paintings
            worksheets.append(this_worksheet)
        return worksheets

# get one
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM worksheets JOIN users ON users.id = user_id WHERE worksheets.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        #1 make a sightings object
        this_worksheet = cls(results[0])
        #2 make a dictionary for artist info
        insured_info = {
            'id':  results[0]['users.id'],
            'f_name':  results[0] ['f_name'],
            'l_name':  results[0] ['l_name'],
            'email':  results[0] ['email'],
            'password':  results[0] ['password'],
            'created_at':  results[0] ['users.created_at'],
            'updated_at':  results[0] ['users.updated_at'],
            }
        #3 make a user object
        this_user = user.User(insured_info)
        #4 set that user object as an attribute of the painting
        this_worksheet.insured = this_user
        #5 return the sighting object
        return this_worksheet

# create worksheet
    @classmethod
    def save(cls, data):
        query = "INSERT INTO worksheets (claim_number, date_of_loss, normal_housing, normal_utilities_heat, normal_utilities_electricity, normal_utilities_water, normal_food_residence, normal_food_restaurant, normal_food_other, normal_services_laundry, normal_services_dry_cleaning, normal_services_other, normal_transportation_gas, normal_transportation_taxi, normal_transportation_rideshare, normal_storage_unit, normal_storage_moving, normal_storage_other, total_NLE, addtl_housing, addtl_utilities_heat, addtl_utilities_electricity, addtl_utilities_water, addtl_food_residence, addtl_food_restaurant, addtl_food_other, addtl_services_laundry, addtl_services_dry_cleaning, addtl_services_other, addtl_transportation_gas, addtl_transportation_taxi, addtl_transportation_rideshare, addtl_storage_unit, addtl_storage_moving, addtl_storage_other, total_AE, total_ALE_claim, user_id) VALUES (%(claim_number)s,%(date_of_loss)s,%(normal_housing)s,%(normal_utilities_heat)s,%(normal_utilities_electricity)s,%(normal_utilities_water)s,%(normal_food_residence)s,%(normal_food_restaurant)s,%(normal_food_other)s,%(normal_services_laundry)s,%(normal_services_dry_cleaning)s,%(normal_services_other)s,%(normal_transportation_gas)s,%(normal_transportation_taxi)s,%(normal_transportation_rideshare)s,%(normal_storage_unit)s,%(normal_storage_moving)s,%(normal_storage_other)s,%(total_NLE)s, %(addtl_housing)s,%(addtl_utilities_heat)s,%(addtl_utilities_electricity)s,%(addtl_utilities_water)s,%(addtl_food_residence)s,%(addtl_food_restaurant)s,%(addtl_food_other)s,%(addtl_services_laundry)s,%(addtl_services_dry_cleaning)s,%(addtl_services_other)s,%(addtl_transportation_gas)s,%(addtl_transportation_taxi)s,%(addtl_transportation_rideshare)s,%(addtl_storage_unit)s,%(addtl_storage_moving)s,%(addtl_storage_other)s,%(total_AE)s,%(total_ALE_claim)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

# update worksheet
    @classmethod
    def update(cls, data):
        query = "UPDATE worksheets SET claim_number=%(claim_number)s, date_of_loss=%(date_of_loss)s, normal_housing=%(normal_housing)s, normal_utilities_heat=%(normal_utilities_heat)s,normal_utilities_electricity=%(normal_utilities_electricity)s,normal_utilities_water=%(normal_utilities_water)s,normal_food_residence=%(normal_food_residence)s,normal_food_restaurant=%(normal_food_restaurant)s,normal_food_other=%(normal_food_other)s,normal_services_laundry=%(normal_services_laundry)s,normal_services_dry_cleaning=%(normal_services_dry_cleaning)s,normal_services_other=%(normal_services_other)s,normal_transportation_gas=%(normal_transportation_gas)s,normal_transportation_taxi=%(normal_transportation_taxi)s,normal_transportation_rideshare=%(normal_transportation_rideshare)s,normal_storage_unit=%(normal_storage_unit)s,normal_storage_moving=%(normal_storage_moving)s,total_NLE=%(total_NLE)s,   addtl_housing=%(addtl_housing)s, addtl_utilities_heat=%(addtl_utilities_heat)s,addtl_utilities_electricity=%(addtl_utilities_electricity)s,addtl_utilities_water=%(addtl_utilities_water)s,addtl_food_residence=%(addtl_food_residence)s,addtl_food_restaurant=%(addtl_food_restaurant)s,addtl_food_other=%(addtl_food_other)s,addtl_services_laundry=%(addtl_services_laundry)s,addtl_services_dry_cleaning=%(addtl_services_dry_cleaning)s,addtl_services_other=%(addtl_services_other)s,addtl_transportation_gas=%(addtl_transportation_gas)s,addtl_transportation_taxi=%(addtl_transportation_taxi)s,addtl_transportation_rideshare=%(addtl_transportation_rideshare)s,addtl_storage_unit=%(addtl_storage_unit)s,addtl_storage_moving=%(addtl_storage_moving)s,total_AE=%(total_AE)s, total_ALE_claim=%(total_ALE_claim)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

# delete worksheet
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM worksheets WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

# worksheet validation
    @staticmethod
    def validate_worksheet(worksheet):
        is_valid = True
        print()
        if len(worksheet['claim_number']) < 2:
            is_valid = False
            flash("Please enter a valid claim number", "worksheet")
        if worksheet['date_of_loss'] == "":
            is_valid = False
            flash("Please enter a date of the loss", "worksheet")
        if float(worksheet['addtl_food_residence']) > 0 and float(worksheet['normal_food_residence']) == 0:
            is_valid = False
            flash("Please enter your normal food expense for the duration of your displacement", "worksheet")
        if float(worksheet['total_ALE_claim']) == 0:
            is_valid = False
            flash("You must incur Additional expenses in order to file a claim", "worksheet")
        if float(worksheet['total_ALE_claim']) < 0:
            is_valid = False
            flash("You must have incurred more Additional expenses than Normal Expenses to file a claim", "worksheet")

        return is_valid
