from flask import Flask, render_template
import config, pages, crop_insurance
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.context_processor
def inject_menu_items():
    return dict(menu=config.siteConfig['menu'], )

SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{hostname}:{port}/{database_name}".format(
    username=config.dbConfig['username'],
    password=config.dbConfig['password'],
    hostname=config.dbConfig['hostname'],
    port = config.dbConfig['port'],
    database_name=config.dbConfig['database'],
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#db = SQLAlchemy(app)

app.secret_key = config.siteConfig['secret-key']
'''
class availableCropInsurancePolicies(db.Model):

    __tablename__ = "crop_insurance_plans"

    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'), nullable=False)
    date_added = db.Column(db.DateTime(), nullable=False)
    last_modified = db.Column(db.DateTime())
    crop_year = db.Column(db.Integer)
    crop = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text())
'''


# Basic Pages
app.add_url_rule('/', view_func=pages.index)
app.add_url_rule('/contact', view_func=pages.contact)

# Crop Insurance
app.add_url_rule('/crop-insurance/calculator-input', view_func=crop_insurance.calculator_input,methods=['GET','POST'])
app.add_url_rule('/crop-insurance/calculator-result', view_func=crop_insurance.calculator_result,methods=['POST'])

if __name__ == '__main__':
    app.run()
