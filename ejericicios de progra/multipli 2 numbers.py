def multiply_without_operator(x, y):
    result = 0
    # If one of the numbers is negative, make both numbers positive
    neg_result = (x < 0) ^ (y < 0)
    x = abs(x)
    y = abs(y)

    # Perform repeated addition
    for _ in range(y):
        result += x

    # Negate the result if necessary
    if neg_result:
        result = -result

    return result

# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
product = multiply_without_operator(num1, num2)
print("Product:", product)
