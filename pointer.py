

class Pointer:

    def __init__(self, turingMachine):
        self.__curCord = 0
        self.__curCond = 1
        self.__turingMachine = turingMachine
    

    @property
    def curCord(self):
        return self.__curCord

    @property
    def curCond(self):
        return self.__curCond
    
    @curCond.setter
    def curCond(self, val):
        self.__curCond = val


    def moveLeft(self):
        if (self.__curCord == 0):
            self.__turingMachine.ribbon = "0" + self.__turingMachine.ribbon
        else:
            self.__curCord -= 1

    def moveRight(self):
        if (self.__curCord == len(self.__turingMachine.ribbon)-1):
            self.__turingMachine.ribbon = self.__turingMachine.ribbon + "0"
        
        self.__curCord += 1