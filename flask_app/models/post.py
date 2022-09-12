from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'recipe_schema'
class Recipe:
    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.description = data['description'],
        self.instructions = data['instructions'],
        self.date_made = data['date_made'],
        self.under_thirty = data['under_thirty'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at'],
        self.users_id = data['users_id'],
        self.first_name=data['first_name'],
        self.last_name=data['last_name']
    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, users_id, date_made, description, instructions, under_thirty) VALUES ( %(name)s , %(users_id)s, %(date_made)s, %(description)s, %(instructions)s, %(under_thirty)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM recipes JOIN users ON users_id=users.id "
        recipes = []
        results = connectToMySQL(schema_name).query_db(query)
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users_id=users.id WHERE id=%(id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        return cls(results[0])
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(schema_name).query_db(query, data)