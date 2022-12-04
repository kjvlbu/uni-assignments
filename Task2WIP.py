#!/usr/bin/env python3

from statistics import mean

if __name__ == '__main__':

    print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")

    runner_list = []
    time_list = []

    while 1:
        data = input("> ")
        runner_info = data.split("::")
        listlengths = len(runner_info)
        if data == "END" and len(time_list) == 0:
            print("Error. No data found.")
        elif listlengths != 2 or runner_info[0] == "" or runner_info[1] == "":
            print("Error in data stream. Ignoring. Proceed.")
        else:
            runner_list.append(runner_info[0])
            time_list.append(runner_info[1])
    
