from Config import mysql
from flask import Blueprint, request, abort, jsonify


student_page=Blueprint('student_page', __name__)

@student_page.route('/api/user_page_student', methods=['Post'])
def student_page():
    if not request.json or 'id' not in request:
        abort(400)
    id=request.json['id']
    if id is None:
        abort(400)
    conn = mysql.connect()
    cur = conn.cursor()
    query_id = ''
    param_id = (id)
    cur.execute(query_id, param_id)
    if cur.fetchone()[0] == 1:
        conn=mysql.connect()
        cur=conn.cursor()
        query_subjects='скрипт який верне предмети по id'
        param_subjects=(id)
        cur.execute(query_subjects, param_subjects)
        return jsonify(subjects=''), 200
    cur.close()