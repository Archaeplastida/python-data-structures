def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    new_dict = {}
    if len(keys) == 0:
        return None
    if len(values) == 0:
        return {x:None for x in keys}
    val_len_remaining = len(values)
    ind_count = 0
    for x in keys:
        if val_len_remaining == 0:
            for x in keys[ind_count:]:
                new_dict[x] = None
            return new_dict
        new_dict[x] = values[ind_count]
        val_len_remaining -= 1
        ind_count += 1
    return new_dict