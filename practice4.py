def logic_operations(binary1,binary2):
    '''
    In this exercise, you will practice using logical operators in Python, 
    specifically and, or, not, ==, and !=. 
    You will create a function that takes two boolean inputs and prints the following in order:

    1. The first boolean value.
    2. The second boolean value.
    3. The negation of the first boolean value.
    4. The negation of the second boolean value.
    5. The result of the first boolean value OR the second boolean value.
    6. The result of the first boolean value AND the second boolean value.
    7. Whether the first boolean value is equal to the second boolean value.
    8. Whether the first boolean value is not equal to the second boolean value.

    Observe and understand the output of each operation.

    '''
    # add your code here
    
    #Supplementary Content: XOR Operation
    #The XOR operation (exclusive OR) is a bitwise operation that compares corresponding bits of two binary numbers. 
    # The result is 1 if and only if the corresponding bits are different (one is 1, the other is 0); 
    # otherwise, the result is 0.
    a = 5  # Binary: 101
    b = 3  # Binary: 011
    print(a,b,a ^ b)  # 6 (Binary: 110)

binary1 = True
binary2 = True
logic_operations(binary1,binary2)
