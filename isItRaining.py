import json
import urllib.request
import flask as Flask

# class AstroPhoto:
#     def __init__(self, data):
#         self.title = data["title"]
#         self.date = data["date"]
#         self.description = data["explanation"]
#         self.url = data["hdurl"]
#
#     # new method
#     def get_short_description(self):
#         if len(self.description) <= 200:
#             return self.description
#         else:
#             return (self.description[0:197] + "...")
#
# def get_apod(api_key):
#     url = "https://api.nasa.gov/planetary/apod?api_key={}".format(api_key)
#     with urllib.request.urlopen(url) as request:
#         response = request.read().decode()
#
#     return AstroPhoto(json.loads(response))
#
# # Test code
# apod_instance = get_apod("DEMO_KEY")
# print("Title: {}".format(apod_instance.title))
# print("Description: {}".format(apod_instance.get_short_description()))
#
#
# def get_random_apods(api_key, count):
#     url = "https://api.nasa.gov/planetary/apod?api_key={}&count={}".format(api_key, count)
#     with urllib.request.urlopen(url) as request:
#         response = request.read().decode()
#
#     photos = []
#
#     for item in json.loads(response):
#         # Each item in the list is an APOD dictionary
#         # We create a new instance of AstroPhoto using
#         # the dictionary, and then append it to photos
#         photos.append(AstroPhoto(item))
#
#     return photos
#
#
# # Test code
# # Should print 2
# apods = get_random_apods("DEMO_KEY", 2)
# print(len(apods))
#
# def get_apods_between(api_key, start_date, end_date):
#     url = ("https://api.nasa.gov/planetary/apod?api_key={}&start_date={}&end_date={}.format(api_key, start_date, end_date")
#     with urllib.request.urlopen(url) as request:
#         response = request.read().decode()

from flask import Flask, render_template, request, redirect, url_for, jsonify

def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        # print("Yes!")
        return True
    else:
        # print("No!")
        return False

if is_it_raining_in_seattle == "true":
    print("Yes!")
else:
    print("No!")