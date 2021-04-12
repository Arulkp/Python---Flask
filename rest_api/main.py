from flask import Flask,request# from flask import render
from flask import  render_template
import csv
app = Flask(__name__)


@app.route("/")
def fornt_page():
    #First Page
    return render_template("index.html")

@app.route("/start")
def get_data():
    with open('/home/arulkumar/Downloads/temp/temp.csv', 'r') as file:
        reader = csv.reader(file)
        row = []
        for x in reader:
            row.append(x)        
        return {'data':row} 
    # return render_template('index.html')

if __name__ == "__main__":
    app.run()