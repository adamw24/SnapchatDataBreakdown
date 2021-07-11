import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import GeneralSnapDataBreakdown as gsd
import datetime

# Use pandas to parse the downloaded snapchat data into tables.

dict_From = {}
dict_To = {}


def parseCountsPerDay(table, dictF, dictT):
    for entry in table[0]["Created"]:
        date = datetime.datetime.strptime(
            entry[:10], "%Y-%m-%d").strftime("%m-%d-%Y")
        try:
            dictF[date] += 1
        except:
            dictF[date] = 1
    for entry in table[1]["Created"]:
        date = datetime.datetime.strptime(
            entry[:10], "%Y-%m-%d").strftime("%m-%d-%Y")
        try:
            dictT[date] += 1
        except:
            dictT[date] = 1


parseCountsPerDay(gsd.table_Chats, dict_From, dict_To)
parseCountsPerDay(gsd.table_Snaps, dict_From, dict_To)

dict_From = dict(sorted(dict_From.items(), key=lambda x: x[0].lower()))
dict_To = dict(sorted(dict_To.items(), key=lambda x: x[0].lower()))

F = plt.plot(dict_From.keys(), dict_From.values(), label="Snaps received")
T = plt.plot(dict_To.keys(), dict_To.values(), label="Snaps sent")

plt.xticks(rotation=90, fontsize=9)

plt.legend(loc="upper left")
plt.xlabel("Date")
plt.ylabel("# of Snaps (chats and snaps)")
plt.title("Number of Snaps sent and recieved each day of the last month")
plt.subplots_adjust(bottom=0.25)

plt.show()
