# -*- coding: utf-8 -*-

from __future__ import print_function

import json
import requests
import sys
import sqlite3
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from capstone.app.models import Business
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

API_KEY = 's7qwiM9RQ0la6t6Ji4NtqizS9nb96unAF6lZPwQhbEVOqMl9ecYLnVKqmCGJNGayb3VeERijxGgv8G9n0BbvF4i7zhAuNjTxYIq7LOI0tZiimIZDeomsVSm7AEUmY3Yx'

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

# Defaults
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Glassboro, NJ'
SEARCH_LIMIT = 3
OFFSET = 0


def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': OFFSET
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(request, term, location):
    
    print("query_api", term, location)
    response = search(API_KEY, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    response = get_business(API_KEY, business_id)

    write_to_file = json.dumps([response], indent=4)

    with open('app/API/YelpAPI/yelp.json', 'w') as f:
        f.write(write_to_file)
    
    return HttpResponse("OK")
    #return render(request, 'app/yelp.html', dic)

def db():
    
    with open('app/API/YelpAPI/yelp.json', 'r') as f:
        data = json.load(f)

    conn = sqlite3.connect('capstone/db.sqlite3')
    cur = conn.cursor()
        # Create the table if it doesn't exist.
    cur.execute(
        """CREATE TABLE IF NOT EXISTS Business(
                id INTEGER PRIMARY KEY,
                business_id varchar(100),
                business_name varchar(100),
                yelp_business_id varchar(254),
                phone varchar(15),
                city varchar(100),
                state varchar(20),
                address varchar(100),
                postal_code varchar(15),
                latitude float(100),
                longitude float(100),
                business_stars float(10),
                business_review_count integer(10),
                is_open integer(1)
            );"""
    )
    
    business_id = data[0]['id']
    business_name = data[0]['name']
    yelp_business_id = data[0]['alias']
    phone = data[0]['phone']
    city = data[0]['location']['city']
    state = data[0]['location']['state']
    address = data[0]['location']['address1']
    postal_code = data[0]['location']['zip_code']
    latitude = data[0]['coordinates']['latitude']
    longitude = data[0]['coordinates']['longitude']
    business_stars = data[0]['rating']
    business_review_count = data[0]['review_count']
    is_open = data[0]['hours'][0]['is_open_now']
        
    # Execute the command and replace '?' with the each value
    # in 'values'. DO NOT build a string and replace manually.
    # the sqlite3 library will handle non safe strings by doing this.
    sql = '''INSERT INTO Business (business_id, business_name, yelp_business_id, phone, city,  state, address, postal_code, latitude, longitude, business_stars, business_review_count, is_open) VALUES(
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            );'''
    cur.execute(sql, (business_id, business_name, yelp_business_id, phone, city, state, address, postal_code, latitude, longitude, business_stars, business_review_count, is_open, ))

    conn.commit()
    conn.close()

@csrf_exempt
def yelp_main(request):
    term = request.POST.get('term')
    location = request.POST.get('location')
    db()
    query_api(request, term, location)
    return HttpResponse("OK")