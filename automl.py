from flask import Flask, render_template, redirect, request, send_file
from sd import getModel

# Define app.
app = Flask(__name__)

# Import the __init__.py from modules which had imported all files from the folder.
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/', methods =["GET", "POST"])
def dsfd():
    s = 'error'
    if request.method == "POST":
       # getting input with name = fname in HTML form
       sdf = request.form.get("dataset")
       s,file = getModel(config=sdf)
       
    return render_template('result.html',model=s)

@app.route('/model')
def download():
    return send_file('models/model.sav')




if __name__ == '__main__':
    app.run(debug=True)