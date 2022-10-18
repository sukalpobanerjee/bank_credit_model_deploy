#from crypt import methods
import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np
 
# Create an object for the class Flask
 
app = Flask(__name__)
model = pickle.load(open('model (1).pkl','rb'))
 
@app.route('/')
 
def home():
    return render_template('index.html') 
    
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        LIMIT_BAL = int(request.form ['LIMIT_BAL'])
        SEX = int(request.form ['SEX'])
        EDUCATION = int(request.form ['EDUCATION'])
        MARRIAGE = int(request.form['MARRIAGE'])
        AGE = int(request.form ['AGE'])
        PAY_0 = int(request.form ['PAY_0'])  
        
        prediction=model.predict_proba([['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0']])
        output=round(prediction[0][0],2)
        return render_template('index.html', prediction_text =f'Probability of the customer is {output}')
    
    except:
        return render_template('index.html', prediction_text ='Invalid input')
 
if __name__ =='__main__':
    app.run(debug=True)


model.feature_names_
