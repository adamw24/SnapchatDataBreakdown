import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def parseCounts(table, dictF, dictT):
    for name in table[0]["From"]:
        if name != "no name":
            try:
                dictF[name] += 1
            except:
                dictF[name] = 1
    for name in table[1]["To"]:
        if name != "no name":
            try:
                dictT[name] += 1
            except:
                dictT[name] = 1


def main():
    # Use pandas to parse the downloaded snapchat data into tables.
    table_Chats = pd.read_html('D:\SnapchatData\html\chat_history.html')
    table_Snaps = pd.read_html('D:\SnapchatData\html\snap_history.html')

    dict_From = {}
    dict_To = {}

    # Parse the number of snaps sent and recieved from each friend from the table of chats and table of snaps
    # ignores users with no name (unsure why that occurs).
    parseCounts(table_Chats, dict_From, dict_To)
    parseCounts(table_Snaps, dict_From, dict_To)

    # Sort the from snaps
    dict_From = dict(sorted(dict_From.items(), key=lambda item: item[1]))
    people_to = dict_To.keys()
    people_from = dict_From.keys()

    nameList = []
    fromSnaps = []
    toSnaps = []

    # Add all the users that sent me snaps (if I have not sent a snap back, fill To with 0)
    for user in people_from:
        nameList.append(user)
        fromSnaps.append(dict_From[user])
        try:
            toSnaps.append(dict_To[user])
        except:
            toSnaps.append(0)

    # Adds all the users I snapped but who have not snapped me back (if any)
    for user in people_to:
        # If does not error, then it is already added.
        try:
            dict_From[user]
        except:
            nameList.insert(0, user)
            fromSnaps.insert(0, 0)
            toSnaps.insert(0, dict_To[user])

    # Use anonymous names for privacy reasons (does not reveal everyones username)
    anonymous_names = []
    for i in range(len(nameList)):
        anonymous_names.append("{} {}".format("user", len(nameList) - i))

    # Shows the top N results
    topN = 30

    # Plot stacked bar graph

    xstuff = np.arange(len(nameList[-1*topN:]))
    width = 0.40
    plt.figure(figsize=(10, 5))
    F = plt.bar(xstuff-width/2, fromSnaps[-1*topN:], width)
    T = plt.bar(xstuff+width/2,
                toSnaps[-1*topN:], width)
    plt.xticks(range(len(nameList[-1*topN:])), anonymous_names[-1*topN:],
               rotation=60, fontsize=9, horizontalalignment='right', verticalalignment='top')
    plt.yticks(range(0, 420, 20))
    plt.legend([T, F], ["Snaps to user", "Snaps from user"])
    plt.xlabel("Friends (usernames hidden for privacy)")
    plt.ylabel("# of Snaps (chats and snaps)")
    plt.title("Number of Snaps sent to/ from my friends in the last month")
    plt.subplots_adjust(bottom=0.205)
    plt.show()


if __name__ == '__main__':
    main()
