from flask import Flask
from flask import render_template,request
import xlrd
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import re
app = Flask(__name__)

@app.route("/")
def page_render():
  return render_template('index.html')

@app.route('/submit' , methods=["POST"])
def submit():
	data = request.files['file']
	data.save(os.path.join(app.config['UPLOAD_FOLDER']+"/templates", secure_filename(data.filename)))
	filename = re.sub('[()]','',data.filename)
	wb = xlrd.open_workbook(os.path.join(app.config['UPLOAD_FOLDER']+"/templates",filename.replace(" ","_")))
	sheet = wb.sheet_by_index(0)
	output = """<html>
	<head>
		<style>
		table {
		  font-family: arial, sans-serif;
		  border-collapse: collapse;
		  width: 100%;
		}

		td, th {
		  border: 1px solid #dddddd;
		  text-align: left;
		  padding: 8px;
		}

		tr:nth-child(even) {
		  background-color: #dddddd;
		}
		</style>
			</head>
		<body>
<table style="border:1px solid black">
	"""
	for x in range(0,sheet.nrows):
		output += """<tr style="border:1px solid black">"""
		for y in range(0,sheet.ncols):
			cell = sheet.cell(x, y)			
			output+= """<td style="border:1px solid black">{0}</td>""".format(str(cell.value))
		output += """</tr>"""
	output += """</table></body></html>"""
	return output

if __name__ == "__main__":
   app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath('flask_ty.py'))
   app.run()