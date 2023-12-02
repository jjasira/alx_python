def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("{} / {} = {}".format(a, b, result))

# Example usage:
a = 10
b = 2
result = safe_print_division(a, b)
