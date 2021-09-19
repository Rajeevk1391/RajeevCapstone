from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hi, My name is Rajeev, this is green deployment of the application version 1.0 "
app.run(host="0.0.0.0", port=8080, debug=True)
