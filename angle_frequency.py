import pickle

### Define which data will be loaded
DATA = "benign_7"
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

    def read_data(self, name):
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


### End Define Data Format

# Data 0
train_x = []
data = Data()
data.read_data('benign_7')
for i in data._scans:
    train_x_x = []
    for j in range(0, 360):
        train_x_x.append([i.distances[j], i.errors[j], i.intensities[j]])
    train_x.append(train_x_x)

a = []
for i in range(0, 360):
    a.append(0)

for i in train_x:
    for j in range(0, 360):
        if i[j][1] > 0:
            a[j] += 1
b = {}
c = []
for i in range(len(a)):
    if a[i] != '':
        if a[i] not in c:
            c.append(a[i])
        b[str(i)] = a[i]

c.sort()
c.reverse()
d = {}
for i in c:
    e = []
    for j in range(len(a)):
        if a[j] == i:
            e.append(j)
    d[i] = e

for i in c:
    print(str(d[i]) + ':' + str(i) + ' times')

ignore = []
ignore1 = []
for i in c:
    if i >= 1:
        ignore += d[i]
    else:
        ignore1 += d[i]
