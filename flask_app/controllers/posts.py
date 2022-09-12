from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.post import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/recipes')
def recipes_dashboard():
    recipes = Recipe.get_all_posts()
    return render_template('/recipes.html', posts = recipes)
@app.route('/new')
def add_recipe():
    return render_template('new_recipe.html')
@app.route('/publish', methods=['POST'])
def publish():
    if request.form['name'] == '' or request.form['description'] == '' or request.form['instructions'] or request.form['date_made']:
        flash("All fields are required!")
        return redirect('/recipes')
    data = {
        'users_id': session['user'],
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_thirty': request.form['under_thirty'],
    }
    Recipe.save_recipe(data)
    return redirect('/wall')
@app.route('/delete', methods=['POST'])
def delete_post():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/recipes')
    data = {
        "id" : request.form['id']
    }
    Recipe.delete_recipe(data)
    return redirect('/recipes')