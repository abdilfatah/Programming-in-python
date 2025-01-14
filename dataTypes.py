a = 10.0
print(type(a))  # <class 'float'>

c = "String" 
print(type(c))  # <class 'str'>

d = [1,2,3] 
print(type(d))  # <class 'list'>

## Strings

a = "Hello, World!" # single line string
b = '''Hello, World!
evbdvsbvdbvsbvdbvsbvvsv
ehwehgwjhgehgwhgegjwhegjwhgejh
w   ffeg    fgfeghf ghefgh  f''' # multi line string
c = " Hello, World! \
evbdvsbvdbvsbvdbvsbvvsv\
ehwehgwjhgehgwhgegjwhegjwhgejh" # multi line string

print(a)
print(b)
print(c)

# Strings are Arrays
a = "Hello "
print(a[1])  # e

name = "John"
length = len(name)
print(length)  # 4

# Slicing
print(name[1:3])  # oh

print (a+name) # Hello John

# String Methods
print(name.lower())  # john
print(name.upper())  # JOHN
print(name.replace("J", "K"))  # Kohn
print(name.split("o"))  # ['J', 'hn']

# Check String
print("J" in name)  # True
print("J" not in name)  # False

# String Concatenation
a = "Hello "
b = "World"
c = a + b
print(c)  # Hello World

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # My name is John, and I am 36

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.

# type casting
a = 10
b = str(a)
print(type(b))  # <class 'str'>

a = "10"
b = int(a)
print(type(b))  # <class 'int'>
