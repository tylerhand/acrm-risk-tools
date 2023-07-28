
from flask import render_template, request
def calculator_input():

    if request.method == 'POST':
        return('Menu Here')

    return render_template('crop-insurance/calculator-input.html')


def calculator_result():
    return render_template('crop-insurance/calculator-results.html')