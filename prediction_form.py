
from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField

class PredictionForm(FlaskForm):
    age = FloatField(label ='Age', render_kw = {'class': 'form-control'})

    sex = SelectField(label = 'Sex', choices = ['Male', 'Female'], render_kw = {'class': 'form-control'})

    has_burning_sensation = SelectField(label = 'Has burning sensation', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})

    daily_average_of_betal_quids = FloatField(label = 'Daily average of betel quids', render_kw = {'class': 'form-control'})

    average_years_of_betel_consumption =  FloatField(label = 'Average years of betel consumption', render_kw = {'class': 'form-control'})

    betel_ingrediants = SelectMultipleField(label = 'Betal Ingrediants', choices = [('none', 'None'), ('betel', 'Betel'),
        ('arecanut', 'Arecanut'), ('lime','Lime'), ('tobacco', 'Tobacco')], render_kw = {'class': 'form-control'})

    daily_average_of_smoking_frequency = FloatField(label = 'Daily average of smoking frequency', render_kw = {'class': 'form-control'})

    average_years_of_smoking = FloatField(label ='Average year of smoking', render_kw = {'class': 'form-control'})

    smoking_type = SelectMultipleField(label = 'Smoking type', choices = [('none', 'None'), ('cigarettes', 'Cigarettes'),
        ('beedi', 'Beedi'), ('ganja','Ganja')], render_kw = {'class': 'form-control'})

    alchohol_type = SelectMultipleField(label = 'Alchohol type', choices = [('none', 'None'), ('arrack', 'Arrack'),
        ('beer', 'Beer'), ('vodka', 'Vodka')], render_kw = {'class': 'form-control'})

    has_difficulty_in_mouth_opening = SelectField(label = 'Has difficulty in mouth opening', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
    
    is_toungue_movement_restricted = SelectField(label = 'Is toungue movement restricted', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})

    is_patch_present = SelectField(label = 'Is patch present', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})

    has_depapilation_on_lips = SelectField(label = 'Has depapilation on lips', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})

    hemoglobin_level = FloatField(label ='Hemoglobin level', render_kw = {'class': 'form-control'})

    medical_history = SelectMultipleField(label = 'Medical History', choices = [('none','None'),
        ('hypertension', 'Hypertension'), ('diabetes', 'Diabetes'), ('heart_disease', 'Heart Diseases'),
        ('respiratory_disease', 'Respiratory Diseases'), ('dermatological_problem', 'Dermatological Problem'),
        ('gi_problem', 'GI Problem'), ('malnutrition_problem', 'Malnutrition Problem'), ('depression', 'Depression'),
        ('other', 'Other')], render_kw = {'class': 'form-control'})
   
    fibrous_bands = SelectMultipleField(label = 'Fibrous Bands', choices = [('none', 'None'),
        ('faucal_area', 'Faucal Area'), ('buccal_mucosa','Buccal Mucosa'), ('buccal_lips', 'Buccal Lips')], render_kw = {'class': 'form-control'})
   
    has_leukoplakia = SelectField(label = 'Has Leukoplakia', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
   
    has_erythroplakia = SelectField(label = 'Has Erythroplakia', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})

    has_candida = SelectField(label = 'Has Candida', choices = [('1','Yes'),('0','No')], coerce = int, render_kw = {'class': 'form-control'})
   
    initial_dignosis = SelectMultipleField(label = "Initial Diagnosis", choices = [('none', 'None'),('osf_with_mild_to_moderate_dysplsia', 'OSF with mild to moderate dysplsia'),
        ('osf_with_severe_dysplasia', 'OSF with severe dysplasia'), ('carcinoma_in_situ_in_bac_of_OSF', 'Carcinoma in situ in bac of OSF'), 
        ('osf_with_cancer', 'OSF with cancer')], render_kw = {'class': 'form-control'})
      
    initial_prescription = SelectMultipleField(label = 'Initial Prescription', choices = [('mo_excercises_and_habit_intervention', 'Mouth excercises and Habit intervention'),
        ('steroid_intra_lesional_injection', 'Steroid Intra Lensional Injection'), ('topical_steroids', 'Topical Steroids'), 
        ('vitamins', 'Vitamins'), ('pentoxyphylline', 'Pentoxyphylline'), ('surgery', 'Surgery'), ('antifungals', 'Antifungals')], render_kw = {'class': 'form-control'})
   
    complaints_after_initial_prescription = SelectMultipleField(label = 'Complaints after initial perception', choices = [('none', 'None'),
        ('hypertension', 'Hypertension'), ('diabetes','Diabetes'), ('heart_disease', 'Heart Disease'), ('respiratory_disease', 'Respiratory Disease'), 
        ('dermatological_problem', 'Dermatological Problem'), ('gi_problem', 'GI Problem'), ('malnutrition_problem', 'Malnutrition Problem'),
        ('depression', 'Depression'), ('other', 'Other')], render_kw = {'class': 'form-control'})
    
    submit = SubmitField('Predict', render_kw = {'class': 'btn btn-primary'})

    
