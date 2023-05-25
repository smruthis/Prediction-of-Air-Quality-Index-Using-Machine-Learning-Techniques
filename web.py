from flask import Flask,render_template,request
import pickle
import numpy as np


app =Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template ('home.html')


@app.route('/predict',methods=['POST'])
def prediction():
    PM25 = float(request.form['PM2.5'])
    PM10= float(request.form['PM10'])
    NO = float(request.form['NO'])
    NO2 = float(request.form['NO2'])
    NOX = float(request.form['NOx'])
    NH3= float(request.form['NH3'])
    CO= float(request.form['CO'])
    SO2 = float(request.form['SO2'])
    O3 = float(request.form['CO'])
    Benzene= float(request.form['Benzene'])
    Toluene= float(request.form['Toluene'])
    result=model.predict([[PM25,PM10,NO,NO2,NOX,NH3,CO,SO2,O3,Benzene,Toluene]])[0]
     # Categorize AQI based on the predicted value
    if result >= 0 and result <= 50:
        aqi_category = 'Good'
    elif result >= 51 and result <= 100:
        aqi_category = 'Satisfactory'
    elif result >= 101 and result <= 200:
        aqi_category = 'Moderate'
    elif result >= 201 and result <= 300:
        aqi_category = 'Poor'
    elif result >= 301 and result <= 400:
        aqi_category = 'Very Poor'
    else:
        aqi_category = 'Severe'

    return render_template('result.html',prediction_text="The AQI is {},which is categorized as {}".format(result,aqi_category))

if __name__=='__main__':
    app.run(debug=True)  


