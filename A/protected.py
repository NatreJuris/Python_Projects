class Protected:
    def __init__(self):             #create protected class
        self.__privateVar = 22

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):      #sets to private
        self.__privateVar = private

class Protected1:
    def __init__(self):                 #protected variable
        self._protectedVar = 0


obj = Protected()       # private object
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

obj = Protected1        #protected object
obj._protectedVar = 34
print(obj._protectedVar)






















