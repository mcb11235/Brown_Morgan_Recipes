from flask_app import app
from flask_app.models.user import User
from flask_app.controllers import users
from flask_app.models.post import Recipe
from flask_app.controllers import posts
if __name__ == "__main__":
    app.run(debug=True)