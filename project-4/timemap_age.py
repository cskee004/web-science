import json 
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np

collection_date = datetime.strptime('2024-10-16', '%Y-%m-%d')

ages = []
mementos_count = []


def parse_maps():
    
    for name in os.listdir(r"./time-maps"):
        file_path = os.path.join(r"./time-maps", name)
        file_size = os.path.getsize(file_path)
        
        if file_size > 0:
            temp_list = []
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
                
                for memento in data['mementos']['list']:
                    memento_datetime = datetime.strptime(memento['datetime'], '%Y-%m-%dT%H:%M:%SZ')
                    temp_list.append(memento_datetime)
                    
            num_mementos = len(temp_list)
            
            if num_mementos > 0:
                earliest_memento = min(temp_list)
                
                age = (collection_date - earliest_memento).days
                
                ages.append(age)
                mementos_count.append(num_mementos)
    
def build_scatter_plot():
    a = np.asarray(ages)
    b = np.asarray(mementos_count)
    
    fig, ax = plt.subplots()
    ax.scatter(a, b)
    
    
    plt.title('Datetime of Mementos')
    plt.xlabel('Age in Days')
    plt.ylabel('Number of Mementos')
    plt.grid(True)
    plt.minorticks_on()
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    plt.show()

file_types = [    
    'HTML',
    'Images',
    'Audio/Visual',
    'Javascript',
    'CSS',
    'Fonts',
    'Plaintext',
    'JSON'
]

file_results = [   
    308,
    9404,
    7,
    369,
    249,
    69,
    5,
    93
]

def build_bar_chart(file_type, file_results):
    a = np.asarray(file_type)
    b = np.asarray(file_results)
    
    fig = plt.figure(figsize=(10,5))
    
    plt.bar(a, b)
    plt.xlabel('File Types')
    plt.ylabel('Numer of Files')
    plt.show()
    
parse_maps()
