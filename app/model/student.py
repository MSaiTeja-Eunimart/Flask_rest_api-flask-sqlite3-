from flask_sqlalchemy import SQLAlchemy
from api import *

class Student1(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    st_name = db.Column(db.String(80))
    st_phno = db.Column(db.Integer)
    st_mail = db.Column(db.String(80))