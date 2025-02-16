def two_fer(name=""):
    return f'One for {name or 'you'}, one for me.'


print(two_fer("Alice"))
print(two_fer("Alex"))
print(two_fer())