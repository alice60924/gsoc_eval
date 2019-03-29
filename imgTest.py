#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:01:48 2019

@author: alicelee
"""

import h5py
from numpy import reshape
from scipy import signal
from matplotlib import pyplot as plt

def goToImage(file, imgAddress, imgW, imgH, depth):
    current_f=file
    h=file
    w=file
    
    for i in range(4):
        current_f=current_f[imgAddress[i]]
        h=h[imgH[i]]
        w=w[imgW[i]]
    
    return [current_f, h, w]


if __name__=="__main__":
    file= h5py.File('1541962108935000000_167_838.h5', 'r')

    #3 Group in the lst layer: ['AwakeEventData', 'AwakeEventInfo', '__DATA_TYPES__']
    imgAddress=['AwakeEventData', 'XMPP-STREAK', 'StreakImage', 'streakImageData']
    imgH=['AwakeEventData','XMPP-STREAK','StreakImage', 'streakImageHeight']
    imgW=['AwakeEventData','XMPP-STREAK','StreakImage','streakImageWidth']
    depth=len(imgAddress)
    
    destinations=goToImage(file,imgAddress, imgW, imgH, depth)
    
    reshaped=reshape(destinations[0], [destinations[1][0], destinations[2][0]])
    
    reshaped=signal.medfilt(reshaped)
    plt.plot(reshaped)
    plt.savefig('Evaluation.png')