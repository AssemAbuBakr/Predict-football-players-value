from flask import Flask, render_template, request
import json
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route("/")
def home():
    return render_template('index.html')

    
@app.route("/predict", methods=["POST"])
def predict():
    Age =  float(request.form['Age'])
    Potential =  float(request.form['Potential'])
    WeakFoot =  float(request.form['Weak Foot'])
    Weight =  float(request.form['Weight'])
    Finishing =  float(request.form['Finishing'])
    HeadingAccuracy =  float(request.form['HeadingAccuracy'])
    ShortPassing =  float(request.form['ShortPassing'])
    Dribbling =  float(request.form['Dribbling'])
    Curve =  float(request.form['Curve'])
    BallControl =  float(request.form['BallControl'])
    Acceleration =  float(request.form['Acceleration'])
    SprintSpeed =  float(request.form['SprintSpeed'])
    Agility =  float(request.form['Agility'])
    Reactions =  float(request.form['Reactions'])
    Balance =  float(request.form['Balance'])
    ShotPower =  float(request.form['ShotPower'])
    Jumping =  float(request.form['Jumping'])
    Stamina =  float(request.form['Stamina'])
    Strength =  float(request.form['Strength'])

    if request.form['PreferredFoot']=="Right":
        PreferredFoot=float(1)
    else:
        PreferredFoot=float(0)

    result = int(model.predict([[Age, Potential, PreferredFoot, WeakFoot,Weight,Finishing,HeadingAccuracy,ShortPassing,Dribbling,Curve,BallControl,Acceleration,SprintSpeed,Agility,Reactions,Balance,ShotPower,Jumping,Stamina,Strength]]))
    if result <0:
        result="0"
    return render_template("index.html", result=result) 



if __name__ == "__main__":
    app.run()
