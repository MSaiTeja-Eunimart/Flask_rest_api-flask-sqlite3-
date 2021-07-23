from flask_sqlalchemy import SQLAlchemy
from api import *

class Teacher1(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    teach_name = db.Column(db.String(80))
    teach_phno = db.Column(db.Integer)
    teach_mail = db.Column(db.String(80))