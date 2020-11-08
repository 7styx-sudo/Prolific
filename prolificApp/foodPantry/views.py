from flask import Flask, Blueprint, render_template

foodPantry_app = Blueprint('foodPantry', __name__)

@foodPantry_app.route('/')
def index():
	return "landing page"
@foodPantry_app.route('/about')
def about():
	return render_template('About.html')

@foodPantry_app.route('/directory')
def directory():
	return render_template('Directory.html')

@foodPantry_app.route('/food pantry profile')
def fpProfile():
	return render_template('Food pantry profile.html') 

