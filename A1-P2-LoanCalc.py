#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

"""
Student Name: William Wilson
Program Title: Logic and Programming
Description: Assignment 1 Loan Calculator
"""

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Amount borrowed input
    amountBorrowed=float(input("Please enter the amount you borrowed: $"))
    #Interest Rate % input
    interestRate=float(input("Please enter the interest rate percentage: "))
    #Number of years input
    loanLength=int(input("Please enter the length of the loan in years: "))

    #i=interest rate/5200
    i=interestRate/5200
    # print(i)
    #weekly=i/1-(1+i)**-52n *A (break it down step1(1+i)step2 -52*n step3 ()**-52n step4 1-ans ()**-52n step5 i/step1-4ans step6 step5*A)
    step1=1+i
    step2=-52*loanLength
    step3=step1**step2
    step4=1-step3
    step5=i/step4
    weeklyAmount=step5*amountBorrowed
    #print the amounts for loans, interest, loan and weekly payments
    print()
    print("Amount of the loan: ${0:.2f} \nInterest Rate: {1}% \nLength of the loan: {2} years".format(amountBorrowed, interestRate, loanLength))
    print("weekly loan payments will be: {0:.2f}".format(weeklyAmount))

    # YOUR CODE ENDS HERE

main()