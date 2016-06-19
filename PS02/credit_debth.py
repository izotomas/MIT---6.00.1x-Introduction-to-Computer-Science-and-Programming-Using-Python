monthlyInterestRate = annualInterestRate/12.0
totalPay = 0
for i in range(1,13):
    payment = balance * monthlyPaymentRate
    totalPay += payment
    balance = balance - payment
    balance = balance * (1 + monthlyInterestRate)
    print 'Month:', i
    print 'Minimum monthly payment:',round(payment,2)
    print 'Remaining balance:', round(balance,2)
print 'Total paid:', round(totalPay,2)
print 'Remaining balance:', round(balance,2)
