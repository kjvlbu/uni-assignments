#!usr/bin/env python3

from statistics import mean

def convert(seconds):
    seconds = int(seconds) % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d minutes, %02d seconds" % (minutes, seconds)

if __name__ == '__main__':

    print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")

    runner_list = []
    time_list = []

    while True:
        data = input("> ")
        runner_info = data.split("::")
        if data == "END" and len(runner_list) == 0 and len(time_list) == 0:
            print("Error. No data found.")
            exit()
        if data == "END":
            break
        elif runner_info[0] == "" or runner_info[1] == "":
            print("Error in the data stream. Please continue.")
        else:
            runner_list.append(int(runner_info[0]))
            time_list.append(int(runner_info[1]))

print("Total Runners:", len(runner_list))
print("Average Time:", convert(mean(time_list)))
print("Fastest Time:", convert(min(time_list)))
print("Slowest Time:", convert(max(time_list)))
print("Best Time Here: Runner #", runner_list[time_list.index(min(time_list))])
