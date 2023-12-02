def safe_print_division(a, b):
    try:
        result = a/ b
        
    except ZeroDivisionError:
        result = None
    finally:
        print("inside result: {}".format(result))
        print("{} / {} = {}".format(a, b, result))

    
