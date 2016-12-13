from flask import Blueprint, request, abort, jsonify
from Config import mysql
student_page=Blueprint('student_page', __name__)

@student_page.route('/api/user_page_student', methods=['Post'])
def student_page():
    if not request.json:
        abort(400)
    if 'id' not in request:
        abort(400)
    id=request.json['id']
    if id is None:
        abort(400)
    conn = mysql.connect()
    cur = conn.cursor()
    query_id = '(Скрипт який перевірить чи є за таким id якось інформація в таблиці)'
    param_id = (id)
    cur.execute(query_id, param_id)
    if cur.fetchone()[0] == 1:
        return jsonify(status="success"), 200
    cur.close()