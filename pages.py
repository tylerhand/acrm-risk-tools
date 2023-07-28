from flask import render_template

def index():
    return render_template('pages/home.html')

def contact():
    return render_template('pages/contact.html')