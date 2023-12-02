def best_score(a_dictionary):
    
    if len(a_dictionary) == 0:
        max_value = None
    
    max_value = 0

    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
    
    for key in a_dictionary:
        if a_dictionary[key] == max_value:
            return key
    
    
   
