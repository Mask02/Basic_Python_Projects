#!/usr/bin/python

print("****************Calculator****************")


operand1 = int(input("Enter a number: "))

operand2 = int(input("Enter a numbar: "))

operator = input("Enter operator: " )

if operator == "+":
	
	print("Answer =" , operand1 + operand2)

elif operator == "-":
	
	print("Answer =" , operand1 - operand2)

elif operator == "*":
	
	print("Answer =" , operand1 * operand2)

elif operator == "/":
	
	print("Answer =" , operand1 / operand2)

elif operator == "%":
	print("Answer =" , operand1 % operand2)
else:
	print("Invaild Operator")
