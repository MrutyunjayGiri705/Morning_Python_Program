# 1. Re-raise the same exception (most common)
# try:
#     x = int("abc")
# except ValueError:
#     print("Conversion failed")
    # raise  # Re-raises the same ValueError exception
# 2. Re-raise after partial handling
# try:
#     risky_operation()
# except Exception as e:
#     cleanup()
#     raise

  
# 3. Raise a new exception instead
# try:
#     x = int("abc")
# except ValueError as e:
# #     raise RuntimeError("Invalid input provided")
# 4. Exception chaining (recommended when raising a new one)
try:
    x = int("abc")
except ValueError as e:
    raise RuntimeError("Invalid input provided") from e

