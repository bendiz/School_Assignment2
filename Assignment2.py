def hours(seconds: int, boolean: bool) -> int:
    """A function that takes in seconds from 00:00(midnight) and a boolean
    that returns true for a 24-hour format and false for a 12-hour format.

    Args:
    seconds (int): Seconds from 00:00 (midnight).
    boolean (bool): Boolean True/False.

    Returns:
    int: Hours as a 12h or 24h clock depending on the boolean parameter.
    """
# 24hr format
    if boolean:
        return int(seconds / 3600)
# 12hr format
    else:
        return int((seconds / 3600) % 12 or 12)


def minutes(seconds: int) -> int:
    """A function that recieves seconds from 00:00(midnight), and a boolean
    that returns true for 24-hour format and false for 12-hour format

    Args:
    seconds (int): Seconds from 00:00 (midnight)

    Returns:
    int: Returns the minutes of the last hour"""

    return int(seconds/60 % 60)


def lamp(digit: int) -> list:
    """A function that takes in a digit and returns a list that represents
    the digit in a 7-segment lamp.

    Args:
    digit (int): Recieves a digit to represent in a 7-segment lamp

    Returns:
    list: A list of numbers 0 or 1 indicating if lamp is off/on """

    match digit:
        case 0:
            return [1, 1, 0, 1, 1, 1, 1]
        case 1:
            return [0, 1, 0, 0, 1, 0, 0]
        case 2:
            return [1, 1, 1, 0, 0, 1, 1]
        case 3:
            return [1, 1, 1, 0, 1, 1, 0]
        case 4:
            return [0, 1, 1, 1, 1, 0, 0]
        case 5:
            return [1, 0, 1, 1, 1, 1, 0]
        case 6:
            return [1, 0, 1, 1, 1, 1, 1]
        case 7:
            return [1, 1, 0, 0, 1, 0, 0]
        case 8:
            return [1, 1, 1, 1, 1, 1, 1]
        case 9:
            return [1, 1, 1, 1, 1, 1, 0]


def showClock(seconds: int, boolean: bool) -> list:
    """A function that recieves seconds 00:00 (midnight) and a boolean which
    is True for 24-hour format and False for 12-hour format.
    Returns a list with the four lists that returns from the lamp function.
    This function will call lamp() 4 times.

    Args:
    seconds (int): Seconds from 00:00 (midnight)
    boolean (bool): True / False

    Returns:
    list: A list with the four lists that returns from the lamp function """

    if (seconds >= 86400) or (seconds < 0) or (type(boolean) != bool):
        return "Please enter a valid time and True/False for 12-hr/24-hr clock"
    clock = []
    hour = hours(seconds, boolean)
    minute = minutes(seconds)
    for time in [hour, minute]:
        # Checks if hour and minute only includes 1 digit and append 0 in front
        if len(str(time)) == 1:
            clock.append(lamp(0))
            clock.append(lamp(time))
        # If hour and minute has a length of 2 digits, return them unchanged
        else:
            for digit in str(time):
                clock.append(lamp(digit))
    return clock


if __name__ == "__main__":
    print("""This clock takes an input of time in seconds,
and a boolean True/False for displaying 24hr/12hr clock.""")
    time = int(input("Input the time in seconds: ").strip())
    true_or_false = input("Input True (24hr), False (12hr): ").lower().strip()
    if true_or_false == "true":
        print(showClock(time, True))
    else:
        print(showClock(time, False))
