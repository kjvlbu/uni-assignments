#!usr/bin/env python3

if __name__ == '__main__':

    print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")

    runner_list = []
    time_list = []

    while True:
        data = input("> ")
        runner_info = data.split("::")
        if not data == "END":
            runner_list.append(runner_info[0])
            time_list.append(runner_info[1])
        elif data == "END" and len(runner_list) == 0 and len(time_list) == 0:
            print("Error. No data found.")
        elif runner_info[0] == "" or runner_info[1] == "":
            print("Error in data stream.")
        elif data == "END" and not len(runner_list) == 0 and not len(time_list) == 0:
            print("Total Runners: ", len(runner_list))
