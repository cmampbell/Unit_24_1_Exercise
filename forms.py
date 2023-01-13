from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange, AnyOf

class NewPetForm(FlaskForm):
    '''Form class for users to add pets to the adoption database'''
    name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired(), AnyOf(values=['Dog', 'Cat', 'Porcupine'])])
    photo_url = URLField('Photo Url', validators=[URL()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
    '''Form class for users to edit pets in the adoption database'''
    photo_url = URLField('Photo Url', validators=[URL()])
    notes = StringField('Notes')
    available = BooleanField()