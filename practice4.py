def logic_operations():
    '''
    In this exercise, you will practice using logical operators in Python, 
    specifically and, or, not, ==, and !=. 
    You will run a series of statements and observe the output to understand how these operators work.

    Below are the steps you will follow:

    Define a few boolean variables.
    Use the and operator to combine these variables and print the result.
    Use the or operator to combine these variables and print the result.
    Use the not operator to invert the boolean value of a variable and print the result.
    Use the == operator to compare these variables and print the result.
    Use the != operator to compare these variables and print the result.
    Observe and understand the output of each operation.
    '''
    # add your code here
    print(True)
    print(False)
    print(True or False)
    print(True or 0)
    print(True or 1)
    print(False and 1)
    print(False or 0)
    print(False or 1)
    print(not True)
    print(not False)
    print(not 1)
    print(not 0)
    a = 1
    print(a==1)
    print(a!=1)
    print(a==0)

    #Supplementary Content: XOR Operation
    #The XOR operation (exclusive OR) is a bitwise operation that compares corresponding bits of two binary numbers. 
    # The result is 1 if and only if the corresponding bits are different (one is 1, the other is 0); 
    # otherwise, the result is 0.
    a = 5  # Binary: 101
    b = 3  # Binary: 011
    print(a,b,a ^ b)  # 6 (Binary: 110)

logic_operations()
