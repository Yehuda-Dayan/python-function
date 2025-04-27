def reverse_string(s):
    """
    This function takes a string as input and returns the string reversed.
    
    :param s: str - The string to be reversed
    :return: str - The reversed string
    """
    return s[::-1]

string = str(input("Enter a string to reverse: "))
reversed_string = reverse_string(string)
print(f"The reversed string is: {reversed_string}")