from app.services.student.teacherService import Teacher
from flask import jsonify, request, Response
from app.utils.settings import *
from flask_json_schema import JsonValidationError
from app.helper.validator.schema.teacher import *

import sys
@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({['error']:e.message,'errors':[validation_error.message for validation_error in e.errors]})

# route to get all teachers
@app.route('/teachers', methods=['GET'])
def get_teachers():
    try:
        return jsonify({'Teachers': Teacher.get_all_teachers()})
    except:
        return sys.exc_info()[0]

# route to get teacher by id
@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher_by_id(id):
    return_value = Teacher.get_teacher(id)
    try:
        return jsonify(return_value)
    except:
        return sys.exc_info()[0]


# route to add new teacher
@app.route('/teachers', methods=['POST'])
@schema.validate(teacher_schema)
def add_teacher():
    request_data = request.get_json()
    Teacher.add_teacher(request_data["teach_name"], request_data["teach_phno"], request_data["teach_mail"])
    response = Response("Teacher added", 201, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]


# route to update teacher with PUT method
@app.route('/teachers/<int:id>', methods=['PUT'])
@schema.validate(teacher_schema)
def update_teacher(id):
    request_data = request.get_json()
    Teacher.update_teacher(id, request_data['teach_name'], request_data['teach_phno'], request_data['teach_mail'])
    response = Response("Teacher Updated", status=200, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]


# route to delete teacher using the DELETE method
@app.route('/teachers/<int:id>', methods=['DELETE'])
def remove_teacher(id):
    Teacher.delete_teacher(id)
    response = Response("Teacher Deleted", status=200, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]