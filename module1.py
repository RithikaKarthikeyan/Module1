#EX-01

a=int(input("Enter a number: "))
if (a%2==0):
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")

# EX-02

a = (0 == True)
b = (False == False)
c = (True + True)
d = (False + 9)

print("a is", a)
print("b is", b)
print("c:", c)
print("d:", d)

# EX-03

print('T')
print('a')

# EX-04

a=int(input("Enter the real part:"))
b=int(input("Enter the imaginary part:"))

x=complex(a,b)
print("The complex number is:",x)
print("Real part:",x.real)
print("Imaginary part:",x.imag)

# EX-05 

men_stepped_on_the_moon=input("Enter a string: ")
print(men_stepped_on_the_moon)