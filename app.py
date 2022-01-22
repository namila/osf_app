from flask import Flask, render_template, session, redirect, url_for
from data_import_form import DataImportForm
from prediction_form import PredictionForm
from predictor import Predictor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OSF_APP_SECRET'

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', form = {})

@app.route('/data-import', methods = ['get','post'])
def data_import_page():
    data_import_form =  DataImportForm()

    if data_import_form.validate_on_submit():
        session['field_1'] = data_import_form.field_1.data
    return render_template('data-import.html',  form = data_import_form)

@app.route('/prediction', methods = ['get','post'])
def pediction_page():
    prediction_form  = PredictionForm()

    if prediction_form.validate_on_submit():
        session['prediction_input'] = {
            'age': prediction_form.age.data,
            'sex': prediction_form.sex.data,
            'has_burning_sensation': prediction_form.has_burning_sensation.data,
            'daily_average_of_betal_quids': prediction_form.daily_average_of_betal_quids.data,
            'average_years_of_betel_consumption': prediction_form.average_years_of_betel_consumption.data,
            'betel_ingrediants': prediction_form.betel_ingrediants.data,
            'daily_average_of_smoking_frequency': prediction_form.daily_average_of_smoking_frequency.data,
            'average_years_of_smoking': prediction_form.average_years_of_smoking.data,
            'smoking_type': prediction_form.smoking_type.data,
            'alchohol_type': prediction_form.alchohol_type.data,
            'has_difficulty_in_mouth_opening': prediction_form.has_difficulty_in_mouth_opening.data,
            'is_toungue_movement_restricted': prediction_form.is_toungue_movement_restricted.data,
            'is_patch_present': prediction_form.is_patch_present.data,
            'has_depapilation_on_lips': prediction_form.has_depapilation_on_lips.data,
            'hemoglobin_level': prediction_form.hemoglobin_level.data,
            'medical_history': prediction_form.medical_history.data,
            'fibrous_bands': prediction_form.fibrous_bands.data,
            'has_leukoplakia': prediction_form.has_leukoplakia.data,
            'has_erythroplakia': prediction_form.has_erythroplakia.data,
            'has_candida': prediction_form.has_candida.data,
            'initial_dignosis': prediction_form.initial_dignosis.data,
            'initial_prescription': prediction_form.initial_prescription.data,
            'complaints_after_initial_prescription': prediction_form.complaints_after_initial_prescription.data,
        }
        return redirect(url_for('prediction_results'))
    return render_template('prediction.html',  form = prediction_form)

@app.route('/prediction/results')
def prediction_results():
    predictor = Predictor(session['prediction_input'])
    result = predictor.predict_risk()
    return render_template('prediction_results.html', input_data = predictor.get_formatted_input_data(), result= result)


if __name__ == '__main__':
    app.run(debug = True)
