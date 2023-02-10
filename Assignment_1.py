"""
Problem statement: File Monitoring system

The goal of this task is to design and develop a file monitoring system.

Generate a random writer that writes pseudo strings (with at least 50% probability of generating the "MARUTI"
keyword. Note that we are strictly looking at the "MARUTI" keyword only as a single value not the MARUTI keyword
inside a random string) into two separate files at regular interval of time.

It should have the capability to monitor both the files and count the total number of occurrences for the "MARUTI"
keyword by each file and write output to the "counts.log" file.
"""

import random
import string
from datetime import datetime
import asyncio
import aiofiles
import nest_asyncio

count1, count2 = 0, 0


class FileMonitoringSystem:
    """Initializes and triggers the Event Loop"""

    async def driver_code(self, loop):
        async with aiofiles.open("counts.log", "w") as log_file:
            async with aiofiles.open("file1.txt", "w") as file1:
                async with aiofiles.open("file2.txt", "w") as file2:
                    loop.create_task(self.__file_writer(file2, log_file))
                    loop.create_task(self.__file_writer(file1, log_file))
                    loop.run_forever()

    def __string_generator(self):
        """Generate random string of length in between 5 and 10"""
        op1 = "".join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
        options = ["MARUTI", op1]
        return random.choices(options, weights=[1.1, 1])[0] + " "

    async def __file_writer(self, file_name, log_file):
        while True:
            global count1, count2
            pseudo_string = self.__string_generator()

            # writes the generated string in file
            await file_name.write(pseudo_string)

            # writes the count of "MARUTI" in log file
            if pseudo_string == "MARUTI ":
                if file_name.name == "file1.txt":
                    count1 += 1
                    await log_file.write(
                        f"\n{file_name.name} has MARUTI Keywords " + str(count1) + " times at time " + str(
                            datetime.now()))
                else:
                    count2 += 1
                    await log_file.write(
                        f"\n{file_name.name} has MARUTI Keywords " + str(count2) + " times at time " + str(
                            datetime.now()))
            await asyncio.sleep(0.5)


async def main():
    try:
        run = FileMonitoringSystem()
        loop = asyncio.get_event_loop()
        await run.driver_code(loop)
    except KeyboardInterrupt:
        print("Script Ended")


nest_asyncio.apply()
asyncio.run(main())
