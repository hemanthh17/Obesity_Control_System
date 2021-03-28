from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app=Flask(__name__,template_folder='templates')
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 16)
    loaded_model = pickle.load(open("pkl.pkl.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
@app.route('/',methods=['GET'])
def home():
    if request.method=='GET':
        return render_template('form.html')
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)        
        if int(result)== 1:
            prediction ='Income more than 50K'
        else:
            prediction ='Income less that 50K'            
        return render_template("result.html", prediction = prediction)

if __name__ == "__main__":
    app.run(debug=True)