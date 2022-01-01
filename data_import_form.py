
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
class DataImportForm(FlaskForm):
    field_1 = StringField('Field1')
    field_2 = StringField('Field2')
    submit = SubmitField('Import Data')

    
