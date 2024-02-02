from flask import Blueprint, jsonify, request
from models.user_model import UserModel
from uuid import uuid4
from models.entities.user_entitie import User
import re
from datetime import datetime

main = Blueprint('user_blueprint', __name__)

@main.route('/')
def getUsers():
    try:
        users = UserModel.getUsers()
        if users != None:
            return jsonify(users)
        else:
            return jsonify({'message':'No users at this moment'}), 404
    except Exception as error:
        return jsonify({'message':str(error)}), 500
    
@main.route('/add', methods=['POST'])
def addUser():
    try:
        id = uuid4()
        username = request.json["username"]
        email = request.json['email']
        date = datetime.now()

        regex_email = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if regex_email.fullmatch(email):
            user = User(id, username, email, date)
            user_added = UserModel.addUser(user)
            
            if user_added == 1:
                return jsonify({"New user added": user.convertJSON()})
            else:
                return jsonify({"message":"Error user add function"}), 404
        else:
            return jsonify({'message':'Error on syntaxis'}), 404

    except Exception as error:
        return jsonify({"message": str(error)}), 500
    
@main.route('/delete/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        user_deleted = UserModel.deleteUser(id)
        if user_deleted == 1:
            resp = jsonify({"User deleted":id})
            return resp
        else:
            return jsonify({"message":'User delete error'}), 404
    except Exception as error:
        return jsonify({"message":error}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def updateUser(id):
    try:
        username = request.json["username"]
        email = request.json["email"]
        date = UserModel.getUserDate(id)
        user = User(id, username, email, date)

        user_updated = UserModel.updateUser(user)
        if user_updated == 1:
            resp = jsonify({"User updated":user.convertJSON()})
            return resp
        else:
            return jsonify({"message":"User update error"}), 404
        
    except Exception as error:
        return jsonify({"message":str(error)}), 500