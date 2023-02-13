from time import *
import random as r


# print(time())  # it start counting seconds from 1971 to now.


def mistakes(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except Exception as e:
            error += 1
    return error

def speed_time(s_time, e_time, user_input):
    time_delay = e_time - s_time
    Roundoff_time = round(time_delay,2)
    speed = len(user_input)/ Roundoff_time
    return round(speed)


while True:
    ck = input("Ready to Test : yes/ no : ")
    if ck == "yes":
        paragraph = ['''The global scope of the health benefits from the discoveries
        documented in this book is breathtaking. Their implementation
        into national health care policies will significantly reduce and
        eliminate three leading causes of mortality in the world today:
        cardiovascular disease, strokes and deaths caused by the side 
        effects of prescription drugs. This book provides the guidelines to
        reach this goal.''']

        test1 = r.choice(paragraph)
        print('*********** Typing Speed ***********')
        print(test1)
        print()
        print()
        start_time = time()
        user_input = input("Enter The Following Texts : \n")
        end_time = time()

        print("Speed : ", speed_time(start_time, end_time, user_input),"W/Sec")
        print("Error : ", mistakes(test1, user_input))
    elif ck == "no":
        print("Thank You")
        print()
        break