# Greeting someone

# def greet():
#     print("Hello coder, Steve!")


# greet()

# # _______________________
# # Generalised coding (parameters):


# def greet(name):
#     # print("Hello coder, " + str(name) + "!")
#     print(f"Hello coder, {name}!")


# greet("Joel")

# # _______________________


# def greet(fname, lname):
#     """_summary_

#     Args:
#         fname (_type_): _description_
#         lname (_type_): _description_
#     """
#     print(f"Hello coder, {fname} {lname}!")


# greet("Joel", "von Treifeldt")

# # _______________________
# # Positional args:


# def subtract(a, b):
#     difference = a - b
#     return difference


# result = subtract(3, 4)
# print(result)

# # _______________________
# # Default args:


# def subtract(a, b=1):
#     difference = a - b
#     return difference


# result = subtract(4)
# print(result)

# result = subtract(4, 3)
# print(result)

# _______________________
# Keyword args:


def subtract(b=1, a=4):
    difference = a - b
    return difference

result = subtract(a=4, b=3)
print(result)
