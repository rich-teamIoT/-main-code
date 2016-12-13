from flask import Blueprint
from Config import app
from Student_page import student_page
from Doctor_page import doctor_page
user_page=Blueprint('user_page', __name__)

app.register_blueprint(student_page)
app.register_blueprint(doctor_page)

