"""
This is my app for making the learning of new english words easy
"""
from collections import OrderedDict
from pyexcel_ods3 import get_data, save_data


class Words:
    """
    Words class -
    This has the interfaces
        - To add a new word
        - Find number of words added
        - Status : details about number of words learnt
        - Search for the existence of a word
    """

    def __init__(self, filename, sheet):
        """
        The calc sheet containing the words is loaded to the set self.words
        And the user is given choice of what he may want to do.
        """
        self.file = filename
        self.words = set()
        try:
            self.data = get_data(filename)
            self.words = set(x[0] for x in self.data[sheet])
        except KeyError:
            pass
        self.count = len(self.words)
        while True:
            self.choice_reader()

    def choice_reader(self):
        """
        This function is repeatedly called by the init method.
        This directs the control to different functions implementing the features.

        Function names are put in a list which are mapped to the options given to user
            - this is a way of simulating a swith case(python doesn't have it's own switch case)
        """
        defList = ['add_word', 'status', 'total_words', 'find_word']
        print(
            "1 : Add a new word\
            2 : Show the Status\
            3 : Strength of collection\
            4 : Find a word\n\
            \rNon Numbers : Quit")
        try:
            """ exec can execute a string as a line of code
                here it is invoking the different functions of the class
            """
            exec("self." + str(defList[int(input()) - 1]) + "()") #ignore exec-used
        except ValueError:
            """ ValueError is generated in case of incompatible datatype conversion is
                attempted or operations carried on imcompatible datatypes
            """
            print("Thank you for using!!\
                \nHave a nice day")
            exit(0)

    def add_word(self, newWord="None"):
        """
        Why the optional parameter:
        This function is called in two different scenarios
            - When the choice is 1 : for adding a new word
            - Searching for a word, the word is not found
              it is automatically added in that case.
        The set is popped and words are put in a list:
            Since I want to randomize the order of the words
            I am popping the words - set.pop() returns a random element
        An OrderedDict needs to be created for saving the data to ods sheet
            - The keys are the sheet names
            - Vales are the data in the sheet
                - each sublist is a row
                - values in each sublist correspond to columns
        """
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
        writeData.update({"Sheet1": shuffledList})
        save_data(self.file, writeData)
        print(newWord, " has been added" if len(shuffledList)
              > self.count else "is already available")
        self.count += 1 if len(shuffledList) > self.count else 0
        self.total_words()

    def total_words(self):
        """
        Just print how many words are there
            return the value of self.count
        """
        print("You Have: ", self.count, " Words")
        # To print all the words in the file
        # for i, w in zip(range(self.count), self.words):
        # print(i, w)

    def status(self):
        """
        Details of how many words have been learnt
        """
        pass

    def find_word(self):
        """
        Find if a word exists, if not make an attempt to add it
        by calling the add_word menthod
        """
        newWord = input()
        if newWord in self.words:
            print("Yes")
        else:
            print("No : Adding the word", newWord)
            self.add_word(newWord)


if __name__ == '__main__':
    """
    Start the execution here
    The project will be divided into modules
        importing problems are avoided
    """
    w = Words("words.ods", "Sheet1")
