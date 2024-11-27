def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == None or not hey_bob.strip():
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

print(response('Are you okay?'))
print(response('WHATS WRONG WITH YOU?'))
print(response('STOP THAT NOW'))
print(response(''))
print(response('I really do not like this behaviour of yours.'))
print(response('Okay if like my spacebar quite a bit?  '))
print(response("This is a statement ending with whitespace      "))