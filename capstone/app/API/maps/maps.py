import urllib.request
import json
import os
import pymysql
import pyodbc
import sqlite3

#Connect to Database
conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()
        # Create the table if it doesn't exist.
    cur.execute(
        """CREATE TABLE IF NOT EXISTS MAPS(
                id INTEGER PRIMARY KEY,
                Resname varchar(100),
                Address varchar(100),
                Latitude varchar(100),
                Longitude varchar(100),
            );"""
    )
    

# Create URL string
url = "https://maps.googleapis.com/maps/api/place/textsearch/json" 
params = { 
    "query": "burger", 
    "location": "39.826781,-75.015446",
    "radius": "1000",
    "region": "US",
    "type": "restaurant",
    "key": "AIzaSyD22ufr_NRQ6SRyaPjjZWlc5M5WttvjjsE"
}    
query_string = urllib.parse.urlencode( params ) 
url = url + "?" + query_string
headers = {"Content-Type": "application/json"}
print (url)
print()
response = urllib.request.urlopen(url)
data = response.read().decode('UTF-8')

#Write Json data to file to examine
file = open("data.json","w")
file.write(data)
file.close()

#Open Json Data
with open('data.json') as f:
  data = json.load(f)

#loop through the data and assign to variables
for i, item in enumerate(data):
    name=data['results'][i]["name"]
    add=data['results'][i]["formatted_address"]
    lat=data['results'][i]["geometry"]["location"]["lat"]
    long=data['results'][i]["geometry"]["location"]["lng"]

    #insert found variables into database
    cursor.execute("INSERT INTO Maps (Resname, Address, Latitude, Longitude) VALUES(?,?,?,?)",(name, add, lat, long))
    cursor.commit()

# CODE to dispay data in the table
cursor.execute("select Resname, Address, Latitude, Longitude from Maps")
row = cursor.fetchone()
while row:
    print(row[0], row[1], row[2], row[3])
    row = cursor.fetchone()

#Close the database connection
conn.close()
print('Your database connetion has been closed.')
