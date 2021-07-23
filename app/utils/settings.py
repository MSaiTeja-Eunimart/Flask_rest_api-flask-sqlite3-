from flask import Flask
from flask_json_schema import JsonSchema

app = Flask(__name__)
schema=JsonSchema(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teacher.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
