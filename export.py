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
import pickle,csv


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
            for i in range(49, 50):
                filename = 'mal_3/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign1':
            for i in range(114, 223):
                filename = 'benign1/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'benign_4':
            for i in range(114, 223):
                filename = 'benign_4/ldscan' + str(i) + '.pkl'
                scan = read_file(filename)
                self._scans.append(scan)

        if name == 'current':
            filename = 'ldscan_current.pkl'
            scan = read_file(filename)
            self._scans.append(scan)

train_x=[]
data = Data()
data.read_data('mal_3')
with open('mal.csv', "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for i in data._scans:
        for j in range(0, 360):
            csvwriter.writerow([j,i.distances[j], i.errors[j], i.intensities[j]])
