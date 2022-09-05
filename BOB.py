def response(hey_bob):
    message = hey_bob.strip()
    if not message:
        return "Fine. Be that way!"
    elif message.isupper() and message.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif message.endswith('?'):
        return "Sure."
    elif message.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
