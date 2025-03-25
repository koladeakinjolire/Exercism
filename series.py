def slices(series, length):
     if series == '':
        raise ValueError('series cannot be empty')
     if length > len(series):
        raise ValueError('slice length cannot be greater than series length')
     if length ==  0:
        raise ValueError('slice length cannot be zero')
     if length <  0:
        raise ValueError('slice length cannot be negative')
     result = [series[i:i+length] for i in range(len(series) - length + 1)]
     return result


print(slices('01234', 2))
print(slices('97867564', 3))
print(slices('97867564', 0))
print(slices('97867564', 9))
print(slices('97867564', -1))