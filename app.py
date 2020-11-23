import os
import pymongo
from flask import Flask, render_template
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://bruhtus:insert_password_here@cluster0.chq4a.mongodb.net/<dbname>?retryWrites=true&w=majority")
#db = client.test

'''db = client.mongodb_basic #creating database
students = [
        {'name': 'anu', 'country': 'japan', 'city': 'tokyo', 'age': 69},
        {'name': 'itu', 'country': 'japan', 'city': 'kumamoto', 'age': 69},
        {'name': 'anumu', 'country': 'indo', 'city': 'surabaya', 'age': 69},
        ]

for student in students: #creating students collection and inserting document
    db.students.insert_one(student)'''

#print(client.list_database_names())

db = client['mongodb_basic'] #accessing the database
#db.students.insert_one({'name':'itumu', 'country':'indo', 'city':'surabaya', 'age':20})

#student = db.students.find_one({'_id':ObjectId('5fbb1352fbdec51ce5600498')})
#students = db.students.find({}, {'_id':0, 'name':1, 'age':1}) #0 means not include and 1 means include
'''query = {'age':{'$gt':30}} #more than 30
#students = db.students.find({'country': 'japan'})
students = db.students.find(query)'''
#students = db.students.find().limit(2)

#students = db.students.find().sort('name', -1) #decending
#students = db.students.find().sort('name') #ascending
#students = db.students.find().sort('country', -1) #decending

'''query = {'name':'itu'}
new_value = {'$set':{'age':49}}
db.students.update_one(query, new_value) #modified the age
students = db.students.find()'''

#db.students.drop() #delete students collection from a database

query = {'name':'itumu'}
db.students.delete_one(query)
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
