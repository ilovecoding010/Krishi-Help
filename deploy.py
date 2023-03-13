from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
#load the model


@app.route('/')
def home():
    return render_template('index.html',**locals())
@app.route('/predict',methods=['POST'])
def predict():
    nitro = int(request.form['Nitrogen'])
    phosphorus = int(request.form['phosphorus'])
    potassium = int(request.form['potassium'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    result = model.predict([[nitro,phosphorus,potassium,temperature,humidity,ph,rainfall]])[0]
    return render_template('index.html',**locals())

if __name__ == '__main__':
    model = joblib.load('minor_project_model.pkl')
    app.run(debug=True)
    app.static_folder = 'static'