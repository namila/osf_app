from tensorflow.keras.models import load_model
import numpy as np
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
    initial_dignosis = None
    initial_prescription = None
    complaints_after_initial_prescription = None

    def __init__(self, form_input) -> None:
        self.model = load_model('pretrained_objects/osf_model.h5')
        self.scaler = joblib.load('pretrained_objects/osf_scaler.pkl')

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
        self.initial_dignosis = form_input['initial_dignosis']
        self.initial_prescription = form_input['initial_prescription']
        self.complaints_after_initial_prescription = form_input['complaints_after_initial_prescription']

    def predict_risk(self):
        predicion_input = [[
            self.age,
            self.daily_average_of_betal_quids,
            self.daily_average_of_smoking_frequency,
            self.average_years_of_betel_consumption,
            self.has_difficulty_in_mouth_opening,
            self.is_patch_present,
            1 if 'lime' in self.betel_ingrediants else 0,
            1 if 'beedi' in self.smoking_type else 0,
            1 if 'arrack' in self.alchohol_type else 0,
            self.is_toungue_movement_restricted,
            self.has_depapilation_on_lips,
            1 if 'osf_with_mild_to_moderate_dysplsia' in self.initial_dignosis else 0,
            1 if 'osf_with_severe_dysplasia' in self.initial_dignosis else 0,
            1 if 'steroid_intra_lesional_injection' in self.initial_prescription else 0,
            1 if 'topical_steroids' in self.initial_prescription else 0,
            1 if 'diabetes' in self.complaints_after_initial_prescription else 0,
            1 if 'heart_disease' in self.complaints_after_initial_prescription else 0,
            self.has_leukoplakia,
            self.has_erythroplakia,
            1 if self.has_leukoplakia == 0 and self.has_erythroplakia == 0 else 0,
            self.hemoglobin_level
        ]]

        test = [[51.56511172,  7.15289256,  5.01244444,  0.        ,  0.        ,
        0.64883756,  1.        ,  0.        ,  0.        ,  1.        ,
        0.35116244,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
       13.83614035]]

        transformed_input = self.scaler.transform(predicion_input)
        results = self.model.predict_classes(transformed_input)
        return results[0][0]
    
    def get_binary_value_from_boolean(self, boolean_value):
        return boolean_value

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
            'initial_dignosis': self.process_string_list(self.initial_dignosis),
            'intial_prescription': self.process_string_list(self.initial_prescription),
            'complaints_after_initial_prescription': self.process_string_list(self.complaints_after_initial_prescription),
        }
        return formatted_input

    def process_string_list(self, list):
        if len(list) == 0:
            return ''
        capitalized_list = map(lambda item: item.replace('_', ' ').capitalize(), list)
        return ', '.join(capitalized_list)
