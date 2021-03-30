from __future__ import print_function
import requests
import json
import cv2

#test_url = 'http://aakashveera.pythonanywhere.com/soil_predict'

headers = {'Content-type': 'multipart/form-data'}

files = [
    ('image', ("data.jpg", open("/users/pc/Desktop/data.jpg", 'rb'), 'application/octet'))
]

response = requests.post('http://localhost:5000/soil_predict', files=files)

print(response.text)