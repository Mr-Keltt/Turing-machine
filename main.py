from turingMachine import TuringMachine

def commandAssembler(commandSets):
    a = []
    for commandSet in commandSets:
        for command in commandSet:
            a.append(command)
    return a

while True:

    if int(input("Хотите выполнить программу (0 - Нет; 1 - Да): ")):
        k = int(input("Введите K:"))
        m = int(input("Введите M:"))
        n = int(input("Введите N:"))
        s = "1"*k + "0"*m + "1"*n
        print()

        print("Начальная строка: " + s)

        print()

        d = int(input("Введите число (0 - Просто вывести результат; 1 - Показать последовательное решение; 2 - Показать все действия): "))

        print()

        commandSet1 = [# удаление лишнего и превращение нулей в еденици.
                        "q1.1.q1.0.R", "q1.0.q2.1.R", "q2.0.q2.1.R", "q2.1.q3.0.R", "q3.1.q3.0.R", "q3.0.q4.0.L", 
                        "q4.0.q4.0.L", 
                        # приведение строки в вид m-1 2 m
                        "q4.1.q5.0.R", "q5.0.q6.1.L", "q6.0.q7.0.L","q7.1.q8.1.L", "q8.1.q8.1.L", "q8.0.q9.0.L", 
                        "q9.0.q10.0.S", "q9.1.q10.1.L", "q10.1.q10.1.L", "q10.0.q11.1.R", "q11.1.q11.1.R", 
                        "q11.0.q12.0.R", "q12.1.q12.1.R", "q12.0.q4.0.L",
                        # приведение строки в вид m 2 m и завершение
                        "q7.0.q13.0.L", "q13.1.q13.1.L", "q13.0.q0.1.S"
                        ]

        commandSets = commandAssembler([commandSet1])

        tm = TuringMachine(s, commandSets, d)
        tm.execute()
        if (d == 0):
            print(tm.ribbon)

        print()

        if int(input("Хотите увидеть набор команд (0 - Нет; 1 - Да): ")):
            print(commandSets)
            print("Всего " + str(len(commandSets)) + " команд")
        print()
    else:
        break