from pr2 import Test
import random
answersList = [["What is your name?", []], ["What is your surname?", []], ["How old are you?", []], ["Are you married", []], ["Where do you work?", []]]

for f in range(5):
    answer = ["What is your name?", "What is your surname?", "How old are you?", "Are you married", "Where do you work?"]
    MyAns = Test()
    for i in range(5):
        randoma = random.randint(0, len(answer) - 1)
        MyAns.__init__(vopros=answer[randoma])
        answer.pop(randoma)
        MyAns.__str__()
        ans = input("Your answer:")

        if ans == "Stop" or ans == "Exit":
            exit()
        else:
            MyAns.save(otv=ans)
    print("Thank you for answers")
    MyAns.res()

#    for i in range(5):
#        ind = MyAns.otvet[i]
#        inde = answer.index(ind)
#        check = 0
#        if answersList[inde][1] != []:
#            for j in range(len(answersList[inde][1])):
#                if
