import random
MAX_LINES=3
MAX_BET=100
MIN_BET=10

def deposit():
    balance=input("Amount to Deposit=")
    while True:
        if balance.isdigit() and int(balance)>0:
            return int(balance)
        else:
            print("Invalid amount!!")
            balance=input("Amount to Deposit=")

def line():
    while True:
        valid_number=["1","2","3"]
        line=input("Guess the line (1-2-3)=").split("-")
        valid=True
        for i in line:
            if len(line)==3 and i in valid_number:
                valid=True
            else:
                valid=False
                break
        if not valid:
            print("please enter in right format (1-2-3)\nThe number should be between (1-3)")
        else:
            return line
        

def bet():
    while True:
        amount=input("Enter the amount to bet= $")
        if amount.isdigit() and (MIN_BET<= int(amount) <=MAX_BET):
            return int(amount)
        else:
            print(f"Invalid amount to bet\n amount need to be between {MIN_BET} and {MAX_BET}")


def winnig_line():
    l=[str(random.randint(1,3)),str(random.randint(1,3)),str(random.randint(1,3))]
    return l

def result(winning,user_line):
    line_match_count=0
    for comp,user in zip(winning,user_line):
        if comp==user:
            line_match_count+=1
    return line_match_count

def amount_won(c):
    
    total_prize=1
    if c==3:
        total_prize*=100
    elif c==2:
        total_prize*=50
    else:
        total_prize*=0
    return total_prize


def main():
    print("Welcome to Slot machine")
    while True:
        print("1) start game")
        print("2) End")
        choice=int(input("option="))
        if choice==1:
            balance=deposit()
            winning_line=winnig_line()
            user_line=line()
            while True:
                amount=bet()
                if amount>balance:
                    print("balance is not enough {balance}")
                else: 
                    break
            correct_guess=result(winning_line,user_line)
            print(f"Winning line:{winning_line}")
            print(f"user line:{user_line}")

            winning_amount=amount_won(correct_guess)
            print(f"you won {winning_amount}$")
            balance=winning_amount+balance-amount
            print(f"balance={balance}")
        elif choice==2:
            break
        else:
            print("invalid")

main()
    















    
    





            
