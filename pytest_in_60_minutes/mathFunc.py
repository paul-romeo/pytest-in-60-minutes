# Function "add" adds two values x and y or 
#   joining two strings x and y 
def add(x, y=2):
    return x + y 


#  Function "multiply" multipies of two numbers x and y (or)
#   repeats the first value (x) by number of times (y)
def multiply(x, y=2):
    return x * y 

import json
class StudentDB: 
    # Constructor 
    def __init__(self):
        self.__data = None

    def connect(self, dataFile):
        with open(dataFile) as jsonFile: 
            self.__data = json.load(jsonFile)

    def getData(self, name):
        for student in self.__data["students"]:
            if student["name"] == name: 
                return student 

    def close(self):
        pass
