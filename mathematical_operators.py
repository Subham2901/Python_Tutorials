#Mathematical Operations On python
"""Expressions- (50+60) is known as expression,
the no. on which we perform our operations are known as operands
 and the symbols like"+,-,/,*" are known as operators
 and operands are also known as literals when they are constants"""
b= 50+60 #addition
print(b)
b=60-50 #subtraction
print(b)
b=60/2 #division which will return float value
print(b)
b=50.0/3.0# here also the returning value is a float no.
print(b)
b=50.0/10 # here also the returning no. is a float no.
print(b)
b=30//2 #divison which will return integer value( this is also known as the floor division as here we get the answer by trunkating the decimal value)
print(b)
b=30*2; # multiplication
print(b)
"""Modulo operations this operations returns the remainder of the 
division between the two operands"""
b=30%10 #modulo operation(remainder 0)
print(b)
b=21%5 #remainder 1
print(b)
""" Exponent operator (**)"""
b=5**2 #here double asterisk is used as exponent operator
print(b)
"""When performing multiple operations together
the python follows a particular precedence of the operators to be used for calculations
1.parenthesis
2.Exponents
3.Multiplications&divisions and modulo ( this works left to right,the operator appearing on the left have the highest priority than that odf the operator appearing on the right side)
4.Addition&Subtraction(this works left to right too)
"""
b=(5+10)-14*12+2
print(b)

