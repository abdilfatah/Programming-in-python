# Logical operators
# and, or, not
# and: both conditions must be true
# or: one condition must be true
# not: reverse the result, if true, return false, if false, return true

# Example 1
x = 5
print(x > 3 and x < 10)  # True
print(x > 3 or x < 4)  # True
print(not(x > 3 and x < 10))  # False

# Example 2
a = True
b = False

print(a and b)  # False
print(a or b)  # True
print(not a)  # False
print(not b)  # True


# control flow
bill_total = 224

discount = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("bill grearter than 100!")
    bill_total = bill_total - discount
elif bill_total > 200:
    print("bill greater than 200!")
    bill_total = bill_total - discount2

else:
    print("bill less than 100!")

print("Total Bill: "+ str(bill_total))

