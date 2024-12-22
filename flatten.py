def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, (str, bytes)):
            result.append(item)
        elif hasattr(item , "__iter__") and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    filtered_result = [item  for item in result if isinstance(item, int)]

    return filtered_result