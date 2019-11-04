import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, pymongo, MongoClient
from bson.objectid import ObjectId
from pprint import pprint

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestoneproject3me'
app.config["MONGO_URI"] = 'mongodb+srv://Neil:BrooklynWooD@myfirstcluster-lxpo1.mongodb.net/milestone_3retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/activities', methods=['GET'])
def activities():
    
    activity = mongo.db.Activities
    
    activities = activity.find().sort('_id', pymongo.ASCENDING)
    
    output = []
    
    for i in activities:
        output.append({'activity' : i['activity']})
        
    return jsonify({'result' : output, 'prev_url' : '', 'next_url' : ''})

if __name__ == "__main__":
    app.run(debug=True)