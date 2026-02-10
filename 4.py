class StringHandler:
    def getString(self):
        self.s = input()
        
    def printString(self):
        print(self.s.upper())

# создание объекта
obj = StringHandler()
obj.getString()
obj.printString()
