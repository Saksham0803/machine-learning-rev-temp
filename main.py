import pickle
from flask import Flask, render_template, request  #(render_template for using html)

app=Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


#url/
@app.route('/')
def index():
    return render_template('app.html')

@app.route('/predict' , methods=['GET','POST'])     #TO POST THE PREDICTION
def predict():
    prediction = model.predict([[request.form.get("temperature")]])
    output = round(prediction[0],2)
    return render_template('app.html',prediction_text=f'Total revenue generated is Rs. {output}/-')

if __name__=='__main__':
    app.run(debug=True)

