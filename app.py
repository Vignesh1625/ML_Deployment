from flask import Flask,render_template,request
import pickle
import numpy as np


with open('model.pk1', 'rb') as file:
    loaded_model = pickle.load(file)

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello():
    if request.method == 'POST' :
        name = request.form["username"]
        hum = int(request.form['hum'])
        temp = int(request.form['temp'])
        steps = int(request.form['steps'])
        # Chloramines = int(request.form['Chloramines'])
        # Sulfate = int(request.form['Sulfate'])
        # Conductivity = int(request.form['Conductivity'])
        # Organic_carbon = int(request.form['Organic_carbon'])
        # Trihalomethanes = int(request.form['Trihalomethanes'])
        # Turbidity = int(request.form['Turbidity'])

        input_values = [hum,temp,steps]
        test_case_2d = np.array(input_values).reshape(1, -1)
        pred = loaded_model.predict(test_case_2d)
        print(pred)
        if( pred[0] == 0 ) :
            return render_template("index.html",stress_level=" Relax! your stress levels are low to be worried of")
        elif( pred[0] == 1) :
            return render_template("index.html",stress_value=" Your stress levels are probalby at a considerable level, take a short break and try exposing yourself to fresh air or grab a cup of tea or coffee")
        elif( pred[0] == 2) :
            return render_template("index.html",stress_level=" Your stress levels are probably high. Take a break, listen to music, take deep breath, expose yourself to fresh air, try going out for a walk or doing some physical activity. Don't ignore these because it will be difficult for you to be productive at this level of stress.")
        else :
            return render_template("index.html",stress_level="")
    return render_template("index.html",stress_level = " ")


if __name__ == "__main__" :
    app.run(debug=True)