import csv
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#cmat=pd.read_csv('Network-Dietary-combined.csv', header=0)

cmat='Dietary_AllKOs_forNetwork.csv' #open file

#convert file into a numpy array
#np.corrcoef takes each row of an array and treats it like a different feature
with open(cmat, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader)).astype(float)

print(data)

###cmat.to_csv('cmat')

outts = np.corrcoef(data).round(decimals=2) #use the array to calculate pearson's r 
pdmatrix=pd.DataFrame(outts) 
print(pdmatrix)
pdmatrix.to_csv('matrix')

g=nx.Graph(outts) #creates network

nx.write_gexf(g, 'Dietary-AllKOs-GEPHI.gexf')
