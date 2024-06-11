def sum():
    addition = 3 + 4
    return addition


# good practice to receive the returned value in a variable
outcome = sum()

print(outcome)

# ______________________________


def colors():
    a = 5
    print("Red")
    print("Yellow")
    print("Green")
    print("Blue")
    return a
    print("Purple")
    print("Orange")
    # ^^ notice how these are fainted out because they're after return, and the function has been exited


colors_outcome = colors()
# prints everything, not just a = 5:
print(colors_outcome)

# ______________________________


def colors2():
    a = 5
    print("Red")
    print("Yellow")
    print("Green")
    print("Blue")
    print("Purple")
    print("Orange")
    if a > 5:
        return a
    elif a < 5:
        return a - 5
    else:
        return 1

multiple_returns = colors()
print(multiple_returns)