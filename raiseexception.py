a = 10
b = 0
try:
    # condition for checking for negative values
    if a < 0 or b < 0:
        # raising exception using raise keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("ZERO DIVISION ERROR OCCURED")
