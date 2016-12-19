from Config import app
from flask import send_from_directory, redirect
from Logining_api import logining_api
from Register_api import register_api


@app.route('/')
def index():
   return redirect('/index.html')

@app.route('/<path:path>')
def send_js(path):
   return send_from_directory('static', path)

app.register_blueprint(register_api)
app.register_blueprint(logining_api)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8080)