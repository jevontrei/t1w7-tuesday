def greet():
    print("I love coding!!")
    
greet()

# ___________________

scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope2():
    scope_in = "inside"

# print(scope_in)
# ^^ doesn't work!