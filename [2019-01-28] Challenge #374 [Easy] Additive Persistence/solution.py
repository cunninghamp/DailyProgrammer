number = int(input("Enter a number: "))

loopcount = 0


def makemap(inputnumber):

    global loopcount

    sumofnumbers = 0

    digits = map(int, (str(inputnumber)))

    for i in digits:
        sumofnumbers = sumofnumbers + i
    print(f"Sum of numbers is: {sumofnumbers}")
    loopcount += 1
    if len(str(sumofnumbers)) > 1:
        makemap(sumofnumbers)
    return loopcount


if len(str(number)) == 1:
    print(loopcount)
else:
    answer = makemap(number)
    print(f"Loops required: {answer}")