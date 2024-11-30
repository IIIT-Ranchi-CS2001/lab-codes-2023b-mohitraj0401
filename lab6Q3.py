def my_max(*args):
    if isinstance(args[0], list):
        container = args[0]
    elif isinstance(args[0], set):
        container = args[0]
    elif isinstance(args[0], tuple):
        container = args[0]
    else:
        raise ValueError("Unsupported data type")
    
    max_value = container[0]
    for item in container:
        if item > max_value:
            max_value = item
    return max_value
