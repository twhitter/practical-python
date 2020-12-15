# sears.py

bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height of Sears Tower (meters)
num_bills = 1 # got to be at least 1 bill
day = 1 # track each day you put a dollar in front of tower

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills *2 

print('Number of days', day)
print('Number of bills', num_bills)
print('Final hieght', num_bills * bill_thickness)

