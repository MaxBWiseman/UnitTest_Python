
def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        if numbers == []:
            return False
        else:
            evens = 0
            
        for n in numbers:
            if n % 2 == 0:
                evens += 1
        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens(5))
    
    """
    __name__ == "__main__" Python idiom is used to ensure that
    certain code is only executed when the script is run directly, and not when
    it is imported as a module in another script.
    """