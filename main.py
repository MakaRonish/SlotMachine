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
            return amount
        else:
            print(f"Invalid amount to bet\n amount need to be between {MIN_BET} and {MAX_BET}")


def winnig_line():
    l=[str(random.randint(1,3)),str(random.randint(1,3)),str(random.randint(1,3))]
    return l

def result():
    winning=winnig_line()
    user_line=line()
    line_match_count=0
    for comp,user in zip(winning,user_line):
        if comp==user:
            line_match_count+=1
    return line_match_count

def amount_won():
    correct_guess=result()
    total_prize=1
    if correct_guess==3:
        total_prize*=100
    elif correct_guess==2:
        total_prize*=50
    else:
        total_prize*=0
    return total_prize

def main():
    print("Welcome to Slot machine")
    









li=["1","2","3"]
li1=["1","2","1"]
c=0
for a,b in zip(li,li1):
    if a==b:
        c+=1
print(c)
print(a)





    
    





            
