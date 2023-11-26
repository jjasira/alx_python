def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

def fibonacci_sequence(n):
    my_list2 = []
    my_list = list(range(n))
    for element in my_list:
        
        my_list2.append(fib(element))
    return my_list2



