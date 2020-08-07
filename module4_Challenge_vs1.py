# Lee Haynes

# http://www.devcoder.me.uk
# + 44 (0) 785 374 0636
# Email: devcodertrainingsite@yandex.com
# Twitter: https://twitter.com/Devcoder2019
# Linkedin: https://www.linkedin.com/in/leehaynes/

#######################################################
#######################################################

# Loan Calculator
# 1. Ask user to enter an deposit
# 2. Ask user to enter total number of repayments 
# 3. Enter the total amount 
# 4. Provide total to repy inc interest
# 5. Early repayment saving 


# place holders 
depoistPaid = 0 # optional
monthlyPayment = 0
loanAmount = 0
intRate = 0.05 # 5%
numOfPayments = 0
earlyRepayment = 1.25 # Interest saved for an early repayment

# Gather data 

depoistPaid = int(input("Enter the deposit you wish to pay £   "))
print("")
numOfPayments = int(input("Enter the total number of payments you wish to make "))
print("")
loanAmount = int(input("Enter the amount you wish to borrow! £ "))

# calulate 

# How much I want to borrow minus dpeosit leavs ballnce left to pay 
ballance = loanAmount - depoistPaid 

# dividing the ballance by monthly pament entered 
total = ballance / numOfPayments

# Repayment how much by how long 
monthlyTotal =  ballance / numOfPayments  

# calculate the interest 
totalInterest = monthlyTotal * intRate

# Repayment how much by how long and calculate the interest
totalDue =  ballance + totalInterest

# Early repayment output 
saving = round(totalDue /  12 * earlyRepayment)
newTotal = totalDue - saving
print("")
print(" - - " * 15)
print("")

# print 

print(f"You have paid a deposit of £ {depoistPaid}")
print("")
print(f"You have chosen to repay the loan in {numOfPayments} monthly payments ")
print("")
print(f"You have borrowed £ {loanAmount}, and you have paid a deposit of £ {depoistPaid}, and the reaming ballance is £ {ballance}") 
print("")
print(f"You have aggreed to pay the £ {ballance} with {numOfPayments} monthly payment \nmaking a monthly total to pay of £ {monthlyTotal}")
print("")
print(f"The final amount to pay is: £ {totalDue}")

earlyRepayment = input("Do you wish to repay the loan early? ")
if earlyRepayment == "yes":
    print("The total you will be saving is £" + str (saving))
    print(f"The new total will be {newTotal}")
else: 
    print("Nothing has changed")
