from flask import Flask,render_template,request
import joblib
import pandas as pd 
app=Flask(__name__)
model=joblib.load("model.pkl")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=['post'])
def predict():
    if request.method=="POST":
        data={
            "City":request.form.get['City'],
            "RoomType": request.form['RoomType'],
            "Bedroom": float(request.form['Bedroom']),
            "Bathroom": float(request.form['Bathroom']),
            "GuestsCapacity": int(request.form['GuestsCapacity']),
            "HasWifi": int(request.form['HasWifi']),
            "HasAC": int(request.form['HasAC']),
            "DistanceFromCityCenter": float(request.form['DistanceFromCityCenter'])
            }
        df=pd.DataFrame([data]) #it will convert from rows to column
        prediction=model.predict(df)[0]
        return render_template("index.html",prediction_text=f"predictrdpricr {round{prediction:.2f}}")
    return render_template("index.html")
if __name__ =="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
    