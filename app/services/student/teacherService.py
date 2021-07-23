from app.utils.settings import *
from flask_sqlalchemy import SQLAlchemy
from app.model.teacher import Teacher1
from api import db
import logging

logging.basicConfig(filename='teacherlogger.log', level=logging.DEBUG
                    , format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

db.create_all()
class Teacher(db.Model):
    def json(self):
        return {'id': self.id, 'Teacher name': self.teach_name,'teach_phno': self.teach_phno,
                'teach_mail': self.teach_mail}


    def add_teacher(teach_name,teach_phno,teach_mail):
        app.logger.info("Added a new teacher")
        app.logger.warning("Could not add a new teacher")
        new_teacher = Teacher1(teach_name=teach_name, teach_phno=teach_phno, teach_mail=teach_mail)
        db.session.add(new_teacher)
        db.session.commit()

    def get_all_teachers():
        app.logger.info("Fetched all the details of the teacher")
        app.logger.warning("Could not fetch the details")
        return [Teacher.json(teacher) for teacher in Teacher.query.all()]

    def get_teacher(id):
        app.logger.info("Fetched the details of the teacher with id "+ str(id))
        app.logger.warning("Waring level log")
        return [Teacher.json(Teacher.query.filter_by(id=id).first())]

    def update_teacher(id, teach_name, teach_phno, teach_mail):
        app.logger.info("Updated the details of the teacher with id "+str(id))
        app.logger.warning("Waring level log")
        teacher = Teacher.query.filter_by(id=id).first()
        teacher.teach_name = teach_name
        teacher.teach_phno = teach_phno
        teacher.teach_mail = teach_mail
        db.session.commit()

    def delete_teacher(id):
        app.logger.info("Teacher deleted with id "+str(id))
        app.logger.warning("Waring level log")
        Teacher.query.filter_by(id=id).delete()
        db.session.commit()
        db.session.commit()