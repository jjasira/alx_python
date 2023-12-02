def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    elif len(a_dictionary) == 0:
        return None
    else:
    
        max_value = 0

        for key in a_dictionary:
            if a_dictionary[key] > max_value:
                max_value = a_dictionary[key]
        
        for key in a_dictionary:
            if a_dictionary[key] == max_value:
                return key
        

