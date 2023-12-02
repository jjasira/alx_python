def safe_print_division(a, b):
    while True:
        try:
            result = a/ b
            break
        except ZeroDivisionError:
            result = None
        finally:
            print("inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))

    

    
