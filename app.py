from flask import Flask, render_template, request
import pickle
import numpy as np

#load pickle file
filename = 'hr_employee.pkl'
rfc = pickle.load(open(filename, 'rb'))


app = Flask(__name__)

@app.route('/')
def name():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        sat = float( request.form['satisfaction_level'] )
        le = float( request.form['last_evaluation'] )
        npr = int( request.form['number_project'] )
        amh = int( request.form['average_montly_hours'] )
        tsc = int( request.form['time_spend_company'] )
        wa = request.form['Work_accident']
        if wa =='Yes':
            wa=1
        elif wa =='No':
            wa=0

        ply = request.form['promotion_last_5years']
        if ply =='Yes':
            ply=1
        elif ply =='No':
            ply=0

        sal = request.form['salary']
        if sal=='low':
            sal=0
        elif sal=='Medium':
            sal=1
        elif sal=='High':
            sal=2

        data = np.array( [[sat, le, npr, amh, tsc, wa, ply, sal]] )
        result = rfc.predict(data)
        return render_template( 'index.html', prediction=result,data=data )



if __name__=='__main__':
    app.run(debug=True)