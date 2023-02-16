def hours(seconds: float, boolean: bool) -> int or str:
    """A function that takes in seconds from 00:00(midnight) and a boolean that returns
    true for a 24-hour format and false for a 12-hour format.
    
    Args:
    seconds (float): Seconds from 00:00 (midnight).
    boolean (bool): Boolean True/False.

    Returns:
    int: Hours as a 12h or 24h clock depending on the boolean parameter.
    """
    hours = round(seconds / 3600)
    if boolean:
        return hours
    else:
        if (hours == 12):
            return str(hours % 12).zfill(2)
        else:
            return hours % 12

print(hours(3600*12, False))

def minutes(seconds: float) -> int:
    """A function that recieves seconds from 00:00(midnight), and a boolean that
    returns true for 24-hour format and false for 12-hour format
    
    Args:
    seconds (float): Seconds from 00:00 (midnight)
    
    Returns:
    int: Returns the minutes of the last hour"""
    pass

def lamp(digit: int) -> list:
    """A function that takes in a digit and returns a list that represents
    the digit in a 7-segment lamp.
    
    Args:
    digit (int): Recieves a digit to represent in a 7-segment lamp
    
    Returns:
    list: A list of numbers 0 for off and 1 for on indicating if the lamp is off/on """
    pass

def showClock(seconds:float, boolean:bool) -> list:
    """A function that recieves seconds 00:00 (midnight) and a boolean which
    is True for 24-hour format and False for 12-hour format. Returns a list with the four lists that
    returns from the lamp function. This function will call lamp() 4 times.
    
    Args:
    seconds (float): Seconds from 00:00 (midnight)
    boolean (bool): True / False
    
    Returns:
    list: A list with the four lists that returns from the lamp function """
    pass
