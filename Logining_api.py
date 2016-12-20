from Config import mysql
from flask import jsonify
from flask import request, abort, Blueprint


logining_api=Blueprint('logining_api', __name__)

@logining_api.route('/api/login', methods=['Post'])
def singIN():
    if not request.json:
        abort(400)
    print(request.json)
    if 'name' not in request.json or 'password' not in request.json:
        abort(400)
    name=request.json['name']
    if name is None:
        abort(400)
    password=request.json['password']
    if password is None:
        abort(400)
    conn=mysql.connect()
    cur=conn.cursor()
    query_logining='select exists(select * from list_of_user where name=%s and password=%s )'
    param_logining=(name, password)
    cur.execute(query_logining, param_logining)
    if cur.fetchone()[0]==1:
        connect=mysql.connect()
        cursor=connect.cursor()
        query_id='select id from list_of_user where name=%s'
        param_id=(name)
        cursor.execute(query_id, param_id)
        data=cursor.fetchone()
        return jsonify(user_id="%s"% data), 200
    cur.close()




