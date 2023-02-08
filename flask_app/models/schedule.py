from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'equipment_schema'
#schedule_id, technician, discipline, start_time, end_time, notes, created_by, project_manager
class Schedule:
    def __init__(self, data):
        self.scheudle_id = data['schedule_id'],
        self.technician = data['technician'],
        self.discipline = data['discipline'],
        self.start_time = data['start_time'],
        self.end_time = data['end_time'],
        self.notes = data['notes'],
        self.created_by = data['created_by'],
        self.project_manager = data['project_manager']
    @classmethod
    def save_project(cls, data):
        query = "INSERT INTO schedules (schedule_id, technician, discipline, start_time, end_time, notes, created_by, project_manager) VALUES (%(schedule_id)s,%(technician)s,%(discipline)s,%(start_time)s,%(end_time)s,%(notes)s,%(created_by)s,%(project_manager)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_project(cls, data):
        query = "UPDATE schedules SET schedule_id=%(schedule_id)s,technician=%(technician)s,discipline=%(discipline)s,start_time=%(start_time)s,end_time=%(end_time)s,notes=%(notes)s WHERE projectid=%(projectid)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM schedules"
        schedules = []
        results = connectToMySQL(schema_name).query_db(query)
        for schedule in results:
            schedules.append(cls(schedule))
        return schedules
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM schedules WHERE schedule_id=%(schedule_id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        print(results)
        return cls(results[0])
    @classmethod
    def get_by_user(cls, data):
        query = "SELECT * FROM schedules WHERE project_manager=%(project_manager)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        return cls(results[0])
    @classmethod
    def delete_schedule(cls, data):
        query = "DELETE FROM schedules WHERE schedule_id=%(schedule_id)s"
        return connectToMySQL(schema_name).query_db(query, data)