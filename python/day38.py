# Write a function called guess_a_number. The function 
# should ask a user to guess a randomly generated number. If the 
# user guesses a higher number, the code should tell them that the 
# guess is too high, if the user guesses low, the code should tell 
# them that their guess is too low. The user should get a maximum 
# of three guesses. When the user guesses right, the code should 
# declare them a winner. After three wrong guesses, the code 
# should declare them a loser.
from random import randint


def guess_a_number():
    count=0
    random_number=randint(1, 11)
    print(random_number)
    while count<3:
        num=int(input("please guess a number between 1-10, you have 3 choice : "))
        count+=1
        if num>random_number:
            print("your guess is too high")
        elif num<random_number:
            print("your guess is too low")
        else:
            print("congratulation, you won")
    if count>=3:
        print("you are a loser")
    else:
        print("you are winner")
        
        
guess_a_number()
