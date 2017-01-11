from os import listdir
import numpy as np
import pickle

files =[i for i in listdir('data') if '.csv' in i]
snapshots = [np.genfromtxt('data/'+file, delimiter=',', dtype=None, names=True) for  file in files]
stars_that_leave = []
for i in range(1,len(snapshots)):
    print('*'*8)
    print('Snapshot: ', i)
    print('Current Number of stars: ', snapshots[i].shape[0])
    tmp = set(list(snapshots[i]['id']))-set(list(snapshots[i-1]['id']))
    if len(tmp)!=0:
        print('Stars That left: ', tmp)
    stars_that_leave = stars_that_leave + list(tmp)

stars_that_leave = list(set(stars_that_leave))

with open('code/pickles/stars_that_leave.pkl', 'wb') as fp:
    pickle.dump(stars_that_leave, fp)