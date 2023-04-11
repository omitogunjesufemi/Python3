def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("Handling run-time error:", err)
else:
    print("Else clause added")
finally:
    print("Finally clause added")
