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


# match statement
# match statement is a new feature in python 3.10
# it is used to compare a value against a set of constants
# it is similar to switch statement in other languages
# it is used to replace long if-elif-else statements

# Example 1
# http_status = 404
# match http_status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Internal Server Error")
#     case _:
#         print("Unknown Status Code")

# for loop
# for loop is used to iterate over a sequence
for i in range(5):
    print(i)

fav_fruits = ["apple", "banana", "orange", "grapes"]
for idx, fruit in enumerate(fav_fruits):
    print(idx, fruit)


# while loop
# while loop is used to execute a block of code multiple times
i = 0
while i < len(fav_fruits):
    print(fav_fruits[i])
    i += 1

#nested loop
for i in range(3):
    for j in range(3):
        print(i*j)