#Write a Python program to get the Python version you are using

import sys
print("Python verions: ", sys.version)
print("Version info: ", sys.version_info)

#Write a Python program to display the current date and time.

from datetime import datetime
now = datetime.now()
date_current = now.strftime("%m/%d/%Y")
time_current = now.strftime("%H:%M:%S")
print(f"current date: {date_current}, current time: {time_current}".format())