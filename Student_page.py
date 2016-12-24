from Config import mysql
from flask import Blueprint, request, abort, jsonify

student_page=Blueprint('student_page',__name__)

@student_page.route('/api/user_page_student', methods=['Put'])
def STpage():
    if not request.json or 'id' not in request.json:
        abort(400)
    id=request.json['id']
    if id is None:
        abort(400)

    conn = mysql.connect()
    cur = conn.cursor()
    query = 'select exists(select * from discipline where id=%s )'
    param = (id)
    cur.execute(query, param)
    if cur.fetchone()[0]==1:
        conn=mysql.connect()
        cur=conn.cursor()
        query_id = 'select discipline_name from discipline where id=%s'
        param_id = (id)
        cur.execute(query_id, param_id)
        data = cur.fetchone()
        return jsonify(subject="%s" % data), 200
    cur.close()