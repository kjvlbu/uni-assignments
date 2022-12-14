#!usr/bin/env python3

import sys
import random


if __name__ == '__main__':

    ucas_num = []
    stu_initial = []
    last_name = []

    try:
        with open("students.txt", 'r') as f:
            students = f.readlines()

        with open("student_emails.txt", 'w') as f:
            for student in students:

                stu_family_name = student.split(", ")

                ucas_num.append(student[:8])
                stu_initial.append(student[9])
                last_name.append(stu_family_name[1])
                random_number = random.randint(1000, 9999)

                stu_email = f"{stu_initial}.{last_name}{random_number}@poppleton.ac.uk"

                f.write(ucas_num + stu_email.lower())

    except FileNotFoundError:
        print("Error: File cannot be located.")

        sys.exit(1)
