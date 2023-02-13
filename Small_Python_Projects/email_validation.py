'''
email = input('Enter Your Email : ') 
# sample normal email - root@gmail.com
# smallest email - r@g.in
space = ()
upper = ()
i_else = ()
if email:
    if len(email)>=6:
        if email[0].isalpha():  # isalpha() => to check the character is alphabetical or not
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i == " ":
                            print('Space is not allowed')
                            space = 1
                        elif i.isalpha():
                            if i == i.upper():
                                print('UpperCase letters are not allowed')
                                upper = 1
                        elif i == i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            print('You have entered Wrong Email')
                            i_else = 1
                    if space == 1 or upper == 1 or i_else == 1:
                        print()
                    else:
                        print('You Entered a Correct email address')
                else:
                    print('User "." only once')
            else:
                print('User "@" only once')
        else:
            print('First letter must be alphabetic')
    else:
        print('Email must be more than 6 characters')
else:
    print('Oops, Somthing Went Wrong.....!')

    # Use slicinng in Programe for email slicing
'''


############# Email Using Regex #############

import re    # with the help of "re" we can use ReGex
# ^[a-z] - this is use for  "^" it means start-with and then we giv parameter a-to-z
# in regex [\._]? if we want to search any character then we use "\" and then gives parameter like "." or "_" or "whatever.." and the "?" denote that if perticular item is present then it is consider as 1 if not then 0 and if items are more than 1 then it returns False
# \w use search a character in entire string
# [.]\w{2,3}$ => [.]\w it denotes find "." and on {2,3}th index and $ means the control goes in reverse format

email_condition = "^[a-z] + [\.]?[a-z 0-9]+ [@]\w + [.]\w{2,3}$ "
user_email = input('Enter Your Email : ') # "rn.root_123@gmail.com" => This is correct way write email.
if re.search(email_condition,user_email):
    print("You Enterd Correct Email.")
else:
    print('You have entered Wrong Email')
