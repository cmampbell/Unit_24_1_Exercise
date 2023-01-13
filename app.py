from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'AdoptDontShop'
app.config['DEBUG_TB_INTERCEPT-REDIRECTS'] = False
# app.run(debug=True)
debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    '''Renders home page for adoption agency'''
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    '''Renders new pet form for adoption agency. If form submit and validated,
    get form data create new pet instance, and add pet to the database'''
    form = NewPetForm()
    if form.validate_on_submit():
        data = form.data
        new_pet = Pet(name=data['name'], species=data['species'], photo_url = data['photo_url'], age=data['age'], notes=data['notes'])

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    '''Render the detail page for the pet, with edit form. If form submit
    and validated, update the pet info in the database and reload the page'''

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.data['photo_url']
        pet.notes = form.data['notes']
        pet.available = form.data['available']

        db.session.add(pet)
        db.session.commit()

        return redirect(f'/{pet.id}')
    else:
        return render_template('pet_details.html', pet=pet, form=form)
