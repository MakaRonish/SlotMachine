import random
import time
MAX_LINES=3
MAX_BET=100
MIN_BET=10
with_draw_amount={}

element_in_line=["A","B","C"]

def deposit():
    balance=input("Amount to Deposit=")
    while True:
        if balance.isdigit() and int(balance)>0:
            return int(balance)
        else:
            print("Invalid amount!!")
            balance=input("Amount to Deposit=")

def line():
    user_line=[]
    while True:
        user_number_of_line=input("How many line do you wanna guess?=")
        if user_number_of_line.isdigit() and 0<int(user_number_of_line)<4:
            count=0
            while count!=int(user_number_of_line):
                line=input(f"Guess the {count+1} line (A-B-C)=").split("-")
                if len(line)==3:
                    valid_line=True
                    for i in range(3):
                        line[i]=line[i].upper()
                    for i in line:
                        if i not in element_in_line:
                            valid_line=False
                            break
                    if valid_line:
                        user_line.append(line)
                        count+=1
                    else:
                        print("choose element from A-B-C")
                else:
                    print("Need 3 character from A to C")
            return user_line
        else:
            print("Invalid number of line")

        

def bet():
    while True:
        amount=input("Enter the amount to bet= $")
        if amount.isdigit() and (MIN_BET<= int(amount) <=MAX_BET):
            return int(amount)
        else:
            print(f"Invalid amount to bet\n amount need to be between {MIN_BET} and {MAX_BET}")


def winnig_line():
    line1=[str(random.choice(element_in_line)),str(random.choice(element_in_line)),str(random.choice(element_in_line))]
    line2=[str(random.choice(element_in_line)),str(random.choice(element_in_line)),str(random.choice(element_in_line))]
    line3=[str(random.choice(element_in_line)),str(random.choice(element_in_line)),str(random.choice(element_in_line))]
    full_line=[line1,line2,line3]
    return full_line



def result(winning,user_line):
    line_match_count=0
    for comp,user in zip(winning,user_line):
        if comp==user:
            line_match_count+=1
    return line_match_count

def amount_won(c,amount_bet):
    total_prize=amount_bet
    if c==3:
        total_prize*=100
    elif c==2:
        total_prize*=50
    elif c==1:
        total_prize*=25
    else:
        total_prize*=0
    return total_prize

def spin_slot(balance):
    winning_line=winnig_line()
    user_line=line()
    while True:
        amount=bet()
        if amount>balance:
            print(f"balance is not enough {balance}")
            while True:
                Deposit=input("y to deposit n to end game=").lower()
                if Deposit.isalpha():
                    if Deposit=="y":
                        balance=deposit()
                        break
                    elif Deposit=="n":
                        return balance
                    else:
                        print("invalid!!!!!")

        else: 
            break
    correct_guess=result(winning_line,user_line)
    time.sleep(1)
    print("it is spinninggggg")
    time.sleep(1)
    print(f"Winning line")
    time.sleep(1)
    for i in winning_line:
        print(i)
    time.sleep(1)
    print(f"user line:")
    for i in user_line:
        print(i)
    time.sleep(1)
    print(f"Correct line count = {correct_guess}")
    winning_amount=amount_won(correct_guess,amount)
    time.sleep(1)
    print(f"you won {winning_amount}$")
    balance=winning_amount+balance-amount
    print(f"balance={balance}")

    return balance

def withdraw(balance):
    print(f"Current balance: ${balance}")
    if balance==0:
        print("your balance is 0$")
        return balance
    while True:
        amount=input("Amount to withdraw=$")
        if amount.isdigit():
            amount=int(amount)
            if amount<=balance:
                name=input("enter you name to withdraw=")
                with_draw_amount[name]=with_draw_amount.get(name,0)+ amount
                balance-=amount
                print(f"Amoint withdraw=${amount}")
                print(f"new balance=${balance}")
                print(with_draw_amount)
                return balance
            else:
                print("Not enough balance")
        else:
            print("invalid amount!!!!")
    




        


def main():
    print("Welcome to Slot machine")
    while True:
        print("1) start game")
        print("2) End")
        choice=int(input("option="))
        if choice==1:
            balance=deposit()
            while True:
                balance=spin_slot(balance)
                print(f"Balance after spin = ${balance}")
                while True:
                    time.sleep(1)
                    continue_playing=input("W to with draw\nY to continue\nN to exit=").lower()
                    if continue_playing.isalpha():
                        if continue_playing=="y":
                            balance=spin_slot(balance)
                        elif continue_playing=="n":
                            return
                        elif continue_playing=="w":
                            print(f"Balance before withdrawal = ${balance}")
                            balance=withdraw(balance)
                            print(f"Balance after withdrawal = ${balance}")
                        else:
                            print("invalid!!!!!")        
        elif choice==2:
            break
        else:
            print("invalid")
main()



    















    
    





            
