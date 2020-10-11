#!/usr/bin/python3
import sys
import json

CHIP_NAME = "nct6793-isa-0290"
VOLTAGE = "+12V"
ENDSWITH = "_input"

# reads historical data

f = open('status.txt', 'r')
line = f.readline()
print('current status:', line)
f.close()

to_file = open("status.txt", 'w')

# read json file
with open('example.json', 'r') as f:
    data1 = json.load(f)
data2 = data1[CHIP_NAME][VOLTAGE]
for key, value in data2.items():
    if key.endswith(ENDSWITH):
        if value > 11.5:
            print('voltage: ', value)
            if line == '0':
                print('0->1')
                to_file.write('1')
            elif line == '1':
                print('1->2')
                to_file.write('2')
            elif line == '2':
                print('calling callback')
                to_file.write('2')
        else:
            to_file.write('0')
to_file.close()

