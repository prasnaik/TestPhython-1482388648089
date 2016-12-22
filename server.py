import os
import pymongo
import ssl
import json  
from pymongo import MongoClient
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')
# VCAP_SERVICES mapping Start

services = os.getenv('VCAP_SERVICES')
services_json = json.loads(services)
mongodb_url = services_json['compose-for-mongodb'][0]['credentials']['uri']
#connect:
client = MongoClient(mongodb_url)  
#get the default database:
#db = client.get_default_database()  
#db = client.test
db = client.Employees

# Function to insert data into mongo db
def insert():
    try:
    employeeId = raw_input('839441 :')
    employeeName = raw_input('prashant :')
    employeeAge = raw_input('34 :')
    employeeCountry = raw_input('India :')
        
    db.Employees.insert_one(
        {
        "id": employeeId,
            "name":employeeName,
        "age":employeeAge,
        "country":employeeCountry
        })
        print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)



print('connected to mongodb!, welcome to mongodb connection, have a fun and bit relax')
#db.test_collection.insert({}) 

# VCAP_SERVICES mapping END
httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

