#This should appear as soon as the program runs, asking the user to choose between two given options.
import math
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment      - to calculate the amount of interest you'll earn on interest")
print("bond            - to calculate the amount you'll have to pay on a home loan") 
financialCal = input() # The user inputs the choice they made. 

#There are two different financial calculators, 'Investment' and 'Bond'

#Investment:
if financialCal.lower() == "investment": #if the user selects and inputs 'investment' the needed information will be asked. 
    amount = float(input("The amount of money that you are depositing: R"))
    interestRate = float(input("Interest rate (%): "))
    numYears = int(input("Number of years you plan on investing for: "))
    interest = input("Simple interest or Compound interest: ")

    #There are two types of interests to calculate Investment, simple and compound interest.

    #Simple interest:
    if interest.lower() == "simple interest": #The total amount when ​simple interest is applied is calculated.
        totalAmount = amount * (1 + interestRate/100 * numYears)
        print(f"The amount of interest you'll earn on interest is {totalAmount:.2f}") #Display the total amount.
    #Compond interest:    
    elif interest.lower() == "compound interest": #The total amount when ​compound interest is applied is calculated.
        totalAmount = amount * math.pow((1+interestRate/100),numYears)
        print(f"The amount of interest you'll earn on interest is R{totalAmount:.2f}") #Display the total amount.
        
#Bond:
elif financialCal.lower() == "bond": #if the user selects and inputs 'bond' the needed information will be asked. 
    houseValue = float(input("The present value of the house: R"))
    interestRate = float(input("Interest rate (%): "))
    numMonths = int(input("Number of months you plan to take to repay the bond: "))
    #The amount that a user will have to be repaid on a home loan each month is calculated.
    repayment = ((houseValue * math.pow((interestRate/12)+1,numMonths))*(interestRate/12))/((math.pow(interestRate/12 + 1,numMonths)-1))
    print(f"The amount you'll have to pay on a home loan is R{repayment:.2f}") #Display the amount.
else:
    print("Enter a valid entry (Investment or Bond).") # If the user doesn’t type in a valid input, an error message will be displayed.  


