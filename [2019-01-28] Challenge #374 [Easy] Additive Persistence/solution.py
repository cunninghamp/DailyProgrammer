# Ask the user for a number
number = int(input("Enter a number: "))

loopcount = 0


def calculate_additive_persistence(inputnumber):

    # Using global variable so that it doesn't reset to 0 on each recursive loop
    global loopcount
    sumofnumbers = 0

    # Creates a list object containing the individual digits of the input number
    digits = map(int, (str(inputnumber)))

    # Calculate the sum of the individual digits
    for i in digits:
        sumofnumbers = sumofnumbers + i
    print(f"Sum of numbers is: {sumofnumbers}")

    # Increment the loop count
    loopcount += 1

    # If the sum of the individual digits is greater than 9 (i.e. more than 1 digit
    # long), do a recursive loop of the function
    if sumofnumbers > 9:
        calculate_additive_persistence(sumofnumbers)

    # Finally, return the number of times the function ran (looped)
    return loopcount


# If the input number is less than 10 the answer is 0, no loops required
if number < 10:
    answer = 0
else:
    answer = calculate_additive_persistence(number)

print(f"Loops required: {answer}")
