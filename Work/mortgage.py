# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000

while principal > 0:
    if principal < 12:
        principal = principal * (1 + rate/12) - (payment + extra_payment)
    else:
        principal = principal * (1 + rate/12) - (payment + extra_payment)
    total_paid = total_paid + payment

print('Total paid', round(total_paid,2))
