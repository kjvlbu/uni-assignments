#!/usr/bin/env python3

from statistics import mean

if __name__ == '__main__':

    print("Poppleton Park Run Timer\n~~~~~~~~~~~~~~~~~~~~~~~~\nLet's Go!")

    runner_list = []
    time_list = []

    while True:
        data = (input("> "))
        if data == "END" and len(time_list) == 0:
            print("No data found.")
        elif data == "END":
            print("Total Runners: ", len(runner_list))
            print("Average Time: ", mean(time_list))
            print("Fastest Time: ", min(time_list))
            print("Slowest Time: ", max(time_list))
            print("Best Time Here: Runner #", runner_list[time_list.index(min(time_list))])
        break
