from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hi, this is capstone project under rollout stretegies , this is version 3.0 final project " 
app.run(host="0.0.0.0", port=8080, debug=True)
