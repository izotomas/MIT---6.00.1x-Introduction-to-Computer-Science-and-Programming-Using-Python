#balance = 320000
#annualInterestRate = 0.2

monthlyInterest = annualInterestRate / 12.0
debt = balance
low = debt / 12.0
high = (debt * (1 + monthlyInterest)**12) / 12.0
pay = (low + high)/2.0
while(low < (high - 0.001)):
    pay = (low + high)/2.0
    debt = balance
    for i in range(12):
        debt = debt - pay
        debt = debt * (1 + monthlyInterest)
    if debt <= 0:
        high = pay
    else:
        low = pay
print 'Lowest Payment: ' + str('%.2f' %pay)
