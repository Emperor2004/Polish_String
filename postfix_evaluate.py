# Operators String
opt = '+-//**%'

# Stack List to evaluate the postfix expression
stack = []

# Taking input from user
# Example: 1 2 + 3 4 - *
exp = input("Enter the postfix expression seperated with space: ")

# Removing whitespaces and Converting it to a List
exp.strip()
p_exp = exp.split()

try:
    for i in p_exp:
        
        # Popping the top two elements from the stack, calculating and pushing the result back
        if i in opt:
            a = stack.pop()
            b = stack.pop()

            s = "{0} {1} {2}".format(b, i, a)
            r = round(eval(s), 2)
            stack.append(r)
        
        # Pushing the operands to the stack
        else:
            stack.append(int(i))
    
    # Printing the result
    if len(stack) == 1:
        print("The result is: ", stack.pop())
    
    # Otherwise, the expression is invalid
    else:
        print("Invalid expression")

# Printing the error, if any
except Exception as e:
    print("Invalid expression")
    print("\n", e)
