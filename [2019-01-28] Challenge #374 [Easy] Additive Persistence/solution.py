number = int(input("Enter a number: "))

loopcount = 0


def calculate_additive_persistence(inputnumber):

    global loopcount
    sumofnumbers = 0

    # Creates a list object containing the individual digits of the input number
    digits = map(int, (str(inputnumber)))

    for i in digits:
        sumofnumbers = sumofnumbers + i
    print("Sum of numbers is: " + str(sumofnumbers))
    loopcount += 1
    if len(str(sumofnumbers)) > 1:
        calculate_additive_persistence(sumofnumbers)
    return loopcount


if number < 10:
    answer = 0
else:
    answer = calculate_additive_persistence(number)

print("Loops required: " + str(answer))