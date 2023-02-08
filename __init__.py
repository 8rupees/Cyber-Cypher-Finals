from flask import Flask, render_template, url_for ,request,redirect
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from datetime import datetime
import pickle
import joblib
import numpy as np
import sklearn
import matplotlib.pyplot as plt


app = Flask(__name__)
cols=['terrain','rain','soil','trees']

df = pickle.load(open('database.pkl','rb'))
model = DecisionTreeClassifier()
X = df.drop(columns = "tress")
y = df["tress"]
model.fit(X,y)

@app.route('/')

def home():
   return render_template('index.html')


@app.route('/predict',methods=['POST'])

def Predict():
   feature_list = request.form.to_dict()
   feature_list = list(feature_list.values())
   feature_list = list(map(float, feature_list))
   final_features = np.array(feature_list).reshape(1, 3) 
   prediction = model.predict(final_features)

   return render_template('index.html', prediction_text='The area in sqkm is - {}'.format(prediction))


if __name__ == '__main__':
   app.run(debug=True)
