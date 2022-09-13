from ctypes import pointer
from pointer import Pointer
import time

class TuringMachine:

    def __init__(self, ribbon, commands, showWorkCheck = 0):
        self.__ribbon = ribbon
        self.__commands = commands
        self.__pointer = Pointer(self)
        self.__showWorkCheck = showWorkCheck
        

    @property
    def ribbon(self):
        return self.__ribbon

    @ribbon.setter
    def ribbon(self, val):
        self.__ribbon = val


    def execute(self):

        while self.__pointer.curCond != 0:
            self.showWork(self.__showWorkCheck)

            for i in range(0, len(self.__commands)):
                options = [0, 0, 0, 0, ""]
                check = 0

                for j in range(0, len(self.__commands[i])):
                    if ord(self.__commands[i][j]) >= ord("0") and ord(self.__commands[i][j]) <= ord("9"):
                        options[check] = options[check] * 10 + int(self.__commands[i][j])

                    elif self.__commands[i][j] == ".":
                        check += 1

                    else:
                        options[4] = self.__commands[i][j]

                if self.__pointer.curCond == options[0] and self.__ribbon[self.__pointer.curCord] == str(options[1]):
                    self.__pointer.curCond = options[2]
                    self.__ribbon = self.__ribbon[:self.__pointer.curCord] + str(options[3]) + self.__ribbon[self.__pointer.curCord+1:]

                    if options[4] == "R":
                        self.__pointer.moveRight()

                    elif options[4] == "L":
                        self.__pointer.moveLeft()

                    break

                elif i == len(self.__commands) - 1:
                    self.__pointer.curCond = 0
                    self.__ribbon = "Невыполнимо"
                    return

        while True:
            self.showWork(self.__showWorkCheck)
            if self.__ribbon == "":
                self.__ribbon = "0"
                break
            
            if self.__ribbon[0] == "0":
                if self.ribbon[self.__pointer.curCord - 1] == "0":
                    self.__pointer.moveLeft()
                self.__ribbon = self.__ribbon[1:]
            elif self.__ribbon[-1] == "0":
                self.__ribbon = self.__ribbon[:-1]
            else:
                break

    def showWork(self, debag = 0):
        if debag > 0:
            if debag == 1:
                print("\033[H\033[J")
                print(self.__ribbon[:self.__pointer.curCord] + "(q" + str(self.__pointer.curCond) + ")" + self.__ribbon[self.__pointer.curCord:])
                time.sleep(1)
            else:
                print(self.__ribbon[:self.__pointer.curCord] + "(q" + str(self.__pointer.curCond) + ")" + self.__ribbon[self.__pointer.curCord:])