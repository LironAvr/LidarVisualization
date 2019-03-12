# -*- coding: utf-8 -*-
from config import *
import pickle,csv


### Define which data will be loaded
DATA = "mal"
###


### Define Data Format
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
### End Define Data Format


data = Data()
data.read_data(DATA)
with open(DATA+'.csv', "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for i in data._scans:
        for j in range(0, 360):
            csvwriter.writerow([j,i.distances[j], i.errors[j], i.intensities[j]])
