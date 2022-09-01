from fractions import Fraction
import fractions

print("What would you like to do? Add (+) Subtract (-) Divide (/) or Multiply (*)?") 
function = input()
print("input your first fraction")
num1 = input(Fraction()) 
print("input your second fraction")
num2 = input(Fraction())


# At this point i used google.

if function == '+':
    result = Fraction(num1) + Fraction(num2)
elif function == '-':
    result = Fraction(num1) - Fraction(num2)
elif function == '*':
    result = Fraction(num1) * Fraction(num2)
elif function == '/':
    result = Fraction(num1) / Fraction(num2)
else:
    print("Input character is not recognized!")


print(result)


# This the way i had it before

# print("What would you like to do? Add (+) Subtract (-) Divide (/) or Multiply (*)?") 
# function = input()
# num1 = input(int())
# num2 = input(int())

# ans = num1 + function + num2

# print(ans)