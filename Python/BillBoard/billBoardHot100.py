from urllib import request
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os


def Make_Soup(URL):
    try:
        print("Connecting to: ", URL)
        pageSource = request.urlopen(URL)
        print("Got the content\n")
        pageSoup = BeautifulSoup(pageSource, 'html.parser')
        return pageSoup
    except Exception as e:
        # CrashReport(e)
        print(e)


def Collector(URL):
    try:
        soupData = Make_Soup(URL)
        i = 1
        songColl = dict()
        for song in soupData.findAll(attrs={'class': 'chart-row__container'}):
            songTitle = song.find(attrs={'class': 'chart-row__song'}).text
            songArtist = song.find(
                attrs={'class': 'chart-row__artist'}).text.replace('\n', '')
            # print(songTitle)
            Title = [songTitle, songArtist]
            songColl[str(i)] = Title
            print(str(i) + "\t" + songTitle, "\n\t" + songArtist)
            i += 1
        print(songColl)
        return songColl
    except Exception as e:
        print(e)
        pass


def SongSaver(SONGCOLL):
    os.system("rm *.json")
    currentTime = datetime.now()
    attributes = [currentTime.year, currentTime.month,
                  currentTime.day, currentTime.hour, currentTime.minute]
    Time = str()
    for i in attributes:
        Time = Time + str(i) + "-"
    songFile = "BillBoardHot100 @ " + Time[:-1] + ".json"
    print('\n' + songFile)
    with open(songFile, "w") as f:
        json.dump(SONGCOLL, f, indent=4)
    print("Older file(if any) is no longer available\n",
          "New file has been written")
    with open(songFile) as f:
        print(json.load(f))


if __name__ == '__main__':
    URL = 'https://www.billboard.com/charts/hot-100'
    SONGCOLL = Collector(URL)
    CHOICE = input("Would you like to save a copy of JSON? y/N")
    if CHOICE == 'y' or CHOICE == 'Y':
        SongSaver(SONGCOLL)
