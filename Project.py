import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    mark_list = []
    attendence_list = []

    with open(data_path) as f:
        reader = csv.DictReader(f)

        for i in reader:
            mark_list.append(float(i['Marks In Percentage']))
            attendence_list.append(float(i['Days Present']))
        return {'x':mark_list,'y':attendence_list}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path = './Student Marks vs Days Present.csv'
    data_source = getDataSource(data_path)
    find_correlation(data_source)
setup()