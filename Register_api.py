from Config import mysql
from flask import Blueprint, request, abort, jsonify


register_api = Blueprint('register_api', __name__)

@register_api.route('/api/register', methods=['Post'])
def register():
    if not request.json:
        abort(400)
    print(request.json)
    if 'name' not in request.json:
        abort(400)
    if 'password' not in request.json:
        abort(400)
    name=request.json['name']
    conn=mysql.connect()
    cur= conn.cursor()
    if name is None:
        jsonify(status="name is None"), 400
    query_name='select exists(select * from list_of_user where name=%s)'
    param_name=(name)
    cur.execute(query_name,param_name)
    if cur.fetchone()[0]==1:
        jsonify(status="this name already exists"), 400

    email=request.json['email']
    if email is None:
        jsonify(status="email is None"), 400
    query_email='select exists(select * from list_of_user where email=%s)'
    param_email=(email)
    cur.execute(query_email,param_email)
    if cur.fetchone()[0]==1:
       jsonify(status="this email already exists"), 400
    cur.close()

    password=request.json['password']
    if password is None:
        jsonify(status="password is None"), 400

    query_save = 'insert into list_of_user (name, password, email) values (%s, %s, %s)'
    param_save = (name, password, email)
    cur = conn.cursor()
    cur.execute(query_save, param_save)
    conn.commit()
    cur.close()
    return jsonify(status='success'), 201
