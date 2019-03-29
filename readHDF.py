#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:28:13 2019

@author: alicelee
"""

import h5py
import csv

datasetCSV="dataset.csv"
file= h5py.File('1541962108935000000_167_838.h5', 'r')
nameList=[[]]

def datasetParameters(dataset, datasetCSV):
    with open(datasetCSV, 'a') as csvfile:
        filewriter = csv.writer(csvfile)
        l=[dataset.name, dataset.shape,dataset.size]
        filewriter.writerow(l)
    return

def search(current, level, nameList):
    
    if (isinstance(current, h5py._hl.dataset.Dataset)):
        datasetParameters(current, datasetCSV)
        return
    
    elif(isinstance(current, h5py._hl.datatype.Datatype)):
        return
    
    keys=list(current.keys())
    l_k=len(keys)
    
    for i in range(l_k):
        if(isinstance(current[keys[i]], h5py._hl.dataset.Dataset)):
            datasetParameters(current[keys[i]], datasetCSV)
    
    l_nameList=len(nameList)
    if (level+1>l_nameList):
        nameList.append([])
    
    for key in current.keys():
        nameList[level].append(key)
        search(current[key], level+1, nameList)
    return

#lv2=lv1['Acquisition']
#lv3=lv2['currentAverage']#dataset
#test object 'RPCAH.TSG4.RQIF.430034'

if __name__=="__main__":
    current=file
    branches="branch.csv"
    search(current, 1, nameList)
    with open(branches, 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(len(nameList)):
            filewriter.writerow(nameList[i])
