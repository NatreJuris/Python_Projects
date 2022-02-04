class Protected:
    def __init__(self):             #create protected class
        self.__privateVar = 22

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):      #sets to private
        self.__privateVar = private

obj = Protected()       #protected and private object
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate() 



















