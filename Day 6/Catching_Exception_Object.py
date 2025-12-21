try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)
    print("Type of exception:", type(e))
