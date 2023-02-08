from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'equipment_schema'
class Equipment:
    def __init__(self, data):
        self.id = data['id'],
        self.serial_number = data['serial_number'],
        self.calibration_procedure = data['calibration_procedure'],
        self.item = data['item'],
        self.category = data['category'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.users_id = data['users_id'],
        self.test_method = data['test_method'],
        self.acquired_date = data['acquired_date'],
        self.purchase_price = data['purchase_price'],
        self.calibration_date = data['calibration_date'],
        self.frequency = data['frequency'],
        self.calibration_due = data['calibration_due'],
        self.location = data['location'],
        self.owner = data['owner']
    @classmethod
    def save_equipment(cls, data):
        query = "INSERT INTO equipment (users_id,serial_number,calibration_procedure,item,category,test_method,acquired_date,purchase_price,calibration_date,frequency,calibration_due,location,owner) VALUES ( %(users_id)s,%(serial_number)s , %(calibration_procedure)s, %(item)s, %(category)s, %(test_method)s, %(acquired_date)s,%(purchase_price)s,%(calibration_date)s,%(frequency)s,%(calibration_due)s,%(location)s,%(owner)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_equipment(cls, data):
        query = "UPDATE equipment SET users_id=%(users_id)s,serial_number=%(serial_number)s,calibration_procedure=%(calibration_procedure)s,item=%(item)s,category=%(category)s,test_method=%(test_method)s,acquired_date=%(acquired_date)s,purchase_price=%(purchase_price)s,calibration_date=%(calibration_date)s,frequency=%(frequency)s,calibration_due=%(calibration_due)s,location=%(location)s,owner=%(owner)s WHERE id=%(id)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM equipment JOIN users ON users_id=users.id "
        equipments = []
        results = connectToMySQL(schema_name).query_db(query)
        for equipment in results:
            equipments.append(cls(equipment))
        return equipments
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM equipment WHERE id=%(id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        print(results)
        return cls(results[0])
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM equipment WHERE id=%(id)s"
        return connectToMySQL(schema_name).query_db(query, data)