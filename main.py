# -*- coding: utf-8 -*-
from config import *
# import StringIO
# import hashlib
# import os
# import random
# import re
# import sys
# from html_decode_support import stringToConvert
# import uuid
# import re
# import urllib2
# from random import randint
# from urlparse import urlparse
# import time
# import oauth2
# import urllib2
# import requests
# from bs4 import BeautifulSoup
# from docx import Document
# from docx.shared import Inches
# from docxtpl import DocxTemplate, InlineImage, R
# from elasticsearch import Elasticsearch
from flask import *
# from flask_httpauth import HTTPBasicAuth
# from extensions import *
# from sqlite import *
# from es import *
import pickle


class LidarScan:
    def __init__(self, ldscan):
        self.distances = []
        self.intensities = []
        self.errors = []

        for i in range(0, len(ldscan)):
            response = ldscan[i].strip()
            if len(response) < 1:
                break
            lst = response.split(',')
            if len(lst) < 4:
                continue
            if lst[0].lower() == 'AngleInDegrees'.lower():
                continue
            if lst[0] == 'ROTATION_SPEED':
                self.rotation = float(lst[1])
                continue
            angle = int(lst[0])
            if -1 < angle < 360 and len(lst) > 2:
                self.distances.append(int(lst[1]))
                self.intensities.append(int(lst[2]))
                self.errors.append(int(lst[3]))
                continue
            print(self)

def read_file(filename):
    output = open(filename, 'rb')
    a = pickle.load(output)
    output.close()
    return a


class Data:
    def __init__(self):
        self.benign_scans = []
        self.malicious_scans = []
        self._scans = []
    def read_data(self,name):
        print(name)
        if name == 'benign':
            for i in range(0, 303):
                filename = 'benign/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'reflective':
            for i in range(379, 1152):
                filename = 'reflective/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'mal':
            for i in range(305, 550):
                filename = 'Mal/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'mal1':
            for i in range(0, 113):
                filename = 'mal1/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'mal_3':
            for i in range(13, 124):
                filename = 'mal_3/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign1':
            for i in range(114, 223):
                filename = 'benign1/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign_4':
            for i in range(720, 943):
                filename = 'benign_4/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign_6':
            for i in range(318, 538):
                filename = 'benign_6/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign_7':
            for i in range(11, 1310):
                filename = 'benign_7/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'mal_6':
            for i in range(539, 761):
                filename = 'mal_6/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'current':
            filename = 'ldscan_current.pkl'
            scan = read_file(filename)
            self._scans.append(scan)
# Data 0
train_x=[]
data = Data()
data.read_data('benign_7')
for i in data._scans:
    train_x_x = []
    for j in range(0, 360):
        train_x_x.append([i.distances[j], i.errors[j], i.intensities[j]])
    train_x.append(train_x_x)

# Data 1
train_x1=[]
data1 = Data()
data1.read_data('mal1')
for i in data1._scans:
    train_x_x = []
    for j in range(0, 360):
        train_x_x.append([i.distances[j], i.errors[j], i.intensities[j]])
    train_x1.append(train_x_x)

# Nạp hai mẫu so sánh
sample1 = train_x[0]
sample2 = train_x1[0]
samples = []
samples.append(sample1)
samples.append(sample2)
# Main program
# Define web
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "fasdfsdfsdfasdfs"
# app update
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='[[',
    variable_end_string=']]'
))
app.jinja_options = jinja_options

# Routing index
@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# Trang so sánh hai mẫu lidar
@app.route('/compare', methods=['POST', 'GET'])
def compare():
    return render_template('compare.html')

# Trang tính toán
@app.route('/statistic', methods=['POST', 'GET'])
def statistic():
    return render_template('statistic.html')

# API Lấy thông tin lidar
@app.route('/get_data_api', methods=['POST', 'GET'])
def get_data_api():
    if request.method == 'POST':
        return json.dumps(train_x)
    return 'nothing'

# API Lấy thông tin hai mẫu so sánh
@app.route('/get_compare_data_api', methods=['POST', 'GET'])
def get_compare_data_api():
    if request.method == 'POST':
        return json.dumps(samples)
    return 'nothing'

# App run
app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)