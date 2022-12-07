from django.http.request import HttpRequest
import requests
import json
import sys
import sqlite3
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from app.models import Business
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
def nutritioncode(input):
    headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
    }
    json_data = {
        'appId': '1b96f64f',
        'appKey': 'f526efa32f0ab250fffe67daca343ec8',
        'query': input,
        "offset": 0,
        "limit": 50,
        "filters":{
        "item_type":1
        }
    }

    response = requests.post('https://api.nutritionix.com/v1_1/search', headers=headers, json=json_data)
    #print(response.json())

    responseJson = response.json() #this is what I get back
    output = json.dumps([responseJson],indent = 3)

    with open('app/API/SanjayAPI/nutrinix.json', 'w') as f:
        f.write(output)
    db()
    return HttpResponse("OK")

def db():
    with open('app/API/SanjayAPI/nutrinix.json', 'r') as f:        
       data = json.load(f)

    conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Food_Items(
            id INTEGER PRIMARY KEY,
            item_id text(100),
            item_name text(100),
            resturaunt_name text(100)
        );"""
    )
    num_results = len(data[0]["hits"])
    
    for i in range(num_results):
        #print(data[0]["hits"][i]["fields"]["item_name"])
        item_id=data[0]["hits"][i]["fields"]["item_id"]
        item_name=data[0]["hits"][i]["fields"]["item_name"]
        resturaunt_name=data[0]["hits"][i]["fields"]["brand_name"]
        sql = '''INSERT or REPLACE INTO Food_Items (item_id, item_name, resturaunt_name) VALUES(
                ?,
                ?,
                ?
            );'''
        cur.execute(sql, (item_id, item_name, resturaunt_name, ))

    #print(uno)
        conn.commit()#
    conn.close()