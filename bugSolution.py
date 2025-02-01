def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or raise a more specific exception, or return a different value

result = function(10, 0)
print(result)  # Output: 0