from flask import Flask,request
import pymongo
import json
from bson import json_util


client =  pymongo.MongoClient("mongodb://localhost:27017/")
table = client['test']
app = Flask(__name__)


@app.route('/get_data')
def read():
	docs_list  = list(table['aion'].find())
	return json.dumps(docs_list, default=json_util.default)
   

@app.route('/add_data' , methods=["POST"])
def write():
	table['aion'].insert_many([request.get_json(force=True) ])
	return "Success"

@app.route('/update_data',methods=["PUT"])
def update():
	data = request.get_json(force=True)
	update = table['aion'].update_one({ "name": data['old'] },{ "$set": { "name":data['new'] } })
	return str(update.modified_count)

@app.route('/delete_data',methods=["DELETE"])
def delete():
	delete = table['aion'].delete_one(request.get_json(force=True))
	return "Deleted Successfully"

if __name__ == '__main__':
	if 'test_db' in client.list_database_names():
		if 'test_collections' in client['test'].list_collection_names():
			app.run()
		else:
			print("Create Collection aion........Restart")		
	else:
		print("Create Database test..........Restart")
			





