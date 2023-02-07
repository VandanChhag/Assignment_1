# Problem statement: File Monitoring system
#
# The goal of this task is to design and develop a file monitoring system.
#
# Generate a random writer that writes pseudo strings (with at least 50% probability of generating the “MARUTI”
# keyword. Note that we are strictly looking at the "MARUTI" keyword only as a single value not the MARUTI keyword
# inside a random string) into two separate files at regular interval of time.
#
# It should have the capability to monitor both the files and count the total number of occurrences for the “MARUTI”
# keyword by each file and write output to the "counts.log" file.
#

import random
import string
from datetime import datetime
import asyncio

c1,c2= 0,0

def string_generator():
    op1 = "".join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
    li = ["MARUTI", op1]
    return random.choices(li, weights=[1.1, 1])[0] + " "


async def f1writer(loop):
    global c1
    with open("file1.txt", "a") as f1:
        pstring = string_generator()
        f1.write(pstring)
        if pstring == "MARUTI ":
            c1 += 1
            with open("counts.log", "a") as count:
                count.write("\nFile 1 has MARUTI Keywords " + str(c1) + " times at time " + str(datetime.now()))
    await asyncio.sleep(0.5)
    return (await f1writer(loop))


async def f2writer(loop):
    global c2
    with open("file2.txt", "a") as f2:
        pstring = string_generator()
        f2.write(pstring)
        if pstring == "MARUTI ":
            c2 += 1
            with open("counts.log", "a") as count:
                count.write("\nFile 2 has MARUTI Keywords " + str(c2) + " times at time " + str(datetime.now()))
    await asyncio.sleep(0.5)
    return (await f2writer(loop))


loop = asyncio.get_event_loop()
loop.create_task(f1writer(loop))
loop.create_task(f2writer(loop))
loop.run_forever()