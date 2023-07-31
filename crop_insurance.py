from flask import render_template, request
import requests
from config import cropInsuranceConfig

def refresh_credentials():
    request.post('https://' + cropInsuranceConfig['api-domain'] + '/auth')
def calculator_input():

    if request.method == 'POST':

        # Get form data
        state = request.form.get('state')
        year = request.form.get('year')
        crop = request.form.get('crop')

        # Search for policies for that crop year
        r = requests.post('https://' + cropInsuranceConfig['api-domain'] + '/crop-insurance',
            headers={'auth': "Bearer {auth}".format(auth = cropInsuranceConfig['auth'])},
            json = {"state": state,"year" : year,"crop": crop}
            )

        if r.status_code != 200:
            error = 'The crop insurance calculation API is currently unavailable. Please contact us if this happens again.'
            return render_template('crop-insurance/calculator-input.html',error=error)

        # Generate Options

    return render_template('crop-insurance/calculator-input.html')

def calculator_result():

    if request.method == 'POST':
        # make api call
        year = request.form['year']

    return render_template('crop-insurance/calculator-results.html')
