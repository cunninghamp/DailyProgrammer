def same_necklace(first, second):
    match = first == second

    if not match:
        for i in range(len(second)):
            second = second[1:] + second[0]
            print('Reordered string is: ' + second)
            if first == second:
                match = True
                break

    print(match)

same_necklace("nicole", "icolen")
