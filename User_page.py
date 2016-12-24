#from Config import app
#from flask import Blueprint, request, abort
#from Doctor_page import profesor_page
#from Student_page import student_page

#user_page=Blueprint('user_page', __name__)

#@user_page.route('/usercheck')
#def User():
    #if not request.json or 'user' not in request.json:
        #abort(400)
    #user=request.json['user']
    #if user is None:
        #abort(400)
    #if user is 'student':
        #app.register_blueprint(student_page)
    #if user is 'profesor':
        #app.register_blueprint(profesor_page)

