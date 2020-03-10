def same_necklace(first, second):
    # Check for an immediate match
    match = first == second

    # If no match, time to start reordering characters and comparing
    if not match:
        # The loop will run the same number of times as the number of characters in the string
        for i in range(len(second)):
            # Strings are zero-indexed, so to get the string from the second character to the last character
            # would be:
            # print(second[1:])
            #
            # And to get the first character:
            # print(second[0])
            #
            # Loop for the same number of times as the length of the second string which is reordered
            # by one character each time
            second = second[1:] + second[0]
            if first == second:
                match = True
                break
    print(match)


same_necklace("nicole", "icolen")
same_necklace("nicole", "lenico")
same_necklace("nicole", "coneli")
same_necklace("aabaaaaabaab", "aabaabaabaaa")
same_necklace("abc", "cba")
same_necklace("xxyyy", "xxxyy")
same_necklace("xyxxz", "xxyxz")
same_necklace("x", "x")
same_necklace("x", "xx")
same_necklace("x", "")
same_necklace("", "")
