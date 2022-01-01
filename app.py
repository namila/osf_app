from flask import Flask, render_template, session, redirect, url_for
from data_import_form import DataImportForm
from prediction_form import PredictionForm

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
        session['field_1'] = prediction_form.field_1.data
        return redirect(url_for('prediction_results'))
    return render_template('prediction.html',  form = prediction_form)

@app.route('/prediction/results')
def prediction_results():
    results = session['field_1']
    return render_template('prediction_results.html', results = results)


if __name__ == '__main__':
    app.run(debug = True)
