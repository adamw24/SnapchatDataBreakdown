import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import GeneralSnapDataBreakdown as gsd
import datetime

# Count the number of snaps sent and recieved every day and reformat the date.


def parseCountsPerDay(table, dictF, dictT):
    for entry in table[0]["Created"]:
        date = datetime.datetime.strptime(
            entry[:10], "%Y-%m-%d").strftime("%m-%d")
        try:
            dictF[date] += 1
        except:
            dictF[date] = 1
    for entry in table[1]["Created"]:
        date = datetime.datetime.strptime(
            entry[:10], "%Y-%m-%d").strftime("%m-%d")
        try:
            dictT[date] += 1
        except:
            dictT[date] = 1


def main():
    dict_From = {}
    dict_To = {}
    parseCountsPerDay(gsd.table_Chats, dict_From, dict_To)
    parseCountsPerDay(gsd.table_Snaps, dict_From, dict_To)

    # Sort the dictionary based on the date
    dict_From = dict(sorted(dict_From.items(), key=lambda x: x[0].lower()))
    dict_To = dict(sorted(dict_To.items(), key=lambda x: x[0].lower()))

    # Plot
    F = plt.plot(dict_From.keys(), dict_From.values(), label="Snaps received")
    T = plt.plot(dict_To.keys(), dict_To.values(), label="Snaps sent")
    plt.xticks(rotation=70, fontsize=9)
    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.ylabel("# of Snaps (chats and snaps)")
    plt.title("Number of Snaps sent and recieved each day of the last month")
    plt.subplots_adjust(bottom=0.25)
    plt.show()


if __name__ == '__main__':
    main()
