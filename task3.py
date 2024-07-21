def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Division operation complete.")

divide_numbers(10, 20)