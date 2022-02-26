# Operators String
opt = '+-//**%'

# Stack List to evaluate the prefix expression
stack = []

# Taking input from user
# Example: * + 1 2 - 3 4
exp = input("Enter the prefix expression seperated with space: ")

# Removing whitespaces and Converting it to a List
exp.strip()
p_exp = exp.split()

# Finding the length of the list p_exp
L = len(p_exp)

try:
    for i in range(L-1, -1, -1):

        # Popping the top two elements from the stack, calculating and pushing the result back
        if p_exp[i] in opt:
            a = stack.pop()
            b = stack.pop()

            s = "{0} {1} {2}".format(a, p_exp[i], b)
            r = round(eval(s), 2)
            stack.append(r)
        
        # Pushing the operands to the stack
        else:
            stack.append(int(p_exp[i]))
    
    # Printing the result
    if len(stack) == 1:
        print("The result is:", stack.pop())
    
    # Otherwise, the expression is invalid
    else:
        print("The expression is invalid")

# Printing the error, if any
except Exception as e:
    print("The expression is invalid")
    print("\n",e)
    
