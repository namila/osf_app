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
    betel_ingrediants = None
    daily_average_of_smoking_frequency = 0
    average_years_of_smoking = 0
    smoking_type = None
    alchohol_type = None
    has_difficulty_in_mouth_opening = False
    is_toungue_movement_restricted = False
    is_patch_present = False
    has_depapilation_on_lips = False
    hemoglobin_level = 0
    medical_history = None
    fibrous_bands = None
    has_leukoplakia = False
    has_erythroplakia = False
    has_candida = False
    intial_dignosis = None
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
        self.betel_ingrediants = form_input['betel_ingrediants']
        self.daily_average_of_smoking_frequency = form_input['daily_average_of_smoking_frequency']
        self.average_years_of_smoking = form_input['average_years_of_smoking']
        self.smoking_type = form_input['smoking_type']
        self.alchohol_type = form_input['alchohol_type']
        self.has_difficulty_in_mouth_opening = form_input['has_difficulty_in_mouth_opening']
        self.is_toungue_movement_restricted = form_input['is_toungue_movement_restricted']
        self.is_patch_present = form_input['is_patch_present']
        self.has_depapilation_on_lips = form_input['has_depapilation_on_lips']
        self.hemoglobin_level = form_input['hemoglobin_level']
        self.medical_history = form_input['medical_history']
        self.fibrous_bands = form_input['fibrous_bands']
        self.has_leukoplakia = form_input['has_leukoplakia']
        self.has_erythroplakia = form_input['has_erythroplakia']
        self.has_candida = form_input['has_candida']
        self.intial_dignosis = form_input['intial_dignosis']
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
            'betel_ingrediants':  self.process_string_list(self.betel_ingrediants),
            'daily_average_of_smoking_frequency': self.daily_average_of_smoking_frequency,
            'average_years_of_smoking': self.average_years_of_smoking,
            'smoking_type':  self.process_string_list(self.smoking_type),
            'alchohol_type':  self.process_string_list(self.alchohol_type),
            'has_difficulty_in_mouth_opening': 'Yes' if self.has_difficulty_in_mouth_opening == 1 else 'No',
            'is_toungue_movement_restricted': 'Yes' if self.is_toungue_movement_restricted == 1 else 'No',
            'is_patch_present': 'Yes' if self.is_patch_present == 1 else 'No',
            'has_depapilation_on_lips': 'Yes' if self.has_depapilation_on_lips == 1 else 'No',
            'hemoglobin_level': self.hemoglobin_level,
            'medical_history': self.process_string_list(self.medical_history),
            'fibrous_bands': self.process_string_list(self.fibrous_bands),
            'has_leukoplakia': 'Yes' if self.has_leukoplakia == 1 else 'No',
            'has_erythroplakia': 'Yes' if self.has_erythroplakia == 1 else 'No',
            'has_candida': 'Yes' if self.has_candida == 1 else 'No',
            'intial_dignosis': self.process_string_list(self.intial_dignosis),
            'intial_prescription': self.process_string_list(self.intial_prescription),
            'complaints_after_initial_prescription': self.process_string_list(self.complaints_after_initial_prescription),
        }
        return formatted_input

    def process_string_list(self, list):
        if len(list) == 0:
            return ''
        capitalized_list = map(lambda item: item.replace('_', ' ').capitalize(), list)
        return ', '.join(capitalized_list)
