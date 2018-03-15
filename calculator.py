#!/usr/bin/env python3

import sys

try:
    ys = int(sys.argv[1]) - 3500
except:
    print('Parameter Error') 
if ys <= 1500:
    print(format((ys*0.03-0),'.2f'))
elif 1500 < ys <= 4500:
    print(format((ys*0.1-105),'.2f'))
elif 4500 < ys <= 9000:
    print(format((ys*0.2-555),'.2f')) 
elif 9000 < ys <= 35000:
    print(format((ys*0.25-1005),'.2f'))
elif 35000 < ys <= 55000:
    print(format((ys*0.3-2755),'2f'))
elif 55000 < ys <= 80000:
    print(format((ys*0.35-5505),'2f'))
elif ys > 80000:
    print(format((ys*0.45-13505),'.2f'))

