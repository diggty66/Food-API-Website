import sqlite3
import requests
import sys
import json
non_bmp_map =dict.fromkeys(range (0x10000, sys.maxunicode+1), 0xfffd)


def foodnutritioncode(Macroinput):


    query = input(Macroinput)
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'
    response = requests.get(api_url, headers={'X-Api-Key': '94NlwilwGgEF0vQlagmVag==spsVNqhqSR9o5iTg'})
    if response.status_code == requests.codes.ok:
        print(response.json())

    else:
        print("Error:", response.status_code, response.text)



    data = json.loads(response.text)


    conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()

    cur.execute(
    """CREATE TABLE IF NOT EXISTS NutritionFix(
    id INTEGER PRIMARY KEY,
    name varchar(50),
    calories varchar(50),
    serving_size_g varchar(50),
    fat_total_g varchar(50),
    fat_saturated_g varchar(50),
    protein_g varchar(50),
    sodium_mg varchar(50),
    potassium_mg varchar(25),
    cholesterol_mg varchar(25),
    carbohydrates_total_g varchar(25),
    fiber_g varchar(25),
    sugar_g varchar(25)
    );"""
    )
   
    for value in data:
        qname = value['name'].translate(non_bmp_map)
    qcalories =value['calories']
    qserving = value['serving_size_g']
    qfattotal = value['fat_total_g']
    qfatsat = value['fat_saturated_g']
    qprotein = value['protein_g']
    qsodium = value['sodium_mg']
    qpotassium = value['potassium_mg']
    qcholesterol =value['cholesterol_mg']
    qcarb = value['carbohydrates_total_g']
    qfibe = value['fiber_g']
    qsugar = value['sugar_g']
    sql = '''INSERT INTO NutritionFix(Name, calories, serving_size_g, fat_total_g, fat_saturated_g, protein_g, sodium_mg, potassium_mg, cholesterol_mg, carbohydrates_total_g, fiber_g, sugar_g) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur.execute(sql,(qname, qcalories, qserving, qfattotal, qfatsat, qprotein, qsodium, qpotassium, qcholesterol, qcarb, qfibe, qsugar))
    
    conn.commit()
    conn.close()

print("records inserted")

