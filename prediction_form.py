
from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, FloatField, SubmitField, SelectField

class PredictionForm(FlaskForm):
    # field_1 = StringField(label = 'Field1',validators=[validators.Length(min=4, max=25)])
    age = FloatField(label ='Age', render_kw = {'class': 'form-control'})
    daily_average_of_betal_quids = FloatField(label = 'Daily average of betel quids', render_kw = {'class': 'form-control'})
    has_arecanut_as_an_ingrediant = SelectField(label = 'Use Arecanut as an ingrediant', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    average_years_of_smoking = FloatField(label ='Average year of smoking', render_kw = {'class': 'form-control'})
    sex = SelectField(label = 'Sex', choices = ['Male', 'Female'], render_kw = {'class': 'form-control'})
    has_burning_sensation = SelectField(label = 'Has burning sensation', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    has_difficulty_in_mouth_opening = SelectField(label = 'Has difficulty in mouth opening', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    has_ulceration = SelectField(label = 'Has ulceration in mouth', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    has_medical_history_of_hypertension = SelectField(label = 'Has medical history of hypertension', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    is_toungue_movement_restricted = SelectField(label = 'Is toungue movement restricted', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    has_prescribed_steroid_intra_lesional_injection = SelectField(label = 'Has prescribeed Steroid Intra Lesion Injection', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    has_prescribed_pentoxyphylline = SelectField(label = 'Has prescribed Pentoxyphylline', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    is_prescribed_antifungals = SelectField(label = 'Has prescribeed Antifungals', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    submit = SubmitField('Predict', render_kw = {'class': 'btn btn-primary'})

    
