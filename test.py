from operator import itemgetter
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


        if name == 'benign_7':
            for i in range(11, 1310):
                filename = 'benign_7/ldscan' + str(i) + '.pkl'
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

# Khởi tạo a
a = []
for i in range(0,360):
    a.append(0)



for i in train_x:
    for j in range(0,360):
        if i[j][1] > 0:
            a[j] += 1
# a = [98, '', 42, 3, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
#      '', '', '', '', '', 220, 220, 220, 220, 220, 220, 220, 195, 2, 22, '', 49, 206, 220, 220, 220, 220,
#      219, 40, 18, 6, '', '', 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 2, 14,
#      '', '', '', '', '', '', '', '', 8, '', '', '', '', '', '', '', '', '', 220, 220,
#      220, 220, 220, 220, 220, 220, 30, 11, 220, '', '', '', 42, '', '', '', '', '', '', '', '',
#      '', '', '', '', '', '', '', '', '', '', '', '', '', 220, '', 41, '', '', '', 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220,
#      220, 220, 220, 220, 220, 220, 220, 220, 1, 2, '', 220, '', '', '', '', '', '', '', '', '',
#      '', 220, '', 123, '', 32, '', '', '', '', '', '', '', '', '', 220, 220, 220, 220, '',
#      '', '', '', '', '', '', '', 171, '', '', 3, 206, 220, 220, 220, 220, 220, 122, 10, 5, '', '',
#      166, 220, 220, 220, 220, 220, 220, 220, 2, 89, 4, '', '', '', '', '', '', '', '', 5, 220, 220, 220,
#      220, 220, 220, 220, 197, 10, 27, '', '', '', 219, 220, 220, 220, 6, 11]
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
    print(str(i) + ' times:' + str(d[i]))

ignore = []
ignore1 = []
for i in c:
    if i>=1:
        ignore+=d[i]
    else:
        ignore1+=d[i]

print('ignore: ')
print(ignore)
print('ignore1:')
print(ignore1)