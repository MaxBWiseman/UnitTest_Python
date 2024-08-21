
def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        
        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens([2, 1, 4]))
    
    """
    __name__ == "__main__" Python idiom is used to ensure that
    certain code is only executed when the script is run directly, and not when
    it is imported as a module in another script.
    """
    
"""
Type Check:

It checks if the input numbers is a list using isinstance(numbers, list).
If numbers is not a list, it raises a TypeError with the message "A list was not passed into the function".
Count Evens:

If numbers is a list, it counts the number of even numbers in the list.
This is done using a list comprehension [1 for n in numbers if n % 2 == 0] which creates a list of 1s for each
even number in numbers.
The sum() function then adds up these 1s to get the total count of even numbers, stored in the variable evens.
Return Value:

If the count of even numbers (evens) is zero or odd, it returns False.
If the count of even numbers is even, it returns True.
Main Execution:

When the script is run directly, it calls even_number_of_evens([2, 1, 4]).
Since [2, 1, 4] is a list, it proceeds to count the even numbers.
The even numbers in the list are 2 and 4, so evens is 2.
Since 2 is even, the function returns True.
"""