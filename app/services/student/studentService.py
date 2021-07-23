from app.utils.settings import *
from flask_sqlalchemy import SQLAlchemy
from app.model.student import Student1
from api import db
import logging

logging.basicConfig(filename='stundentlogger.log', level=logging.DEBUG
                    , format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

db.create_all()
class Student(db.Model):
    def json(self):
        return {'id': self.id, 'Student name': self.st_name,'st_phno': self.st_phno, 'st_mail': self.st_mail}


    def add_student(st_name,st_phno,st_mail):
        app.logger.info("Added a new student")
        app.logger.warning("Could not add a new student")
        new_student = Student1(st_name=st_name, st_phno=st_phno,st_mail=st_mail)
        db.session.add(new_student)
        db.session.commit()

    def get_all_students():
        app.logger.info("Fetched all the details of the students")
        app.logger.warning("Could not fetch the student")
        return [Student.json(student) for student in Student.query.all()]

    def get_student(id):
        app.logger.info("Fetched the details of the student with id " + str(id))
        app.logger.warning("Waring level log")
        return [Student.json(Student.query.filter_by(id=id).first())]

    def update_student(id, st_name, st_phno, st_mail):
        app.logger.info("Updated the details of the student with id " + str(id))
        app.logger.warning("Waring level log")
        student = Student.query.filter_by(id=id).first()
        student.st_name = st_name
        student.st_phno = st_phno
        student.st_mail = st_mail
        db.session.commit()

    def delete_student(id):
        app.logger.info("Teacher deleted with id " + str(id))
        app.logger.warning("Waring level log")
        Student.query.filter_by(id=id).delete()
        db.session.commit()