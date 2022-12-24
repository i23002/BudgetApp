import sys
import matplotlib.pyplot as plt
from tabulate import tabulate

def main():
    record = {}
    
    #GETTING THE BUDGET AMOUNT
    try:
        initial_deposit = int(input("Budget Amount: "))
    except ValueError:
        sys.exit("Please enter a valid Amount")
    
    #SECURITY
    if initial_deposit <= 0:
        sys.exit(f"Budget Amount cannot be {initial_deposit}")
    
    #SAVING IN RECORDS
    record["initial_deposit"] =  initial_deposit
    
    #GETTING USER INPUTS 
    print("NOTE: AFTER ENTERING ALL THE ITEMS, IF THE PROGRAM PROMPTS FOR DESCRIPTION,AMOUNT, JUST HIT ENTER WITHOUT ENTERING ANYTHING.")
    while True:
        try:
            des , bal = input("Description,amount: ").strip().split(",")
            #SECURITY MEASURES
            if des.isdecimal() or des.isdigit() or des.isnumeric():
                sys.exit(f"Description needs a String but got this {des}")
            if int(bal) <= 0:
                sys.exit(f"Balance cannot be {bal}")
            record[des] = int(bal) 
        except ValueError:
            break
    
    #ASKING FOR DETAILED SUMMARY
    try:
        val = int(input("Get Detailed Summary(1/0)? "))
    except ValueError:
        sys.exit("Please enter a valid response.")
        
    #REFINING THE RECORD DATA FOR PLOTTING
    x,y = refine(record)
    
    #STORING THE DATA AS A 2D LIST 
    table = write(record)
    
    #PRINTING BEGINS 
    print()
    print("*"*10+" SUMMARY "+"*"*10)
    print()
    print("INITIAL DEPOSIT:", initial_deposit)
    print()
    
    #PRINTS THE TABLE
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    print()
    
    #PRINTING THE ANSWER
    if val == 0:
        print(Budget(record, val))
    if val == 1:
        summary1 , summary2, summary3, balance = Budget(record, val)
        print(summary1)
        print(summary2)
        print(summary3)
        print(balance)
        
    
    #PRINTS THE SCATTER PLOT 
    plt.bar(x, y, color ='maroon',width = 0.4)
    plt.xlabel("Items")
    plt.ylabel("Amount Used")
    plt.title("Amount spent in different Items")
    plt.show()
    
class Budget_Catagory:
    def __init__(self):
        self._deposit = 0
        self._withdraw = 0
        self._current = 0
        self.message = ''

     #DEPOSIT METHOD DEPOSITS THE AMOUNT
    def deposit(self, amount):
        self._current += amount
        self._deposit += amount
        
    
    #WITHDRAW METHOD WITHDRAWS THE AMOUNT
    def withdraw(self, amount):
        self._current -= amount
        self._withdraw += amount
        
    #GET_BALANCE METHOD RETURNS THE CURRENT BALANCE
    def get_balance(self):
        if self._current > 0:
            return f"CURRENT BALANCE: {self._current}"
        else:
            return f"CURRENT BALANCE: {0}"
    
    #CHECK FUNDS METHOD RETURNS HOW MUCH HAS BEEN DEPOSITED AND HOW MUCH WAS USED
    def check_funds(self):
        statement1 = f"Amount Deposited: {self._deposit}."
        statement2 = f"Amount Used: {self._withdraw}."
        return statement1 , statement2
    
    #RETURNS THE AMOUNT USED IN PERCENT
    def check_funds_percent(self):
        cal = (100*self._current)/self._deposit
        statement = f"Amount Used: {100 - round(cal)}%."
        return statement

def Budget(dic, val=False):
    """ BUGTET FUNCTION USES THE METHODS OF BUDGET CATEGORY TO STORE THE INPUT INFORMATION IN AN ARRAY"""
    arr = []
    item = Budget_Catagory()
    item.deposit(dic["initial_deposit"])
    for i in dic:
        if i != "initial_deposit":
            item.withdraw(dic[i])
    if val == False:
        return item.get_balance()
    if val == True:
        ans1 , ans2 = item.check_funds()
        summary = item.check_funds_percent()
        balance = item.get_balance()
        arr.append(ans1)
        arr.append(ans2)
        arr.append(summary)
        arr.append(balance)
        return arr     

def write(dic):
    """WRITE FUNCTION CONVERTS THE DICTIONARY DATA IN A 2D ARRAY"""
    lis=[]
    lis.append(["DESCRIPTION" , "AMOUNT"])
    for i in dic:
        if i != "initial_deposit":
            lis.append([i,dic[i]])
    return lis

def refine(dic):
    """ REFINES THE DICTIONARY DATA IN TWO SEPARATE ARRAY FOR PLOTTING PURPOSE """
    x = []
    y = []
    
    for i in dic:
        if i != "initial_deposit":
            x.append(i)
            y.append(dic[i])
    return x,y


if __name__ == "__main__":
    main()