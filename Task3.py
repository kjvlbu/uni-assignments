#!/usr/bin/env python3

import random
import sys
import re

if __name__ == '__main__':

    try:
        with open("students.txt", 'r') as f0:
            students = f0.readlines()

        with open("student_emails.txt", 'w') as f1:
            for student in students:

                full_name = student[9:]
                name_split = full_name.split(", ")
                first_name = name_split[1]

                ucas_num = student[:8]
                initial = first_name[0]
                surname = re.sub(r"[^a-zA-Z]", "", name_split[0])
                rand_num = random.randint(1000, 9999)

                emails = f"{initial}.{surname}{rand_num}@poppleton.ac.uk"

                f1.write(ucas_num + " " + emails.lower() + "\n")

        f0.close()
        f1.close()

        print("Success! Process completed.")

    except FileNotFoundError:
        print("Error. File cannot be located")

        sys.exit(1)
