from app.services.student.studentService import Student
from flask import jsonify, request, Response, session , g
from app.utils.settings import *
from flask_json_schema import JsonSchema, JsonValidationError
from app.helper.validator.schema.student import *

import sys

@app.before_request
def before_request_func():
    print("This is a before request function after the objects instance in created")

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({['error']:e.message,'errors':[validation_error.message for validation_error in e.errors]})

# route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    try:
        return jsonify({'Students': Student.get_all_students()})
    except:
        return sys.exc_info()[0]

# route to get student by id
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    return_value = Student.get_student(id)
    try:
        return jsonify(return_value)
    except:
        return sys.exc_info()[0]


# route to add new student
@app.route('/students', methods=['POST'])
@schema.validate(student_schema)
def add_student():
    request_data = request.get_json()
    Student.add_student(request_data["st_name"], request_data["st_phno"], request_data["st_mail"])
    response = Response("Student added", 201, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]


# route to update student with PUT method
@app.route('/students/<int:id>', methods=['PUT'])
@schema.validate(student_schema)
def update_student(id):
    request_data = request.get_json()
    Student.update_student(id, request_data['st_name'], request_data['st_phno'], request_data['st_mail'])
    response = Response("Student Updated", status=200, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]


# route to delete student using the DELETE method
@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    Student.delete_student(id)
    response = Response("student Deleted", status=200, mimetype='application/json')
    try:
        return response
    except:
        return sys.exc_info()[0]

@app.after_request
def after_request_func(responce):
    print("This is a after request function it can be executed multiple times")
    return responce;