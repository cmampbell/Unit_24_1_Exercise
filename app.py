from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ItsAWonderfulLife'
app.config['DEBUG_TB_INTERCEPT-REDIRECTS'] = False
# app.run(debug=True)
debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    # pets = Pet.query.all()
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    form = PetForm()
    
    return render_template('add_pet.html', form=form)