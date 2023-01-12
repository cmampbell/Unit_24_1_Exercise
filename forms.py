from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField
from wtforms.validators import DataRequired, URL

class PetForm(FlaskForm):
    '''Form class for users to add pets to the adoption database'''
    name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    photo_url = URLField('Photo Url', validators=[URL()])
    age = IntegerField('Age')
    notes = StringField('Notes')