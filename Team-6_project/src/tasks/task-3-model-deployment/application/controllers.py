from flask import render_template
from flask import current_app as app
from functionality import prediction

@app.route("/getresults", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/getresults", methods = ["GET", "POST"])
def result():

    
    prediction.get_prediction()
    return "USE MODEL HERE TO OBTAIN THE SPECIES OF THE PLANT"