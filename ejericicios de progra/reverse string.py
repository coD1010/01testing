def reverse_string(input_string):
    reversed_string = ''
    # Iterate through the string from the end to the beginning
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string

# Test the function
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)