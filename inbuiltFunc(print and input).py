"""print()  is an inbuilt function which consists of one or multiple arguments
separated by a comma separator. It is used to display outputs"""
print("i love python") # here the string is an argument
print(5+10) #here the expression is an argument
print("a+b = ",10) #here the string as well as the number both are an argument separated by an comma separator
a=2
b=3
print(a+b)
print("a+b = ",a+b)
print("hello", " ","world")
"""Now we wil use the  .format() to print the desried data, .format() is an inbuilt func() of the String class """
x=50
y=10
"""We will use {} tuples and provide index nos. to print the desired outputs"""
print("{0} * {1} = {2}".format(x,y,x*y))
"""Now we will see how to use "sep=" argument in tjhe print() """
print("hello","world",sep="++++++++++++")
""" WE CAN ALSO USE C-PROGRAMMING STYLE FORMATTOIKNG TO ACCESS THE ARGUMENT IN THE PRINT STATEMENT"""
k1="Subham"
print("who is a good boy ? %s"%k1)#Similarly  we can use %d(integeer),%f(float)
"""__________________________________________________________________________________________________________________________________"""
"""__________________________________________________________________________________________________________________________________"""
"""__________________________________________________________________________________________________________________________________"""
"""__________________________________________________________________________________________________________________________________"""
"""NOW WE WILL SEE HOW TO USE input() function in 
python to take user defined values"""
value=input("Enter some value")
print(value)
"""now here the value is getting stored in string format to change the format we can use explicit typecasting """
value =float(input("Enter a value :"))
print(value)# now the output will be a float no.
"""_____________________________________________________________________________________________________________________________________"""
"""_____________________________________________________________________________________________________________________________________"""
"""_____________________________________________________________________________________________________________________________________"""
"""LETS CHECK ALL THE BUILTIN FUNTIONS THAT PYTHON PROVIDES"""
print(dir(__builtins__))# this will diaplay all the builtin func() that python provides
