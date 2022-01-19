from tensorflow.keras.models import load_model
import joblib

class Predictor:
    model = None
    scaler = None

    age = 0
    sex = None 
    has_burning_sensation = False
    daily_average_of_betal_quids = 0
    average_years_of_betel_consumption =  0
    daily_average_of_smoking_frequency = 0
    average_years_of_smoking = 0
    has_difficulty_in_mouth_opening = False
    is_toungue_movement_restricted = False
    medical_history = None
    fibrous_bands = None
    has_leukoplakia = False
    has_erythroplakia = False
    intial_dignosis = None
    has_candida = False
    intial_prescription = None
    complaints_after_initial_prescription = None

    def __init__(self, form_input) -> None:
        self.model = load_model('pretrained_objects/osf_model.h5')
        selfscaler = joblib.load('pretrained_objects/osf_scaler.pkl')

        self.sex = form_input['sex'] 
        self.age = form_input['age']
        self.has_burning_sensation = form_input['has_burning_sensation']
        self.daily_average_of_betal_quids = form_input['daily_average_of_betal_quids']
        self.average_years_of_betel_consumption =  form_input['average_years_of_betel_consumption']
        self.daily_average_of_smoking_frequency = form_input['daily_average_of_smoking_frequency']
        self.average_years_of_smoking = form_input['average_years_of_smoking']
        self.has_difficulty_in_mouth_opening = False
        self.is_toungue_movement_restricted = False
        self.medical_history = form_input['medical_history']
        self.fibrous_bands = form_input['fibrous_bands']
        self.has_leukoplakia = False
        self.has_erythroplakia = False
        self.intial_dignosis = form_input['intial_dignosis']
        self.has_candida = False
        self.intial_prescription = form_input['intial_prescription']
        self.complaints_after_initial_prescription = form_input['complaints_after_initial_prescription']

    def predict_risk(self):
        return 1

    def get_formatted_input_data(self):
        formatted_input  =  {
            'age': self.age,
            'sex': self.sex,
            'has_burning_sensation': 'Yes' if self.has_burning_sensation == 1 else 'No',
            'daily_average_of_betal_quids': self.daily_average_of_betal_quids,
            'average_years_of_betel_consumption': self.average_years_of_betel_consumption,
            'daily_average_of_smoking_frequency': self.daily_average_of_smoking_frequency,
            'average_years_of_smoking': self.average_years_of_smoking,
            'has_difficulty_in_mouth_opening': 'Yes' if self.has_difficulty_in_mouth_opening == 1 else 'No',
            'is_toungue_movement_restricted': 'Yes' if self.is_toungue_movement_restricted == 1 else 'No',
            'medical_history': self.medical_history.replace('_', ' ').capitalize(),
            'fibrous_bands': self.fibrous_bands.replace('_', ' ').capitalize(),
            'has_leukoplakia': 'Yes' if self.has_leukoplakia == 1 else 'No',
            'has_erythroplakia': 'Yes' if self.has_erythroplakia == 1 else 'No',
            'intial_dignosis': self.intial_dignosis.replace('_', ' ').capitalize(),
            'has_candida': 'Yes' if self.has_candida == 1 else 'No',
            'intial_prescription': self.intial_prescription.replace('_', ' ').capitalize(),
            'complaints_after_initial_prescription': self.complaints_after_initial_prescription.replace('_', ' ').capitalize(),
        }
        return formatted_input
        
