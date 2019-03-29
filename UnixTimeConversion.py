#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:48:08 2019

@author: alicelee
"""

#convert timezone
import pytz 
from pytz import timezone

from datetime import datetime, timedelta

#nanosecond resolution
time_str=float("1541962108935000000")/10**9

utc=pytz.utc
UTC_time=datetime.utcfromtimestamp(time_str)
UTC_dt=utc.localize(UTC_time)

CERN_tz=timezone('Etc/GMT+1')
CERN_time=UTC_dt.astimezone(CERN_tz)

if __name__=="__main__":
    #UTC time
    print(UTC_time)
    
    #CERN time (EST+1)
    print(CERN_time)
