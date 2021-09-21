from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hi, this is capstone project under rollover stretegies , this is version 2.0  "
app.run(host="0.0.0.0", port=8080, debug=True)
