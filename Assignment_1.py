# Problem statement: File Monitoring system
#
# The goal of this task is to design and develop a file monitoring system.
#
# Generate a random writer that writes pseudo strings (with at least 50% probability of generating the “MARUTI”
# # keyword. Note that we are strictly looking at the "MARUTI" keyword only as a single value not the MARUTI keyword
# # inside a random string) into two separate files at regular interval of time.
#
# It should have the capability to monitor both the files and count the total number of occurrences for the “MARUTI”
# keyword by each file and write output to the "counts.log" file.
#

import random
import string
import time


def string_generator():
    op1 = "".join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
    li = ["MARUTI", op1]
    return random.choices(li, weights=[1.1, 1])[0] + " "


counter, f1M, freq1, f2M, freq2, flag = 0, 0, 0, 0, 0, 0

with open("counts.log", "w") as counts:
    while True:
        if counter % 2 == 0:

            pstring = string_generator()

            if pstring == "MARUTI ":
                flag = 1
            else:
                flag = 0

            with open("file1.txt", "a") as f1:
                freq1 += 1
                f1.write(pstring)
                if flag == 1:
                    f1M += 1
        else:

            pstring = string_generator()

            if pstring == "MARUTI ":
                flag = 1
            else:
                flag = 0

            with open("file2.txt", "a") as f2:
                freq2 += 1
                f2.write(pstring)
                if flag == 1:
                    f2M += 1

        counter += 1
        res = "\nCount in File 1: {}/{}\nCount in File 2: {}/{}".format(f1M, freq1, f2M, freq2)
        print(res)
        counts.write(res)
        time.sleep(0.5)
