def meanFunction(*numbers):
    '''Returns the average of given numbers.

    There are no restrictions to given numbers.'''
    mean = sum(numbers)/len(numbers)
    print(f"The mean of the given list of numbers is: {mean}")

def medianFunction(*numbers):
    '''Returns the middle value of given numbers.

    The calculation is different depending on if the list of numbers is even or odd.'''
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 != 0:
        median_index_odd = int((len(sorted_numbers)-1)/2)
        print("This is median for odd list: ", numbers[median_index_odd])

    else:
        median_step_2 = int(len(sorted_numbers)/2)
        median_step_3 = int(len(sorted_numbers)/2) - 1
        median_index_even = int(sorted_numbers[median_step_2] + sorted_numbers[median_step_3]/2)
        print("This is median for even list: ", median_index_even)

def modeFunction(*numbers):
    '''Returns the value that appears the most often.

    Only shows the the lowest value if there are two values with the same amount of appearances.'''
    max_count = (0,0)
    for num in numbers:
        occurences = numbers.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    print("The mode of given list of numbers is: ", max_count[1])





