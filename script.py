#!/usr/bin/python3
import sys
import json
import argparse

CHIP_NAME = "nct6793-isa-0290"
VOLTAGE_CATEGORY = "+12V"
VOLTAGE_ENTRY_SUFFIX = "_input"
THRESHOLD = 11.5

def low_voltage_action():
    print('Low voltage action not defined.')
    pass

def main():
    # reads historical data
    try:
        f = open('status.txt', 'r')
        warning_count = int(f.readline())
        print('current status:', warning_count)
        f.close()
    except:
        warning_count = 0

    state_file = open("status.txt", 'w')

    # read json file
    with open('example.json', 'r') as f:
        sensors_info = json.load(f)
    voltages = sensors_info[CHIP_NAME][VOLTAGE_CATEGORY]
    for key, value in voltages.items():
        if key.endswith(VOLTAGE_ENTRY_SUFFIX):
            print('voltage:', value)
            if value < THRESHOLD:
                if warning_count == 0:
                    print('state change: 0->1')
                    state_file.write('1')
                elif warning_count == 1:
                    print('state change: 1->2')
                    state_file.write('2')
                elif warning_count == 2:
                    print('hit threshold for 3 calls, calling low_voltage_action')
                    state_file.write('2')
                    low_voltage_action()
            else:
                state_file.write('0')
    state_file.close()

main()
