def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
        return None
    except Exception as e:
        print("Error:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        pass