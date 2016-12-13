from flask import request, abort, jsonify, Blueprint
from Config import mysql
logining_api=Blueprint('logining_api', __name__)

@logining_api.route('/api/login', methods=['Post'])
def singIN():
    if not request.json:
        abort(400)
    print(request.json)
    if 'login' not in request.json or 'password' not in request.json:
        abort(400)

    login=request.json['login']
    if login is None:
        abort(400)
    password=request.json['password']
    if password is None:
        abort(400)
    conn=mysql.connect()
    cur=conn.cursor()
    query_logining='select exists(select * from user_list where login=%s and password=%s )'
    param_logining=(login, password)
    cur.execute(query_logining, param_logining)
    if cur.fetchone()[0]==1:
        query_id = 'Скрипт який з бази даних витягне id користувача за login'
        param_id = (id)
        cur.execute(query_id, param_id)
        return jsonify(user_id=id), 200
    cur.close()

