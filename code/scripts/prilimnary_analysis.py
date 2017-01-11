from os import listdir
import pandas as pd



files =[i for i in listdir('data') if '.csv' in i]
snapshots = [pd.read_csv(file) for  file in files]


