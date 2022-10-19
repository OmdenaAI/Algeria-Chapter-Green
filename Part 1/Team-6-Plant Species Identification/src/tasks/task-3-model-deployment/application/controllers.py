from flask import render_template, request
from flask import current_app as app
from functionality import prediction
from werkzeug.utils import secure_filename
import os

CURRDIR = os.path.dirname(os.getcwd()) + "/task-3-model-deployment/"

@app.route("/", methods = ["GET", "POST"])
def home():
    predicted_val = ""
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(f.filename)
        predicted_val = prediction.get_prediction(filename)
        os.remove(CURRDIR+f.filename)
    return render_template("index.html", prediction = predicted_val)

@app.route("/getresults", )
def result():

    
    return "USE MODEL HERE TO OBTAIN THE SPECIES OF THE PLANT"