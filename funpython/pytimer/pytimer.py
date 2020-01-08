#This is a simple python script to track our daily time, all recorded data are stored locally
#By Renkun Kuang, on Jan 06, 2020

import time
import sys

def add_a_record():
    localtime = time.localtime(time.time())
    # print ("本地时间为 :", localtime)
    print(localtime.tm_year)
    year = localtime.tm_year
    mon = localtime.tm_mon
    mday = localtime.tm_mday

