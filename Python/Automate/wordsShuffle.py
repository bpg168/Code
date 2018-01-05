"""
This is my app for making the learning of new english words easy
"""
from collections import OrderedDict
from pyexcel_ods3 import get_data, save_data


class Words:
    """
    Words class
    """

    def __init__(self, filename, sheet):
        self.file = filename
        listData = list()
        try:
            self.data = get_data(filename)
            listData = list(x[0] for x in self.data[sheet])
        except KeyError:
            pass
        self.words = set(listData)
        self.count = len(self.words)
        while True:
            self.choice_reader()
        

    def choice_reader(self):
        defList = ['add_word', 'status', 'total_words', 'find_word']
        print(
            "1 : Add a new word\
            2 : Show the Status\
            3 : Strength of collection\
            4 : Find a word\n\
            \rNon Numbers : Quit")
        try:
            exec("self."+ str(defList[int(input()) - 1])+"()")
        except ValueError:
            print("Thank you for using!!\
                \nHave a nice day")
            exit(0)

    def add_word(self, newWord = "None"):
        print(self.count)
        if newWord == 'None':
            newWord = input("Enter a word to add :\t")
        print(self.words)
        self.words.add(newWord)
        shuffledList = []
        for i in range(0, self.count):
            try:
                shuffledList.append([(self.words.pop())])
                # print("pop", self.words.pop())
            except KeyError:
                pass
        w = dict()
        writeData = OrderedDict()
        writeData.update({"Sheet1" : shuffledList})
        save_data(self.file, writeData)
        print(newWord, " has been added" if len(shuffledList) > self.count else "is already available")
        self.count += 1 if len(shuffledList) > self.count else 0 
        self.total_words()

    def total_words(self):
        print("You Have: ", self.count, " Words")
        #To print all the words in the file
        # for i, w in zip(range(self.count), self.words):
            # print(i, w)

    def status(self):
        pass

    def find_word(self):
        newWord = input() 
        if newWord in self.words:
            print("Yes")
        else:
            print("No : Adding the word", newWord)
            self.add_word(newWord)

if __name__ == '__main__':
    w = Words("words.ods", "Sheet1")

