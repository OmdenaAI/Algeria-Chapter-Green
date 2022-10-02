from flask import render_template, request
from flask import current_app as app
from functionality import prediction
from werkzeug.utils import secure_filename
import os

CURRDIR = os.path.dirname(os.getcwd()) + "/task-3-model-deployment/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getresults", methods = ["GET", "POST"])
def result():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(f.filename)
        Val = prediction.get_prediction(filename)
        os.remove(CURRDIR+f.filename)
        return f"<h1>{Val}</h1>"
    return "USE MODEL HERE TO OBTAIN THE SPECIES OF THE PLANT"