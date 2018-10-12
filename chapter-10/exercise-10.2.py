def capitalize_nested(t):
    res = []
    for s in t:
        if type(s) == list:
            # res.append(capitalize_nested(s))
            s = capitalize_nested(s)
        else:
            # res.append(s.capitalize())
            s = s.capitalize()
        res.append(s)
    return res


print(capitalize_nested(['hej', ['hello']]))
print(capitalize_nested(['herro', ['hello'], 'bye']))